import requests
import argparse
from lxml import html

AMAZON_LOGIN = 'https://www.amazon.com/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&switch_account=';
FACEBOOK_LOGIN = 'https://www.facebook.com/?stype=lo&jlou=AfcpRieG-amy9jCTwZVbL3crYU3IEYBRCAh0zT4snzVlQCNb9crIqiHZpK7pz3aFdvvtyI9NULQE_O0Sby6CaVe2&smuh=54298&lh=Ac_0OCgG5NfOnmKY'
TWITTER_LOGIN = 'https://twitter.com/login/'
YOUTUBE_LOGIN = ''

def generate_payload(login):
	tree = html.fromstring(login.text)
	hidden_inputs = tree.xpath('//form//input[@type="hidden"]')
	print(hidden_inputs)
	payload = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
	payload['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	return payload

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('username', type = str, nargs = 1)
	parser.add_argument('password', type = str, nargs = 1)
	args = parser.parse_args()
	username = args.username
	password = args.password
	
	session = requests.session()
	amazon_session = session.get(AMAZON_LOGIN)
	facebook_session = session.get(FACEBOOK_LOGIN)
	twitter_session = session.get(TWITTER_LOGIN)

	amazon_payload = generate_payload(amazon_session)
	facebook_payload = generate_payload(facebook_session)
	twitter_payload = generate_payload(twitter_session)

	amazon_payload['email'] = username
	amazon_payload['password'] = password

	facebook_payload['email'] = username
	facebook_payload['pass'] = password

	twitter_payload['session[username_or_email]'] = username
	twitter_payload['session[password]'] = password



	amazon_result = session.post(AMAZON_LOGIN, data = amazon_payload, headers = dict(referer = AMAZON_LOGIN))
	facebook_result = session.post(FACEBOOK_LOGIN, data = facebook_payload, headers = dict(referer = FACEBOOK_LOGIN))
	twitter_result = session.post(TWITTER_LOGIN, data = twitter_payload, headers = dict(referer = TWITTER_LOGIN))


	print("Amazon Login result was {} with status code {}".format(amazon_result.ok, amazon_result.status_code))
	print(amazon_result.text)

	print("facebook Login result was {} with status code {}".format(facebook_result.ok, facebook_result.status_code))
	print(facebook_result.text)

	print("twitter Login result was {} with status code {}".format(twitter_result.ok, twitter_result.status_code))
	print(twitter_result.text)

if __name__ == '__main__':
    main()