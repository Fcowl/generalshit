import psutil
import pygetwindow as gw
import ctypes
from pathlib import Path

import win32gui
import win32process
import win32con


class ProcessNotFoundError(Exception):
    pass

def get_language() -> str | None:
    """ ru if russian ; en if english ; None if else"""
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        return 'ru'
    if hex(pf(0)) == '0x4090409':
        return 'en'
    return None

def is_admin() -> bool:
    return bool(ctypes.windll.shell32.IsUserAnAdmin())

def is_process_running(target_proc: str, *, target_path: Path | str | None = None) -> bool:
    if target_path is not None:
        for proc in psutil.process_iter(['exe']):
            if proc.name() == target_proc and proc.exe() == str(target_path):
                return True
        return False

    for proc in psutil.process_iter(['name']):
        if proc.name() == target_proc:
            return True
    return False

def get_proc_list() -> list[str]:
    return [proc.name() for proc in psutil.process_iter(['name'])]

def activate(target_title: str = '', *, hwnd: int | None = None, pid: int | None = None, path: Path | str | None = None) -> None:
    if path:
        pid: int = get_pid_by_path(path)
    if pid:
        hwnd: int = get_hwnds_by_pid(pid)[0]
    if hwnd:
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

            # Сделать активным
        win32gui.SetForegroundWindow(hwnd)
        return

    window: gw.Win32Window = gw.getWindowsWithTitle(target_title)[0]
    window.restore()
    window.activate()

def get_hwnds_by_pid(pid: int) -> list[int]:
    hwnds: list[int] = []

    def callback(hwnd, _):
        if not win32gui.IsWindowVisible(hwnd):
            return
        _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
        if window_pid == pid:
            hwnds.append(hwnd)

    win32gui.EnumWindows(callback, None)
    
    if not hwnds:
        raise ProcessNotFoundError(f'No hwnd found ({pid=})')
    return hwnds

def get_pid_by_path(target_path: Path | str) -> int:
    for proc in psutil.process_iter(['exe']):
        try:
            if proc.exe() == str(target_path):
                return proc.pid
        except psutil.AccessDenied:
            continue
    raise ProcessNotFoundError(f'open process with path {target_path} not found')
