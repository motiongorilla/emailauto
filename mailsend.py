import yagmail
import os

sender = "nize.afonya@gmail.com"
receiver = "yegor.omelchenko@gmail.com"

subject = "This is the subject"

content = """
Contents of the procedural email!
"""

pw1 = os.environ['PASSWORD']

mail_protocol = yagmail.SMTP(user=sender, password=pw1)
mail_protocol.send(to=receiver, subject=subject, contents=content)
print("Email send!")
