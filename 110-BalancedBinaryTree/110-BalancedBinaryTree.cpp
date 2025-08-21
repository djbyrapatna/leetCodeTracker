// Last updated: 8/21/2025, 1:50:21 PM
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

//DFS algorithm search, want to keep

#include <cmath>

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        
        auto [dummy, isBalanced] = dfs(root);

        return isBalanced;

    }

    std::pair<int, bool> dfs(TreeNode* root){
        if (root==NULL){
            return std::make_pair(0,true);
        }
        

        auto [leftHeight, leftBalanced] = dfs(root->left);
        auto [rightHeight, rightBalanced] = dfs(root->right);

        bool balanced = leftBalanced && rightBalanced && (std::abs(leftHeight-rightHeight)<=1);
        
        int retHeight = std::max(leftHeight, rightHeight)+1;

        return std::make_pair(retHeight, balanced);
    }

};