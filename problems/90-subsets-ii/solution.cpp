class Solution {
   private:
   void helper (vector<vector<int> >& res, vector<int>& out, const vector<int> &S, int start ) {
       res.push_back(out);
       for (int i = start; i < S.size(); ++i) {     //attention: i is from the start
           out.push_back(S[i]);
           helper(res, out, S, i+1);
           out.pop_back();
           while (i < S.size()-1 && S[i] == S[i+1]) i++; //eliminating repeating
       }
   }
public:
    vector<vector<int> > subsetsWithDup(vector<int> &S) {
        vector<vector<int> > res; 
        vector<int> out;
        sort(S.begin(), S.end());
        helper(res, out, S, 0);
        return res;
    }
};