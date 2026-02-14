import os
import zipfile
from datetime import datetime

def PerformBackup(source, exclude_ext, logfile):
    files_copied = []
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = f"Backup_{timestamp}.zip"

    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for foldername, subfolders, filenames in os.walk(source):
                for file in filenames:
                    ext = os.path.splitext(file)[1]

                    if ext in exclude_ext:
                        continue

                    filepath = os.path.join(foldername, file)
                    zipf.write(filepath)
                    files_copied.append(filepath)

        return zip_name, files_copied

    except Exception as e:
        with open(logfile, "a") as f:
            f.write(f"Error during backup: {str(e)}\n")
        return None, []
    
def RestoreBackup(zip_name, destination, logfile):
    try:
        with zipfile.ZipFile(zip_name, 'r') as zipf:
            zipf.extractall(destination)
        return True
    except Exception as e:
        with open(logfile, "a") as f:
            f.write(f"Restore Error: {str(e)}\n")
        return False

