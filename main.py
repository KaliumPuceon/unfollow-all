#! /usr/bin/python3
# pylint: disable=C0103
"""helo"""
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

numFollowing = client.following()["total_blogs"]
numFollowers = client.followers(keys.blogurl)["total_users"]

followersUsers = [] #list of following blogs by URL
followersUrls = [] #list of users who own following blogs

for k in range(0, round(numFollowers/20)):
    block = client.followers(keys.blogurl, offset=20*k)
    users = block["users"]
    for user in users:
        followersUrls.append(user["url"])
        followersUsers.append(user["name"])

followingUrls = [] #list of followed blogs by URL
followingUsers = [] #list of users who own followed blogs

for k in range(0, round(numFollowing/20)):
    block = client.following(offset=20*k)
    blogs = block["blogs"]
    for blog in blogs:
        followingUrls.append(blog["url"])
        followingUsers.append(blog["name"])

# If a you are following a user and they follow you, keep them, I guess

for user, url in zip(followingUsers, followingUrls):
    if not ((user in followersUsers) or (url in followersUrls)):
        print("unfollowing of "+user+" running "+url+" recommended")
