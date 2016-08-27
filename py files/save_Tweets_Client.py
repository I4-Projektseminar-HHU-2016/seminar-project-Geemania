import tweepy
import unicodecsv as csv
import codecs

from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# Erstellen einer csv Datei
class TwitterClientCrawler():

    def fetch_and_write(self, *args):
        api = tweepy.API(auth, wait_on_rate_limit=True)

        for tweet in tweepy.Cursor(api.search, q=args).items():
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                tweet.text = tweet.text.replace('|', ' ')
                tweet.text = tweet.text.replace('\n', ' ')
                with open('result.csv', 'ab') as resultFile:
                    writer = csv.writer(resultFile,
                                        delimiter=";",
                                        lineterminator="\n",
                                        encoding='utf-8')
                    if tweet.place and tweet.user.location:
                        writer.writerow([tweet.id_str, tweet.created_at, tweet.text, tweet.lang, tweet.place.bounding_box.coordinates, tweet.user.location])
                    elif ((not tweet.place) and (tweet.user.location)):
                        writer.writerow([tweet.id_str, tweet.created_at, tweet.text, tweet.lang, 'NaN', tweet.user.location])
                    elif ((tweet.place) and (not tweet.user.location)):
                        writer.writerow([tweet.id_str, tweet.created_at, tweet.text, tweet.lang, tweet.place.bounding_box.coordinates, 'NaN'])
                    else:
                        writer.writerow([tweet.id_str, tweet.created_at, tweet.text, tweet.lang, 'NaN', 'NaN'])
                    
        resultFile.close()

if __name__ == "__main__":
    crawler = TwitterClientCrawler()
    crawler.fetch_and_write('#Warcraft', '#Legion')


########################################################################
#                                                                      #
#   Der Quellcode beider Dateien wurde in Zusammenarbeit mit Thorsten  #
#   Brueckner geschrieben                                              #
#                                                                      #
########################################################################
