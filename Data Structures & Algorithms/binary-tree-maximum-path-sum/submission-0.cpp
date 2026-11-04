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
    int maxPathSum(TreeNode* root) {
        //maybe we need a helper function to get the max of the children
        int res = root->val; // it would js be the current val to start
        dfs(root, res);
        return res;
    }
private:
    int dfs(TreeNode* root, int& res) { //pass it as a reference so that dfs has access to it
        if (root == nullptr) { // basic edgeguard
            return 0;
        } //do the recursive calls
    int leftmax = dfs(root->left, res); 
    int rightmax = dfs(root->right, res);
    leftmax = std::max(leftmax, 0); //if its negative we don't want it
    rightmax = std::max(rightmax, 0);
    res = std::max(res, root->val + leftmax + rightmax); //compute max pathsum with a split
    return root->val + std::max(leftmax, rightmax); //only pick one side thats higher max
    }
};
