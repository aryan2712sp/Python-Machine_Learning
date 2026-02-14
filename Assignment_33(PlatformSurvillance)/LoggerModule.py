import os
from datetime import datetime

def CreateLogFile(log_dir):
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(log_dir, f"PlatformLog_{timestamp}.log")

    return filename

def WriteLog(log_file, data):
    try:
        with open(log_file, "a") as f:
            f.write(data + "\n")
    except Exception as e:
        pass
