#! /usr/bin/python3
# pylint: disable=C0103

"""
RUN THIS TO KILL YOUR BLOG IMMEDIATELY
"""

import pytumblr
import keys

# Authenticate via OAuth

client = pytumblr.TumblrRestClient( #fetch keys from keys.py because Git
    keys.consumer_key,
    keys.consumer_secret,
    keys.oauth_token,
    keys.oauth_secret,
)

# Make the request

print("Fetching number of blogs")
numFollowing = client.following()["total_blogs"]
numFollowers = client.followers(keys.blogurl)["total_users"]
print("Blogs counted\n")


followersUsers = [] #list of following blogs by URL
followersUrls = [] #list of users who own following blogs

print("Fetching all "+str(numFollowers)+" followers")

for k in range(0, round(numFollowers/20)):
    block = client.followers(keys.blogurl, offset=20*k) #fetch block of followers
    users = block["users"]
    for user in users:
        followersUrls.append(user["url"])
        followersUsers.append(user["name"])

    print(str(20*k)+" of "+str(numFollowers)+" fetched")

print("Followers fetched\n")


followingUrls = [] #list of followed blogs by URL
followingUsers = [] #list of users who own followed blogs

print("Fetching all "+str(numFollowing)+" followed blogs")
for k in range(0, round(numFollowing/20)):
    block = client.following(offset=20*k) #fetch block of followed blogs
    blogs = block["blogs"]
    for blog in blogs:
        followingUrls.append(blog["url"])
        followingUsers.append(blog["name"])

    print(str(20*k)+" of "+str(numFollowing)+" fetched")

print("Followed blogs fetched\n")

# If a you are following a user and they follow you, keep them, I guess

unfollowCount = 0
unfollowList = []

print("Filtering out mutuals")
for user, url in zip(followingUsers, followingUrls): #tuple iterable of followed blogs
    if not ((user in followersUsers) or (url in followersUrls)):
        print("unfollowing of "+user+" running "+url+" recommended")
        unfollowList.append(url)
        unfollowCount += 1
print("Filtering done\n")

confirm = input("Are you sure you want to unfollow "+str(unfollowCount)+" blogs? Type yes to continue:\n") #I take no responsibility for wholly borking up your entire blog

if confirm == "yes":

    for url in unfollowList: #unfollow everyone for real
        print("Unfollowing "+url)
        client.unfollowList(url)

else:
    print("Alright, cool")
