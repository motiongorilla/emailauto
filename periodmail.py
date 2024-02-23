import yagmail
import os
import time
from datetime import datetime

sender = "nize.afonya@gmail.com"
receiver = "gorillastyle.studio@gmail.com"
password = os.environ['PASSWORD']

subject = "Periodic email testing."


while True:
    now = datetime.now()
    message = f"""
    This is one of the periodic emails that has been sent at a specific time.
    Sent by python yagmail.
    Time sent:{now}
    """
    print(now.minute)
    if now.minute == 53:
        mail_protocol = yagmail.SMTP(user=sender, password=password)
        mail_protocol.send(to=receiver, subject=subject, contents=message)
        print("Email sent!")
    time.sleep(60)
