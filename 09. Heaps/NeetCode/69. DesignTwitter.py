"""
Approach: 

we use this two dictionaries to store followers and tweets. Along with tweets we also store time because
we need the 10 most recent ones. 
We append the last index elements to our heap. Among all the last index elements we pop from heap and if
index is more than 0 we add index-1 element to heap

Tc - nlogn
sc - n
"""


class Twitter:
    def __init__(self):
        self.time = 0 
        #we are starting our time from 0 and decreasing because we need the maximum time
        #so using min-heap by doing negative numbers
        self.tweetMap = defaultdict(list) 
        # { user: [(time, tweet), (time, tweet)]}
        # userId -> list of [time, tweetIds]
        self.followMap = defaultdict(set)  
        # userId -> set of followeeId
        # {follower: set(followee) }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1 #min-heap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId) #following himself
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 #last element
                time, tweetId = self.tweetMap[followeeId][index]
                # we append the last tweet for every user
                heapq.heappush(
                    minHeap, [time, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10: #we only want top 10 id's
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:                                                                                       
                # if index is -1 that means we only had 1 element (0-indexed)
                #so we want to add all values until index for that key becomes -1.
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(
                    minHeap, [time, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId) #add to set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: #using set because we can do this in O(1) operation.
            self.followMap[followerId].remove(followeeId)
