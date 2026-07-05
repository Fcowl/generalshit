import psutil

def is_process_running(process:str) -> bool:
    for proc in psutil.process_iter(['name']):
        if proc.name() == process:
            return True
    return False
