import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "GnaTE6bMiJMIwuf8Mptj8hY6a",
    "consumer_secret"     : "qvCY9W40e9vRFru955CXj0Rt8YSBP5RjVtPntS8kQ5ONZ2usba",
    "access_token"        : "968331154062544896-SXbKabU8fXerarLBTE14svHP27K7SN6",
    "access_token_secret" : "N737TQwbarQDARnAvCBoyBPab1pECFEs9Eo3hmEC0v2tS" 
    }

  api = get_api(cfg)
  tweet = "hello samreen!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
