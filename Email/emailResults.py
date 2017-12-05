import yagmail
import sys
'''
USAGE:
python emailer.py <email-addr> <report.txt>
'''

#yag = yagmail.SMTP('''FILL THIS OUT WITH YOUR USER/PASS FOR YOUR EMAIL SERVICE''')
#yag = yagmail.SMTP('<USER>', '<PASS>')
yag = yagmail.SMTP('ehteam2@gmail.com', 'ethical789')

#load email from HTML file
'''TODO:
make sure email picture is from the user email fb acct.
make sure user name is correct ($USER -> fb profile name)
move subject line to a new file maybe?
'''
email = sys.argv[1]
with open(sys.argv[2], 'r') as f:
    data = f.read()
    contents = [data]
    subject = 'Phishing Results'
    yag.send(email, subject, contents)

