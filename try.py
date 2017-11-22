#sample input line
#python try.py usename password

import mechanize
import sys

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
browser.set_handle_refresh(False)

def main():

    try_url = ["http://www.facebook.com/login.php",
                "https://members.zipcar.com/register/",
                "https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F",
                "https://www.tumblr.com/login",
                "https://www.netflix.com/login"
                ]

    correct_url = ["https://www.facebook.com/",
                    "https://members.zipcar.com/members/account",
                    "https://www.ebay.com/",
                    "https://www.tumblr.com/dashboard",
                    "https://www.netflix.com/browse"]

    # fb #need to use nr = 0 (email, pass)

    # zipcar #need to use nr = 0 (user_name, password)

    # ebay #need to use nr = 0 (userid, pass)

    # tumblr #need to use nr = 0 (user[email], user[password])

    # netflix #need to use nr = 0 (email, password)

    username = sys.argv[1]
    password = sys.argv[2]

    response_url_collection = list()
    for i in try_url:
        browser.open(i)
        browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
        if "facebook" in i:
            browser.form['email'] = username
            browser.form['pass'] = password
            response = browser.submit()
        if "zipcar" in i:
            browser.form['user_name'] = username
            browser.form['password'] = password
            response = browser.submit()
        if "ebay" in i:
            browser.form['userid'] = username
            browser.form['pass'] = password
            response = browser.submit()
        if "tumblr" in i :
            browser.form['user[email]'] = username
            browser.form['user[password]'] = password
            response = browser.submit()
        if "netflix" in i:
            browser.form['email'] = username
            browser.form['password'] = password
            response = browser.submit()

        response_url = response.geturl()
        response_url_collection.append(response_url)
    print ("resulting urls ", response_url_collection)

#compare the urls
    match_success_urls = list()
    for j in response_url_collection:
        for h in correct_url:
            if j == h:
                match_success_urls.append(j)

    print ("sites we were able to access : " , match_success_urls)



if __name__ == '__main__':
    main()
