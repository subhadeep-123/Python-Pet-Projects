import smtplib
import ssl
from email.message import EmailMessage
from string import Template
from pathlib import Path
import config

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Dummy Dummy'
email['to'] = 'subhadeep762@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(
    {'name': 'TinTin', 'money': '1, 000, 000'}), 'html')

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.login('dummyemailtest8@gmail.com', config.psswd)
    smtp.send_message(email)
    print('All Good Boss!')
