import twitter
import requests

#api = 

def get_tweets(country_name):
	results = api.GetSearch(
    raw_query="q="+ country_name.replace(' ', '%20') + "%20&result_type=recent&since=2014-07-19&count=100")
	return results

url = 'http://localhost:8000/api/twitter/'

us_tweets = get_tweets("Mexico")
tweet = { 'tweet_id': us_tweets[0].id, 'text': us_tweets[0].text}
res = requests.post(url, data=tweet)
print(res.text)

