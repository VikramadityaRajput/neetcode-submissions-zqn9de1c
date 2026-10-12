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
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
    int dfs(TreeNode* root, int msf) {
        if (root == nullptr) {
            return 0;
        }
        int gc = 0;

        if (root->val >= msf) {
            gc += 1;
            msf = root->val;
        }
        gc += dfs(root->left, msf);
        gc += dfs(root->right, msf);
        return gc;
    }
};
