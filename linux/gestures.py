import evdev
from evdev import InputDevice, ecodes, UInput
import sys


def find_touchpad():
    for path in evdev.list_devices():
        dev = InputDevice(path)
        if 'touchpad' in dev.name.lower() or 'trackpad' in dev.name.lower():
            return dev
    return None


def main():
    touchpad = find_touchpad()
    if not touchpad:
        print("Ошибка: Тачпад не найден.")
        sys.exit(1)

    print(f"Используется устройство: {touchpad.name} ({touchpad.path})")

    caps = {
        ecodes.EV_KEY: [
            ecodes.KEY_VOLUMEUP,
            ecodes.KEY_VOLUMEDOWN,
            ecodes.KEY_BRIGHTNESSUP,
            ecodes.KEY_BRIGHTNESSDOWN,
        ]
    }
    ui = UInput(caps, name="touchpad-edge-controller")

    current_x = 0
    last_y = 0
    y_accumulator = 0  # Накопитель расстояния по вертикали

    # Зоны по оси X (настройте под свой тачпад)
    LEFT_EDGE_MAX = 300  # Левый край (громкость)
    RIGHT_EDGE_MIN = 4400  # Правый край (яркость)

    # ПУТЬ ДЛЯ ОДНОГО ШАГА: Чем больше это число, тем длиннее нужно провести палец
    # 150-200 единиц обычно равнялись примерно 1 см движения на стандартных тачпадах
    STEP_THRESHOLD = 130

    try:
        for event in touchpad.read_loop():
            if event.type == ecodes.EV_ABS:
                if event.code == ecodes.ABS_MT_POSITION_X:
                    current_x = event.value
                elif event.code == ecodes.ABS_MT_POSITION_Y:
                    current_y = event.value

                    if last_y != 0:
                        delta_y = current_y - last_y

                        # Проверяем, что палец находится именно в левой или правой зоне
                        is_left = (0 < current_x < LEFT_EDGE_MAX)
                        is_right = (current_x > RIGHT_EDGE_MIN)

                        if is_left or is_right:
                            # Суммируем движение в аккумулятор
                            y_accumulator += delta_y

                            # Если накопленное расстояние превысило порог шага
                            if abs(y_accumulator) >= STEP_THRESHOLD:
                                if y_accumulator > 0:
                                    # Свайп вниз -> Тише / Темнее
                                    key = ecodes.KEY_VOLUMEDOWN if is_left else ecodes.KEY_BRIGHTNESSDOWN
                                else:
                                    # Свайп вверх -> Громче / Светлее
                                    key = ecodes.KEY_VOLUMEUP if is_left else ecodes.KEY_BRIGHTNESSUP

                                # Отправляем одиночный клик клавиши (появится красивое OSD окно)
                                ui.write(ecodes.EV_KEY, key, 1)
                                ui.write(ecodes.EV_KEY, key, 0)
                                ui.syn()

                                # Сбрасываем аккумулятор, оставляя «остаток» для точности
                                y_accumulator = 0

                    last_y = current_y

            # Сброс при отрывании пальца от тачпада
            elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOUCH and event.value == 0:
                last_y = 0
                y_accumulator = 0

    except KeyboardInterrupt:
        print("\nСкрипт остановлен.")


if __name__ == '__main__':
    main()