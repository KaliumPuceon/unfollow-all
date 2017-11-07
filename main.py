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

followersUsers = []
followersUrls = []

print(client.followers(keys.blogurl))

for k in range(0, round(numFollowers/20)):
    block = client.followers(keys.blogurl, offset=20*k)
    users = block["users"]
    for user in users:
        followersUrls.append(user["url"])
        followersUsers.append(user["name"])

print(followersUrls)
print()
print(followersUsers)
print()

followingUrls = []
followingUsers = []

for k in range(0, round(numFollowing/20)):
    block = client.following(offset=20*k)
    blogs = block["blogs"]
    for blog in blogs:
        followingUrls.append(blog["url"])
        followingUsers.append(blog["name"])

print(followingUrls)
print()
print(followingUsers)
