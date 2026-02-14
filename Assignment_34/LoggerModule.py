import os
from datetime import datetime

def CreateLogFolder():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

def CreateLogFile():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Logs/BackupLog_{timestamp}.log"
    return filename

def WriteLog(logfile, data):
    try:
        with open(logfile, "a") as f:
            f.write(data + "\n")
    except Exception:
        pass
