/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right>;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right> = NULL;
 *     }
 * }
 */
class RetType {
public:
     int sum,size;
     RetType():sum(0),size(0){};
     RetType(int _sum, int _size):sum(_sum),size(_size){};
    };
    
class Solution {
private:
    TreeNode* node = NULL;
    RetType data;
public:
    TreeNode* findSubtree2(TreeNode* root) {
        helper(root);       //attention the use of this function- no given value
        return node;
    }    
    RetType helper(TreeNode* root) {
        if (!root)
            return RetType();            
        RetType left = helper(root->left);
        RetType right = helper(root->right);
        RetType ret = RetType(left.sum + right.sum + root->val, left.size + right.size + 1);
        //attention here
        if (!node || data.size * ret.sum >= ret.size * data.sum ) {  
            node = root;
            data = ret;
        }
        return ret;
        
    }
// act as global variables here
    
};