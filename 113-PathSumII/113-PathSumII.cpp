// Last updated: 8/21/2025, 4:43:45 PM
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
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        std::vector<vector<int>> resultVector;
        if (root==NULL){
            return resultVector;
        }
        std::vector<int> start;
        dfs(root, targetSum, 0, resultVector, start);
        return resultVector;
    }

    void dfs(TreeNode* root, int targetSum, int runningSum, std::vector<vector<int>> &resultVector, std::vector<int>currVector){
        
        bool found = false;
        
        runningSum += root->val;
        currVector.push_back(root->val);
        if (root->left == NULL && root->right == NULL && targetSum==runningSum){
            resultVector.push_back(currVector);
            
        }

        if(root->left !=NULL){
        
            dfs(root->left, targetSum, runningSum, resultVector, currVector);
            
            //currVector.pop_back();
        }
        if(root->right!=NULL){
            dfs(root->right, targetSum, runningSum, resultVector, currVector);
           
            //currVector.pop_back();
        }

        

    }
};