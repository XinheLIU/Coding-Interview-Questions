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
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> ret;
        vector<TreeNode*> stack;
        TreeNode* cur = root;
        while(!stack.empty() || cur){
            while(cur){
                stack.push_back(cur);
                cur = cur->left;
            }
            cur = stack.back();
            stack.pop_back();
            ret.push_back(cur->val);
            cur = cur->right;
        }
        return ret;
    }
};

class Solution2 {
public:
    vector<int> ret;
    vector<int> inorderTraversal(TreeNode *root) {
        ret.clear();
        traverse(root);
        return ret;
    }
    
    void traverse(TreeNode *root){
        if (!root)
            return;
        traverse(root->left);
        ret.push_back(root->val);
        traverse(root->right);
    }
};