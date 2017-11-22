"""
Jae Lee & Cameron Moeller
sample input line
python try.py usename password
"""

from enum import Enum
import mechanize
import sys
import json


# enum for the sites
class Site(str, Enum):
    Facebook = "facebook"
    Zipcar = "zipcar"
    Ebay = "ebay"
    Tumblr = "tumblr"
    Netflix = "netflix"

# Dictionary of sites that we can attempt to authenticate
urls = {
    Site.Facebook: {
        "attempt": "http://www.facebook.com/login.php",
        "correct": "https://www.facebook.com/?sk=welcome"
    },
    Site.Zipcar: {
        "attempt": "https://members.zipcar.com/register/",
        "correct": "https://members.zipcar.com/members/account"
    },
    Site.Ebay: {
        "attempt": "https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F",
        "correct": "https://www.ebay.com/"
    },
    Site.Tumblr: {
        "attempt": "https://www.tumblr.com/login",
        "correct": "https://www.tumblr.com/dashboard"
    },
    Site.Netflix: {
        "attempt": "https://www.netflix.com/login",
        "correct": "https://www.netflix.com/browse"
    }
}

# Browser settings
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
browser.set_handle_refresh(False)


def main():

    # fb #need to use nr = 0 (email, pass)
    # zipcar #need to use nr = 0 (user_name, password)
    # ebay #need to use nr = 0 (userid, pass)
    # tumblr #need to use nr = 0 (user[email], user[password])
    # netflix #need to use nr = 0 (email, password)

    try:
        # Grab command line arguments, exit if it is invalid
        site = sys.argv[1]
        username = sys.argv[2]
        password = sys.argv[3]

        # Authenticate to site
        result = attempt_authentication(site=site, username=username, password=password)
        print(json.dumps(result))

    except Exception as e:
        # Exit program and print an error
        error = {"error": e.args}
        print(json.dumps(error))


def attempt_authentication(site, username, password):
    # grab fields
    attempt = urls[site]["attempt"]
    correct = urls[site]["correct"]
    browser.open(attempt)
    browser.select_form(nr=0)

    # try the credentials on different sites
    if site == Site.Facebook:
        browser.form['email'] = username
        browser.form['pass'] = password
    if site == Site.Zipcar:
        browser.form['user_name'] = username
        browser.form['password'] = password
    if site == Site.Ebay:
        browser.form['userid'] = username
        browser.form['pass'] = password
    if site == Site.Tumblr:
        browser.form['user[email]'] = username
        browser.form['user[password]'] = password
    if site == Site.Netflix:
        browser.form['email'] = username
        browser.form['password'] = password

    # Submit the request and get the response
    response = browser.submit()
    response_url = response.geturl()

    # Check if the authentication was successful
    return {site: True} if response_url == correct else {site: False}

if __name__ == '__main__':
    main()
