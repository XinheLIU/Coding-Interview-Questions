class Solution {
 private:
    void helper(vector<vector<int> > &res,
                vector<int> &out,
                vector<int> &nums,
                int start) {
        res.push_back(out);
        for (int i = start; i < nums.size(); ++i) {
            out.push_back(nums[i]);
            helper(res, out, nums, i + 1);
            out.pop_back();
        }
    }
 public:
    vector<vector<int> > subsets(vector<int> &nums) {
        vector<vector<int> > res;
        vector<int> out;
        helper(res, out, nums, 0);
        return res;
    }
};as