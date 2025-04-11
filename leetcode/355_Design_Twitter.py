"""
Name: Design Twitter (#355)
URL: https://leetcode.com/problems/design-twitter/

Time Complexity:
__init__ : O(1)
postTweet : O(1)
getNewsFeed : O(U * T)
follow : O(1)
unfollow : O(1)

Space Complexity: O(N)
"""

class Twitter:
    def __init__(self):
        self.time = 0

        # Stores userId => Set[followedId]
        self.userIdToFollowedId = {}

        # Stores userId => List[(time, userId, tweetId)]
        self.userIdToTweetId = {}
        
    # O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userIdToTweetId:
            self.userIdToTweetId[userId] = []
        
        self.userIdToTweetId[userId].append((self.time, userId, tweetId))
        
        self.time += 1
        

    # O(U * T)
    def getNewsFeed(self, userId: int) -> List[int]:
        usersToFetchPostsFrom = [userId]
        tweetMinHeap = []

        if userId in self.userIdToFollowedId:
            for followedUserId in self.userIdToFollowedId[userId]:
                usersToFetchPostsFrom.append(followedUserId)

        for user in usersToFetchPostsFrom:
            if user in self.userIdToTweetId:
                for tweet in self.userIdToTweetId[user]:
                    heapq.heappush(tweetMinHeap, (tweet[0], (tweet[1], tweet[2])))

                    if len(tweetMinHeap) > 10:
                        heapq.heappop(tweetMinHeap)

        tweetMinHeap.sort(key = lambda x : x[0], reverse = True)

        return [tweetId for _, (tweetUserId, tweetId) in tweetMinHeap]

    # O(1)
    def follow(self, followerId: int, followedId: int) -> None:
        if followerId not in self.userIdToFollowedId:
            self.userIdToFollowedId[followerId] = set()

        self.userIdToFollowedId[followerId].add(followedId)
        
    # O(1)
    def unfollow(self, followerId: int, followedId: int) -> None:
        if followerId != followedId and followerId in self.userIdToFollowedId:
            self.userIdToFollowedId[followerId].discard(followedId)