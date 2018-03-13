import tweepy
import time
import os
consumer_key = "GnaTE6bMiJMIwuf8Mptj8hY6a"
consumer_secret ="qvCY9W40e9vRFru955CXj0Rt8YSBP5RjVtPntS8kQ5ONZ2usba"
access_token = "968331154062544896-SXbKabU8fXerarLBTE14svHP27K7SN6"
access_token_secret = "N737TQwbarQDARnAvCBoyBPab1pECFEs9Eo3hmEC0v2tS" 
  

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
  
api = tweepy.API(auth)
a=0
b=1
while a<=2:
      img="/home/cs2017a126/Desktop/img"+str(b)+".jpg"
      cmd="fswebcam -f 3 --fps 20 -r 800*600" +img
      os.system(cmd)
      print("pic taken")
      api.update_with_media(img, status="Nice one")
      print("wait for 5 seconds for selfiiiii")
      time.sleep(5)
      a+=1
      b+=1
      print("success")
