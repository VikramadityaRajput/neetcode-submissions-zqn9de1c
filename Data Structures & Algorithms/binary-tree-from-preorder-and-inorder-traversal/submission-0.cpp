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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
            if (preorder.empty() || inorder.empty()) {
            return nullptr;
        }
        TreeNode* root = new TreeNode(preorder[0], nullptr, nullptr);
        int mid = find(inorder, preorder[0]);
        vector<int> leftPre = sliceTree(preorder, 1, mid + 1);
        vector<int> leftIn = sliceTree(inorder, 0, mid);
        root->left = buildTree(leftPre, leftIn);
        vector<int> rightPre = sliceTree(preorder, mid+1, preorder.size());
        vector<int> rightIn = sliceTree(inorder, mid+1, preorder.size());
        root->right = buildTree(rightPre, rightIn);
        return root;
    }
    int find(vector<int> nums, int num) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums.at(i) == num) return i;
        }
        return -1;
    }
    vector<int> sliceTree(vector<int>& original, int start, int end) {
        vector<int> result;
        for (int i = start; i < end; i++) {
            result.push_back(original.at(i));
        }
        return result;
    }
};
//first value in pre is the root
//use the index of the root's location in IOT to partition 
//recursivley call the algorithm until youre at the base case