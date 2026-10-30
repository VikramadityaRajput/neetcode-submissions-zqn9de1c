#include <queue>
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::priority_queue<int> max_heap(stones.begin(), stones.end());
        while (!max_heap.empty()) {
            if (max_heap.size() == 1) {
                return max_heap.top();
            }
            int stone1 = max_heap.top();
            max_heap.pop();
            int stone2 = max_heap.top();
            max_heap.pop();
            if (stone1 == stone2) {
                continue;
            }
            if (stone1 < stone2) {
                stone2 -= stone1;
                max_heap.push(stone2);
            } else if (stone1 > stone2) {
                stone1 -= stone2;
                max_heap.push(stone1);
            }
        }
        return 0;
    }
};
