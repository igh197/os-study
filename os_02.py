import os
import psutil

current_pid = os.getpid()
all_processes = psutil.process_iter()

for process in all_processes:
    try:
        process_pid = process.pid
        if process_pid == current_pid:
            print("현재 파이썬 프로그램의 프로세스 명:", process_pid)
            break
    except psutil.Error:
        pass
