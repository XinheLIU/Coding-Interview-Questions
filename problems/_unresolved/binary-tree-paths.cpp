/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ret;
        if (root) dfs(root, "", ret);
        return ret;
    }
    void dfs(TreeNode *root, string out, vector<string> &ret) {
        out += to_string(root->val);
        if (!root->left && !root->right) ret.push_back(out);
        else {
            if (root->left) dfs(root->left, out + "->", ret);
            if (root->right) dfs(root->right, out + "->", ret);
        }
    }
};