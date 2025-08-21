// Last updated: 8/21/2025, 4:25:12 PM
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

 //DFS down, if root, check running sum
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root==NULL){
            return false;
        }
        return dfs(root,targetSum, 0);
    }

    bool dfs(TreeNode* root, int targetSum, int runningSum){
        bool found = false;
        //std::cout<<root->val<<"\n";
        runningSum += root->val;
        if (root->left == NULL && root->right == NULL){
            //runningSum += root.val;
            //std::cout<<"leaf"<<"\n";
            return targetSum == runningSum;
        }

        if(root->left !=NULL){
            //std::cout<<"going left"<<"\n";
            found = found || dfs(root->left, targetSum, runningSum);
        }
        if(root->right!=NULL){
            //std::cout<<"going right"<<"\n";
            found = found || dfs(root->right, targetSum, runningSum);
        }

        return found;

    }
};