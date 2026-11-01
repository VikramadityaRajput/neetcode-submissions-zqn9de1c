class Twitter {
private:
    std::map<int, set<int>> followMap; //map a user to a set of who theyre following
    int count; // in order to track recency of posts will be incremented
    std::map<int, vector<pair<int, int>>> tweetMap; //map a user to the tweets theyve  
public:
    Twitter() {
        count = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        tweetMap[userId].push_back({count, tweetId}); //add the tweet to the tweetmap
        count++; 
    }
    
    vector<int> getNewsFeed(int userId) {
        std::vector<int> res; 
        std::priority_queue<vector<int>> max_heap;
        followMap[userId].insert(userId); 
        int size = followMap[userId].size();
        //add the most recent tweet from each of your followers
        for (int followeeId : followMap[userId]) {
            if (tweetMap.count(followeeId)) {
                int index = tweetMap[followeeId].size() - 1; //we just want the last element
                int tweetTime = tweetMap[followeeId][index].first;
                int tweetId = tweetMap[followeeId][index].second;
                max_heap.push({tweetTime, tweetId, followeeId, index});
            }
        } 
        while (res.size() < 10 && !max_heap.empty()) {
            std::vector<int> top = max_heap.top();
            max_heap.pop();

            int tId = top[1];
            int fId = top[2];
            int index = top[3];
            res.push_back(tId);
            if (index >= 1) {
                int nextTime = tweetMap[fId][index - 1].first;
                int nextTweetId = tweetMap[fId][index - 1].second;
                max_heap.push({nextTime, nextTweetId, fId, index - 1});
            }
        }
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        followMap[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followMap.contains(followerId)) {
            followMap[followerId].erase(followeeId);
        }
    }
};
