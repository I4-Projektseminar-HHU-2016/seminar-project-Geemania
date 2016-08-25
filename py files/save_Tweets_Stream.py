 # -*- coding: utf-8 -*-
import tweepy
import unicodecsv as csv
from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def start_stream():
        api = tweepy.streaming.Stream(auth, TwitterStreamListener(), timeout=60, compression=True, wait_on_rate_limit=True)
        api.filter(follow = None, track = ['#Warcraft', '#Legion', '#WorldOfWarcraft'])
        return
                

class TwitterStreamListener(tweepy.StreamListener):
        
        tweet_count = 0
    
        def on_status(self, tweet):
                if (not tweet.retweeted) and ('RT @' not in tweet.text):
                        tweet.text = tweet.text.replace('|', ' ')
                        tweet.text = tweet.text.replace('\n', ' ')

                        TwitterStreamListener.tweet_count += 1
                        
                        with open('result.csv', 'ab') as resultFile:
                                writer = csv.writer(resultFile,
                                                delimiter=";",
                                                lineterminator="\r\n",
                                                encoding='utf-8')
                                if tweet.place:
                                        writer.writerow([tweet.id_str, tweet.created_at, tweet.text, tweet.lang, tweet.place.bounding_box.coordinates])
                                else:
                                        writer.writerow([tweet.id_str, tweet.created_at, tweet.text, tweet.lang, 'NaN'])
                        print (TwitterStreamListener.tweet_count)
                return

        def on_error(self, status_code):
                print ('Error: ' +repr(status_code) +'restarting...')
                lambda e:self.start_stream()
                return

        def on_timeout(self):
                print ("Timeout... restarting...")
                lambda e:self.start_stream()
                return True

        def on_limit(self, track):
                print ("Limit reached... restarting...")
                lambda e:self.start_stream()
                return


if __name__ == "__main__":
        start_stream()

        
