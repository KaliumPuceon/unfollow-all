#! /usr/bin/python3

"""helo"""
import json
import pytumblr
import keys

# Authenticate via OAuth

client = pytumblr.TumblrRestClient(
    keys.consumer_key,
    keys.consumer_secret,
    keys.oauth_token,
    keys.oauth_secret,
)

# Make the request

following = client.following(limit=2000)
followers = client.followers("andmaybegayer.tumblr.com",limit=200)

blogs = following["blogs"]
users = followers["users"]

print(len(blogs))
print(len(users))

unames = []
bnames = []

for user in users:
    unames.append(user["name"])
    bnames.append(user["url"])

print(blogs)
print()
print(unames)
print()
print(bnames)
