import mechanize
import MySQLdb
import paramiko
from sshtunnel import SSHTunnelForwarder
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
browser.set_handle_refresh(False)

#NOTE: you must have the ssh key in the same directory as try.py

#ssh tunneling = https://stackoverflow.com/questions/44128175/python-used-sshtunnel-cant-connect-to-mysql


#-----------------------------------------------
#SSHTUNNEL
with SSHTunnelForwarder(
    ("13.57.61.57", 22), #<--- iffy
    # ('localhost', 22),
    ssh_username = "ubuntu",
    ssh_pkey = "ethicalhacking2.pem",
    remote_bind_address = ('127.0.0.1', 3306) #<--- iffy
    # remote_bind_address = ('13.57.61.57', 3306)
) as tunnel:
        connection = MySQLdb.connect(user = "root",
        password = "ethicalhacking")


# db = MySQLdb.connect (host = "13.57.61.57",
#                          user = "root",
#                         passwd = "ethicalhacking",
#                         db = "ethicalhackingteam2")
#
# cur = db.cursor()
# cur.execute("SELECT * FROM ethicalhackingteam2")
# for r in cur.fetchall():
#     print r[0], " ", r[1]

#--------------------------------------------
# #PARAMIKO - feel free to try it
# k = paramiko.RSAKey.from_private_key_file("ethicalhacking2.pem")
# c = paramiko.SSHClient()
# c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# print("connecting")
# c.connect(hostname = "13.57.61.57", username = "ubuntu", pkey = k)
# print("connected")
# print(c.get_transport().is_active())
#
#
# # commands = ["ls", "cd /var/www/html"]
# commands = ["mysql --user=root --password=ethicalhacking" , "use ethicalhackingteam2", "select * from ethicalhackingteam2  "]
#
# for com in commands:
#     print "Executing {}".format(com)
#     print(c.get_transport().is_active())
#
#     stdin, stdout, stderr = c.exec_command(com)
#     stdin.write("use ethicalhackingteam2")
#     print stdout.read()
#     print("errors")
#     print stderr.read()
#--------------------------------------------------

#LIST OF SUCCESSFUL URLS















class yes:

    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)

    def main(self):
        # url = 'http://www.facebook.com/login.php' #need to use nr = 0 (email, pass)

        # url = 'https://www.instructables.com/account/login/' #need to use nr = 1 (u, p)

        # url = 'https://members.zipcar.com/register/' #need to use nr = 0 (user_name, password)

        # url = 'https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F' #need to use nr = 0 (userid, pass)

        # url = 'https://www.tumblr.com/login' #need to use nr = 0 (user[email], user[password])

        # url = 'https://www.netflix.com/login' #need to use nr = 0 (email, password)




        yes = self.browser.open(url)
        # i = 0
        # for f in self.browser.forms():
        #     print(i)
        #     print(f)
        #
        #     ++i




        self.browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
        self.browser.form["email"] = "alexbui3415@yahoo.com"
        self.browser.form['password'] = "Thongthao123"
        response = self.browser.submit()
        print (response.geturl())

        #lets compare urls
        #IF RESPONSE != LIST OF URL, THEN IT'S A FAIL


if __name__ == '__main__':
    main()
