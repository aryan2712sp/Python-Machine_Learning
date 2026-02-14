import smtplib
from email.message import EmailMessage

def SendEmail(sender, password, receiver, logfile, zipname):
    try:
        msg = EmailMessage()
        msg['Subject'] = "Marvellous Data Shield Backup Completed"
        msg['From'] = sender
        msg['To'] = receiver

        msg.set_content(f"Backup completed successfully.\nZip File: {zipname}")

        with open(logfile, 'rb') as f:
            msg.add_attachment(f.read(),
                               maintype='application',
                               subtype='octet-stream',
                               filename=logfile)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

    except Exception:
        pass
