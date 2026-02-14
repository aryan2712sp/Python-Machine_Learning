import sys
from LoggerModule import *
from BackupModule import *
from EmailModule import *
from HistoryModule import *

def ValidatePath(path):
    return os.path.exists(path)

def Main():
    CreateLogFolder()
    logfile = CreateLogFile()

    default_exclude = ['.tmp', '.log', '.exe']

    if "--restore" in sys.argv:
        zipname = sys.argv[2]
        destination = sys.argv[3]
        RestoreBackup(zipname, destination, logfile)
        return

    if "--history" in sys.argv:
        DisplayHistory(logfile)
        return

    if len(sys.argv) < 3:
        WriteLog(logfile, "Invalid arguments")
        return

    source = sys.argv[1]
    receiver = sys.argv[2]

    if not ValidatePath(source):
        WriteLog(logfile, "Invalid source path")
        return

    zipname, files = PerformBackup(source, default_exclude, logfile)

    if zipname:
        WriteLog(logfile, f"Backup Start Time: {zipname}")
        WriteLog(logfile, f"Files Copied: {len(files)}")
        WriteLog(logfile, f"Zip File: {zipname}")

        UpdateHistory(zipname, len(files))

        sender = "your_email@gmail.com"
        password = "your_app_password"

        SendEmail(sender, password, receiver, logfile, zipname)

if __name__ == "__main__":
    Main()
