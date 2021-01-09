print('----------------------------------------------------------')
print('| This  Project done by using TWEEPY in python           |')
print('| FOR ANY ISSUES IN THIS PROJECT PLEASE RAISE AN ERROR   |')
print('----------------------------------------------------------')

import tweepy
import time

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
    time.sleep(100)
  
authentication = tweepy.OAuthHandler(consumer_key,consumer_secret)

authentication.set_access_token(access_token,access_token_secret)

api =tewwpy.API(authentication)

public_tweets =api.home-timeline()

print("This your home page Feed")
# This for prints your home page feed

for t in public_tweets:

  print(t.text)

print("Information about the user")  

print(api.me()) 

'''
    you also do like this
    
    user = api.me()
    print(user.name)
    print(user.screen_name)
    print(user.follwers_count)........
'''

# follow back you follower
for f in limit_handler(tweepy.Cursor((api.follwers).items()):
  
  # This if codition checks for a particular user in your follwers and follow them back
  
  if follower.name == "GIVE YOUR FOLLWER NAME":
    follower.follow()
    break
  # This if codition checks for a user in your follwers and follows them back
  
  if follower.name != "":
    follower.follow()
    
  # This if codition checks for a particular user followers count in your follwers and follow them back
  
  if follower.followers_count() > 10000:
    follower.follow()
    

search_element = "YOUR KEYWORD IN THE POST"  

No.ofTweets = 10 # How many tweets you want loop over

for t in teepy.Cursor(tweepy.Cursor(api.search , search_element).items(No.ofTweets)):
  try:
    tweet.favorite()   # give a like
    tweet.retweet()    # Retweet the tweet  
  except tweepy.Tweepy.Error as er:
    continue
    # or print(e.reason)
  except stopIteration:
    break
  
  
