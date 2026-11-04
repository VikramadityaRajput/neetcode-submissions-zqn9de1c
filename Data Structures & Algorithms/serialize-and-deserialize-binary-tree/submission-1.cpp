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
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (root == nullptr) {
            return "N,";
        }
        return to_string(root->val) + ',' + serialize(root->left) + serialize(root->right);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        //we have to actually figure out node.val so i guess u just iterate along the string until a comma
        stringstream ss(data);
        return build(ss);
    }
private:
    TreeNode* build(stringstream& ss) {
        string val;
        
        if (!getline(ss, val, ',') || val == "N") { //stores the next val
            return nullptr; //base case to exit
        }
        TreeNode* node = new TreeNode(stoi(val)); //save it to a node
        node->left = build(ss); //recursive call
        node->right = build(ss);
        return node;
    }
};
