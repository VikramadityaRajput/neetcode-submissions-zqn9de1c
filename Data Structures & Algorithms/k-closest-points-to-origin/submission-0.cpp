#include <queue>
class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        //first step is just to convert all coordinates to d^2 (save a calculation by not doing a sqrt)
        std::priority_queue<std::pair<int, std::vector<int>>> max_heap;
        vector<int> distances;
        vector<vector<int>> res;
        for (unsigned int i = 0; i < points.size(); i++) {
            int distance = (points[i][0] * points[i][0]) + (points[i][1] * points[i][1]);
            max_heap.push({distance, points[i]});
        } //now we have a vector and were going to heapify it
        while (max_heap.size() > k) {
            max_heap.pop();
        } //now our heap is of size k
        while (!max_heap.empty()) {
            std::vector<int> add = max_heap.top().second;
            res.push_back(add);
            max_heap.pop();
        }
        return res;
    }   
};
