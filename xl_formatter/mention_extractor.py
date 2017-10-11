import re
from .models import TwitterData, TwitterMention, InstagramData, InstagramMention

def extract_mentions():

    for tweet in TwitterData.objects.all():

        author = tweet.author
        content = tweet.contents
        tweet_id = tweet.id

        try:
            rt_string = content.split(' ')
        except:
            print(tweet.id, content, 'There was an Exception')
            continue

        isDirected = False
        isMixed = False
        isRetweet = False

        if rt_string[0] == 'RT':
            isMixed = True
            isRetweet = True
        else:
            isDirected = True

        mentions = re.findall("@([a-z0-9_]+)", content, re.I)

        if isRetweet:
            try:
                mention = mentions[0]
                twitter_mention = TwitterMention(
                    author=author,
                    twitter_data_id=tweet_id,
                    is_Direct=isDirected,
                    is_Mixed=isMixed,
                    mention=mention.lower()
                )
                twitter_mention.save()
            except:
                print('No mentions ', mentions)
                continue
        else:
            for mention in mentions:
                try:
                    mention = mention.lower()
                except:
                    print('Mention is None')

                twitter_mention = TwitterMention(
                    author=author,
                    twitter_data_id=tweet_id,
                    is_Direct=isDirected,
                    is_Mixed=isMixed,
                    mention=mention
                )
                twitter_mention.save()

    for tweet in InstagramData.objects.all():

        author = tweet.author
        content = tweet.contents
        tweet_id = tweet.id

        try:
            rt_string = content.split(' ')
        except:
            print(tweet.id, content, 'There was an Exception')
            continue

        isDirected = False
        isMixed = False
        isRetweet = False

        if rt_string[0] == 'RT':
            isMixed = True
            isRetweet = True
        else:
            isDirected = True

        mentions = re.findall("@([a-z0-9_]+)", content, re.I)

        if isRetweet:
            try:
                mention = mentions[0]
                twitter_mention = InstagramMention(
                    author=author,
                    instagram_data_id=tweet_id,
                    is_Direct=isDirected,
                    is_Mixed=isMixed,
                    mention=mention.lower()
                )
                twitter_mention.save()
            except:
                print('No mentions ', mentions)
                continue
        else:
            for mention in mentions:
                try:
                    mention = mention.lower()
                except:
                    print('Mention is None')

                twitter_mention = InstagramMention(
                    author=author,
                    instagram_data_id=tweet_id,
                    is_Direct=isDirected,
                    is_Mixed=isMixed,
                    mention=mention
                )
                twitter_mention.save()