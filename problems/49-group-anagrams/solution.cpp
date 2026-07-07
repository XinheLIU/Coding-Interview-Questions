/*
 * @lc app=leetcode id=49 lang=cpp
 *
 * [49] Group Anagrams
 */

// @lc code=start
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       vector<vector<string>> res;
       unordered_map<string, vector<string>> m;
       for (string s:strs){
           vector<int> cnt(26,0);
           string t = "";
           for (char c:s) ++cnt[c - 'a'];
           for (int d:cnt) t += to_string(d) + "/";
           m[t].push_back(s);
       }
       for (auto a:m)
           res.push_back(a.second);
        return res;
    }
};
// @lc code=end

