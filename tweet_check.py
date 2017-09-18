from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey="Rf5pDiFPAni0KCMfCsMe6c4Us"
csecret="LtXzxzSSHSsHNVv9gb41EfDLnjVs4rFBK5Ss2pj3Aey0JK172J"
atoken="162992083-lKyCwKLsOw8KWbD8UE6rvnvhsFtwOFrZYSUSC0sZ"
asecret="OAbgxXlpIHwgoiQUxBuzfy6ckp5Cd33iXe0HBSCq2DPd4"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
