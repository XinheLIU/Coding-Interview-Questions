// Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.
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
    TreeNode* subtree = NULL;
    int subtreeSum = INT_MAX;
    int helper(TreeNode* root) {
        if (!root)
            return 0;
        int sum = helper(root->left) + helper(root->right) + root->val;
        if (sum < subtreeSum ) {
            subtreeSum = sum;
            subtree = root;
        }
        return sum;
    }
    
    TreeNode* findSubtree(TreeNode* root) {
        helper(root);
        return subtree;
    }
};