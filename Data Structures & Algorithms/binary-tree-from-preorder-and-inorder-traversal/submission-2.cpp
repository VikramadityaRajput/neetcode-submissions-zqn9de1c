#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> inorderMap;
        for (int i = 0; i < inorder.size(); i++) {
            inorderMap[inorder[i]] = i;
        }
        int preorderIndex = 0;
        return build(preorder, inorder, inorderMap, preorderIndex, 0, inorder.size() - 1);
    }

private:
    TreeNode* build(vector<int>& preorder, vector<int>& inorder, unordered_map<int, int>& inorderMap, int& preorderIndex, int inStart, int inEnd) {
        if (inStart > inEnd) {
            return nullptr;
        }
        
        // The current root is always the current preorder element
        int rootVal = preorder[preorderIndex++];
        TreeNode* root = new TreeNode(rootVal);
        
        // Find where this root is in the inorder array
        int mid = inorderMap[rootVal];
        
        // Recursively build the left and right subtrees using the calculated bounds
        root->left = build(preorder, inorder, inorderMap, preorderIndex, inStart, mid - 1);
        root->right = build(preorder, inorder, inorderMap, preorderIndex, mid + 1, inEnd);
        
        return root;
    }
};