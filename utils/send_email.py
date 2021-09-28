import smtplib
from email.mime.text import MIMEText


def send_email():
    # 1. Set the email Server
    host = 'smtp.163.com'

    # 2. Set the SSL Port
    port = 465

    # 3. Set the Sender
    sender = ''
    pwd = ''

    # 4. Set the Receiver
    receiver = ''

    # 5. Set the email content
    body = '<h1>You has succeed to check in！</h1><p>111</p>'
    msg = MIMEText(body, 'html')
    msg['subject'] = 'Check in Solution'
    msg['from'] = sender
    msg['to'] = receiver

    # 6.Send the email
    try:
        s = smtplib.SMTP_SSL(host, port)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())
        print("Done.sent email success!")
    except smtplib.SMTPException:
        print("Error.sent email fail~")
