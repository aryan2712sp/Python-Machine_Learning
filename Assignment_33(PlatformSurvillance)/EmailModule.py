import smtplib
from email.message import EmailMessage

def SendEmail(sender, password, receiver, log_file, summary):
    try:
        msg = EmailMessage()
        msg['Subject'] = "Platform Surveillance Report"
        msg['From'] = sender
        msg['To'] = receiver

        msg.set_content(summary)

        with open(log_file, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data,
                               maintype='application',
                               subtype='octet-stream',
                               filename=log_file)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

    except Exception:
        pass
