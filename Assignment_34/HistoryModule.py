import os
from datetime import datetime

HISTORY_FILE = "BackupHistory.txt"

def UpdateHistory(zipname, filecount):
    try:
        size = os.path.getsize(zipname)

        with open(HISTORY_FILE, "a") as f:
            f.write(f"{datetime.now()} | Files: {filecount} | Size: {size} bytes | {zipname}\n")
    except:
        pass

def DisplayHistory(logfile):
    try:
        with open(HISTORY_FILE, "r") as f:
            data = f.read()

        with open(logfile, "a") as log:
            log.write("\nBackup History:\n")
            log.write(data)

    except Exception as e:
        with open(logfile, "a") as log:
            log.write(f"History Error: {str(e)}\n")
