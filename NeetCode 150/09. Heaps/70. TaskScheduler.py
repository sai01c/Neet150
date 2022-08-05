"""
Approach: 
{follower: set(followee)}
{user: [[time, tweet], [time, tweet]]}

we use this two dictionaries to store 

I did not understand news feed. 
"""


class Twitter:
    def __init__(self):
        self.count = 0
        # userId -> list of [count, tweetIds]
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # we append the last tweet for every user
                heapq.heappush(
                    minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:  # here we add if there are any index-1 for that user
                # this logic is very very complicated
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(
                    minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
