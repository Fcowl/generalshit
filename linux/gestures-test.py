from itertools import cycle

import evdev
from evdev import InputDevice, ecodes


def find_touchpad():
    """Автоматический поиск устройства тачпада в системе"""
    devices = [InputDevice(path) for path in evdev.list_devices()]
    for dev in devices:
        # Ищем устройство, в названии которого есть touchpad
        if 'touchpad' in dev.name.lower() or 'trackpad' in dev.name.lower():
            return dev
    return None


def main():
    device = find_touchpad()
    if not device:
        print("Тачпад не найден автоматически. Укажите путь вручную (например, /dev/input/event4).")
        return

    print(f"Подключено к устройству: {device.name} ({device.path})")
    print("Слушаем события тачпада. Проведите пальцем по левому или правому краю...")

    try:
        for event in device.read_loop():
            print(event)
            if event.type == ecodes.EV_ABS:

                if event.code == ecodes.ABS_MT_POSITION_X:
                    current_x = event.value


                #current_x = [event.value for event.code in device.read_loop() if event.code == ecodes.ABS_MT_POSITION_X]

                    if current_x:
                        if current_x > 0 and current_x < 200:
                            print(f"👉 Движение в ЛЕВОМ крае (X: {current_x}) -> Управление громкостью")
                        elif current_x > 4400:
                            print(f"👉 Движение в ПРАВОМ крае (X: {current_x}) -> Управление яркостью")

    except KeyboardInterrupt:
        print("\nСкрипт остановлен.")


if __name__ == "__main__":
    main()