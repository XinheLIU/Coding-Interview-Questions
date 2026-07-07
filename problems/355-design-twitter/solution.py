class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.order = 0
        self.user_tweets = {}
        self.friends = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.order += 1
        if userId in self.user_tweets:
            self.user_tweets[userId].append((self.order, tweetId))
        else:
            self.user_tweets[userId] = [(self.order, tweetId)]
            

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        rt = []
        if userId in self.user_tweets:
            rt = self.user_tweets[userId][-10:]
        
        if userId in self.friends:
            for friend in self.friends[userId]:
                if friend in self.user_tweets:
                    rt.extend(self.user_tweets[friend][-10:])
        rt.sort(key = lambda x: x[0])
        return [tweet[1] for tweet in rt[-10:][::-1]]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        if followerId not in self.friends:
            self.friends[followerId] = set()
        self.friends[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        if followerId not in self.friends:
            return
        if followeeId in self.friends[followerId]:
            self.friends[followerId].remove(followeeId)        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

'''

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.order = 0
        self.user_tweets = collections.defaultdict(list)
        self.friends = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.order += 1        
        self.user_tweets[userId].append((self.order, tweetId))
            

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        rt = []
        rt = self.user_tweets[userId][-10:]
        
        if userId in self.friends:
            for friend in self.friends[userId]:
                if friend in self.user_tweets:
                    rt.extend(self.user_tweets[friend][-10:])
        rt.sort(key = lambda x: x[0])
        return [tweet[1] for tweet in rt[-10:][::-1]]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        if followerId not in self.friends:
            self.friends[followerId] = set()
        self.friends[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        if followerId not in self.friends:
            return
        if followeeId in self.friends[followerId]:
            self.friends[followerId].remove(followeeId)
     '''    