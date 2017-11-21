import mechanize
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
# browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
browser.set_handle_refresh(False)

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
        # print yes.get_data()

        i = 0
        for f in self.browser.forms():
            print(i)
            print(f)

            ++i




        self.browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0


        self.browser.form["email"] = "alexbui3415@yahoo.com"
        self.browser.form['password'] = "Thongthao123"
        response = self.browser.submit()
        print (response.geturl())
        # print (response.get_data())

if __name__ == '__main__':
#     main()
    objName = yes()
    objName.main()
