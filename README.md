# Unfollow All
I got kinda tired of having followed several thousand blogs as a confused teen
so I decided to get rid of them all. Sitting and clicking on "Unfollow" sounded
bad, though, so I did this.

# Stuff you'll need
You need to have
1. A Tumblr, obviously
1. Python 3
1. PyTumblr (Install with pip)
1. A set of Tumblr API keys (Instructions Below)

# Key Setup Instructions
Go [here](https://www.tumblr.com/oauth/apps) and register an application

Go [here,](https://api.tumblr.com/console/) give the app access and click the "Show
Keys" button at the top of the screen. Copy those keys into the right strings
below. They're in the right order and everything at the time of writing.

Fill in your blog name. This only works if you only have one blog, I
Still need to add multi-blog-support so hang on if that's your deal because
Gods this could go badly if you try something clever with it. If you want to
get on that before I do feel free.

Lastly, save the file, close it, and rename it to keys.py

# Limitations
The tumblr API is rate limited to 1000 requests per hour. If you follow/are
followed by more than a few thousand blogs this will not work unless you ask
for them to drop your rate limit.

This also only works if you have one blog. I'll add support for many blogs when
I get round to it but at the moment it only checks for mutuals against a single
blog. DO NOT USE THIS IF YOU HAVE MANY BLOG-EXCLUSIVE MUTUALS. It'll be bad.

If you feel like fixing either of these for me, do a pull request and I'll learn
how those work to accept it.

# TODO
1. Add multi-blog support
1. Add more options (e.g. unfollow all, unfollow those who follow me, etc.)
1. Add memory because if you mess up and need to rerun this it takes an /age/
1. Make into a web service? I'm sure someone wants this.
