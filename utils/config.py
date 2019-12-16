from utils.secrets import tinder_token

host = 'https://api.gotinder.com'
headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    'content-type': 'application/json',
    'User-agent': 'Tinder/7.5.3 (iPohone; iOS 10.3.2; Scale/2.00)',
    'X-Auth-Token': tinder_token,
}
FIRST_MESSAGE = "Hello"

if __name__ == '__main__':
    pass
