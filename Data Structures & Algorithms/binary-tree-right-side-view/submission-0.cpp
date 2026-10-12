/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        std::vector<int> nums;
        std::vector<TreeNode*> q;
        TreeNode* curr = root;
        if (root == nullptr) {
            return nums;
        }
        q.push_back(curr);
        while (!q.empty()) {
            nums.push_back(q.back()->val); //the last element after LOT
            int size = q.size();
            for (unsigned int i = 0; i < size; i++) {
                curr = q.front();
                if (curr->left != nullptr) {
                    q.push_back(curr->left);
                }
                if (curr->right != nullptr) {
                    q.push_back(curr->right);
                }
                q.erase(q.begin());
            }
        }
        return nums;
    }
};
//do a BFS and add the last number before going down