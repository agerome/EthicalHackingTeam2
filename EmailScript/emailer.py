import yagmail
import datetime

# first is "from" arg; using a dictionary you can give an alias as value
#yag=yagmail.SMTP({fromreal:'fakealias'}, 'password') 
#could add a .yagmail file to keep this hidden for security sake
yag = yagmail.SMTP()

#load email from HTML file
'''TODO:
make sure email picture is from the user email fb acct.
make sure that the links to the user email gets inserted/changed ($EMAIL -> "fake" email added to account)
make sure user name is correct ($USER -> fb profile name)
update timestamp to current time before sending 
move subject line to a new file maybe?
'''
with open('email_list.txt', 'r') as emails:
    #give the targeted email addresses a nice 'ol slap
    email_list = emails.read().splitlines()

    print("Phishing emails sent to:")
    for email in email_list:
        with open('sample_email.html', 'r') as f:
            data = f.read().replace('\n', '')
            data = data.replace('$EMAIL', 'obviously.a.fake.email@gmail.com')
            data = data.replace('$USEREMAIL', email)
            data = data.replace(' $USER', ' Name')

            formattedDate = datetime.date.strftime(datetime.datetime.utcnow(), '%A, %B %d, %Y at %H:%M (UTC)')
            data = data.replace('$DATE', formattedDate)

            contents = [data]
            subject = 'New email added to your Facebook account'
            yag.send(email, subject, contents)

        print('\t' + email)
