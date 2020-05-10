# -*- coding: utf-8 -*-

# List of the users you don't want to follow
BLACKLIST_FILE = "blacklist.txt"  

# List of users you don't want to unfollow
WHITELIST_FILE = "whitelist.txt"  

# Contains random comments posted by the bot
COMMENTS_FILE = "comments.txt"  

# Users IDs of friends
FRIENDS_FILE = "friends.txt"  

# Captions to put under the photos
PHOTO_CAPTIONS_FILE = "photo_captions.txt" 

# The file containing hashtags you want to track: the bot will like and comment
# photos and follow users using the hashtags in this file
HASHTAGS_FILE = "hashtag_database.txt"

# Same as HASHTAGS_FILE, but with users. The bot will follow those users'
# followers and like their posts
USERS_FILE = "username_database.txt"

# File containing all the photos already posted from the PICS_PATH directory
POSTED_PICS_FILE = "pics.txt"

# The path of the directory containing the photos the bot will upload
# NOTE: Being a directory, it must end with '/'
PICS_PATH = "/Users/rafael/BOT/pics/"

# The bot will comment each photo it posts with the hashtags in PICS_HASHTAGS
# Each string but the last must end with a space
# NOTE: Instagram allows only for a maximum of 30 hashtags per post.
PICS_HASHTAGS = (
    "#hashtag1 #hashtag2 #hashtag3 #hashtag4 " "#hashtag5 #hashtag6 #hashtag7"
)

# The string to insert under the random caption. The bot will construct each
# photo caption like the following ->
# [random caption taken from PHOTO_CAPTIONS]
# FOLLOW_MESSAGE
FOLLOW_MESSAGE = "Follow us ( @TopTechTool ) for the most helpful and cheap day to day tech devices :) "


# NOTE: Because the bot follows a bunch of people through job7 (follow
# people by a random hashtag in HASHTAGS_FILE), I recommend setting
# NUMBER_OF_FOLLOWERS_TO_FOLLOW between 15 and 30, and
# NUMBER_OF_NON_FOLLOWERS_TO_UNFOLLOW between 50 and 60. Following and
# unfollowing many people in the same day can cause a temporary
# "follow ban" by Instagram: basically you can't follow or unfollow
# anybody for 24 hours.

# Specifies the number of people to follow each time the function
# bot.follow_followers gets executed. By default, this function gets
# executed by the bot every 2 days at 11:00.
NUMBER_OF_FOLLOWERS_TO_FOLLOW = 15

# Specifies the number of people to unfollow each time the function
# bot.unfollow_non_followers gets executed. By default, this function
# gets executed every day at 08:00.
NUMBER_OF_NON_FOLLOWERS_TO_UNFOLLOW = 50


# This is to enable a filter that will decide whether like, comment, follow, unfollow a user.
FILTER_PRIVATE_USERS=True

FILTER_USERS_WITHOUT_PROFILE_PHOTO=False

# *********************************************************
# Below are all the settings that can be used on the Bot:
# 
#         whitelist_file="whitelist.txt",
#         blacklist_file="blacklist.txt",
#         comments_file="comments.txt",
#         followed_file="followed.txt",
#         unfollowed_file="unfollowed.txt",
#         skipped_file="skipped.txt",
#         friends_file="friends.txt",
#         base_path="",
#         proxy=None,
#         max_likes_per_day=1000,
#         max_unlikes_per_day=1000,
#         max_follows_per_day=350,
#         max_unfollows_per_day=350,
#         max_comments_per_day=100,
#         max_blocks_per_day=100,
#         max_unblocks_per_day=100,
#         max_likes_to_like=100,
#         min_likes_to_like=20,
#         max_messages_per_day=300,
#         filter_users=True,
#         filter_private_users=True,
#         filter_users_without_profile_photo=False,
#         filter_previously_followed=False,
#         filter_business_accounts=False,
#         filter_verified_accounts=False,
#         max_followers_to_follow=5000,
#         min_followers_to_follow=10,
#         max_following_to_follow=2000,
#         min_following_to_follow=10,
#         max_followers_to_following_ratio=15,
#         max_following_to_followers_ratio=15,
#         min_media_count_to_follow=3,
#         max_following_to_block=2000,
#         like_delay=10,
#         unlike_delay=10,
#         follow_delay=30,
#         unfollow_delay=30,
#         comment_delay=60,
#         block_delay=30,
#         unblock_delay=30,
#         message_delay=60,
#         stop_words=("shop", "store", "free"),
#         blacklist_hashtags=["#shop", "#store", "#free"],
#         blocked_actions_protection=True,
#         blocked_actions_sleep=False,
#         blocked_actions_sleep_delay=300,
#         verbosity=True,
#         device=None,
#         save_logfile=True,
#         log_filename=None,
#         log_follow_unfollow=True