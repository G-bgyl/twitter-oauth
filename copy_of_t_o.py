import json
from requests_oauthlib import OAuth1Session
import secret

client_key = secret.API_Key
client_secret = secret.API_Secret

resource_owner_key = secret.ACCESS_KEY
resource_owner_secret = secret.ACCESS_SECRET

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
text = r.text
dict = json.loads(text)
for each in  dict['statuses']:
    user = each['user']['name']
    txt = each['text']
    print('----------------------------')
    print (user)
    print (txt)