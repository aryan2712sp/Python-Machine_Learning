import sys
import time
from LoggerModule import *
from ProcessMonitor import *
from EmailModule import *

def ValidateInputs():
    if len(sys.argv) != 4:
        return False
    return True

def CreateSummary(processes):
    total = len(processes)

    top_cpu = sorted(processes, key=lambda x: x["CPU"], reverse=True)[:5]
    top_mem = sorted(processes, key=lambda x: x["RSS"], reverse=True)[:5]
    top_threads = sorted(processes, key=lambda x: x["Threads"], reverse=True)[:5]
    top_files = sorted(processes, key=lambda x: (x["OpenFiles"] if isinstance(x["OpenFiles"], int) else 0), reverse=True)[:5]

    summary = f"""
Total Processes : {total}

Top CPU Processes :
{[p['Name'] for p in top_cpu]}

Top Memory Processes :
{[p['Name'] for p in top_mem]}

Top Thread Processes :
{[p['Name'] for p in top_threads]}

Top Open File Processes :
{[p['Name'] for p in top_files]}
"""
    return summary

def Main():
    if not ValidateInputs():
        return

    log_dir = sys.argv[1]
    receiver = sys.argv[2]
    interval = int(sys.argv[3])

    sender = "your_email@gmail.com"
    password = "your_app_password"

    log_file = CreateLogFile(log_dir)

    while True:
        processes = GetProcessInfo()

        for p in processes:
            log_data = f"""
Timestamp : {p['Timestamp']}
Process Name : {p['Name']}
PID : {p['PID']}
CPU % : {p['CPU']}
Memory RSS : {p['RSS']}
Threads : {p['Threads']}
Open Files : {p['OpenFiles']}
----------------------------------------
"""
            WriteLog(log_file, log_data)

        summary = CreateSummary(processes)
        SendEmail(sender, password, receiver, log_file, summary)

        time.sleep(interval * 60)

if __name__ == "__main__":
    Main()
