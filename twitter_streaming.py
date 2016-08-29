from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from json import load
from kafka import KafkaProducer

with open('tokens.json') as data_file:
    tokens = load(data_file)

access_token = tokens['access_token']
access_token_secret = tokens['access_token_secret']
consumer_key = tokens['consumer_key']
consumer_secret = tokens['consumer_secret']

producer = KafkaProducer(bootstrap_servers='localhost:9092')


class StdOutListener(StreamListener):

    def on_data(self, data):
        producer.send('twitter-stream', data.encode('utf-8'))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['python', 'data'])
