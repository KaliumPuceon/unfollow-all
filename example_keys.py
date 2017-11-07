"""A keyfile for safely loading keys without having to put them in the main repo"""

# INSTRUCTIONS
# go to https://www.tumblr.com/oauth/apps and register an application

# go to https://api.tumblr.com/console/ give the app access and click the "Show
# Keys" button at the top of the screen. Copy those keys into the right strings
# below. They're in the right order and everything at the time of writing.

# Fill in your blog name. This only works if you only have one blog, I
# Still need to add multi-blog-support so hang on if that's your deal because
# Gods this could go badly if you try something clever with it. If you want to
# get on that before I do feel free.

# Lastly, save the file, close it, and rename it to keys.py

consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
oauth_token = "oauth_token"
oauth_secret = "oauth_secret"
blogurl = "yablognamehere.tumblr.com"
