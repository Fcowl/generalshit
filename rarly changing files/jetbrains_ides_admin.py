from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
import functions2

def set_run_as_admin(shortcut_path: str, enable: bool = True) -> None:
    """Включает или отключает запуск ярлыка от имени администратора."""
    with open(shortcut_path, "r+b") as f:
        # Переходим к 21-му байту (смещение 0x15), где хранятся флаги заголовка
        f.seek(0x15)
        # Читаем текущий байт
        current_byte = f.read(1)[0]

        if enable:
            # Устанавливаем 6-й бит (0x20 = 00100000 в двоичной системе)
            new_byte = current_byte | 0x20
        else:
            # Сбрасываем 6-й бит
            new_byte = current_byte & ~0x20

        # Возвращаемся на 1 байт назад и перезаписываем его
        f.seek(0x15)
        f.write(bytes([new_byte]))

if __name__ == '__main__':
    taskbar_path : Path = Path(r"C:\Users\Fcowl\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar")
    LNKs_to_patch: list[str] = ['CLion.lnk', 'IntelliJ IDEA.lnk', 'PyCharm.lnk', 'Rider.lnk']
    LNKs_list: list[str] = functions2.files_in_folder(taskbar_path)

    for LNK in LNKs_list:
        if LNK in LNKs_to_patch:
            path:str = str(taskbar_path / LNK)
            set_run_as_admin(path,True)
            print(f"{LNK} patched")

r"""
# Пример использования
path = r"C:\Users\Fcowl\Desktop\FurMark (2).lnk"
set_run_as_admin(path, enable=True)
print("Параметр «Запуск от имени администратора» успешно включен.")
"""