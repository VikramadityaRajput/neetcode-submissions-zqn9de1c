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
    vector<vector<int>> levelOrder(TreeNode* root) {
        std::vector<vector<int>> res;
        if (root == nullptr) {
            return res;
        }
        TreeNode* curr = root;
        std::queue<TreeNode*> q;
        q.push(curr);

        while (!q.empty()) {
            int size = q.size();
            std::vector<int> tres;
            for (unsigned int i = 0; i < size; i++) {
                curr = q.front();
                if (curr->left != nullptr) {
                    q.push(curr->left);
                }
                if (curr->right != nullptr) {
                    q.push(curr->right);
                }
                tres.push_back(curr->val);
                q.pop();
            }
            res.push_back(tres);
        }
        return res;
    }
};
