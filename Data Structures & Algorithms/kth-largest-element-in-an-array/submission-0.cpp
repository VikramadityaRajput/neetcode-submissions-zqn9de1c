class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::priority_queue<int> max_heap(nums.begin(), nums.end()); //maxheap with nums
        for (int i = 0; i < k - 1; i++) {
            max_heap.pop();
        } //now our max heap is of size k
        return max_heap.top();
    }
};
