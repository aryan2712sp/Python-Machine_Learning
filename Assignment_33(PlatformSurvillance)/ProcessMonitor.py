import psutil
from datetime import datetime

def GetProcessInfo():
    process_list = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            info = proc.info
            memory = proc.memory_info()
            threads = proc.num_threads()

            try:
                open_files = len(proc.open_files())
            except:
                open_files = "Access Denied"

            process_list.append({
                "Name": info['name'],
                "PID": info['pid'],
                "CPU": info['cpu_percent'],
                "RSS": memory.rss,
                "VMS": memory.vms,
                "MemoryPercent": proc.memory_percent(),
                "Threads": threads,
                "OpenFiles": open_files,
                "Timestamp": datetime.now()
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return process_list
