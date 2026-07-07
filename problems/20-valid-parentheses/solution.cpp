/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */
// @lc code=start
#include <iostream>
#include <unordered_map>
using namespace std;
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> map = {{')','('},{']','['},{'}','{'}};
        stack<char> stack;
        for (char &c: s){
            if (map.find(c) == map.end())
                stack.push(c);
            else
            {
                if(stack.empty() || map[c] != stack.top())
                    return false;
                stack.pop();
            }
        }
        return stack.empty();
    }
};
// @lc code=end

