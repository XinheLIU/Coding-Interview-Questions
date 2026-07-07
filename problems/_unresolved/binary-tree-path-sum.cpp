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
    void dfs(vector<vector<int>>& ret, vector<int> path, TreeNode *root, int target, int sum) {
        if (!root)
            return;
        path.push_back(root->val);
        sum += root->val;
        if (!root->left && !root->right && sum == target)
            ret.push_back(path);
        dfs(ret, path, root->left, target, sum);
        dfs(ret, path, root->right, target, sum);
        // attention here!
        sum -= root->val;
        path.pop_back();
    }
    vector<vector<int>> binaryTreePathSum(TreeNode *root, int target) {
        vector<vector<int>> ret;
        vector<int> path;
        dfs(ret,path,root,target,0);
        return ret;
    }
};