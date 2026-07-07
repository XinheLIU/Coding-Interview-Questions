class Solution {
public:
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    int findPeak(vector<int> A) {
        int l = 1, r = A.size();
        int mid;
        while (l <= r) {
            mid = (l + r) >> 1;
            if (A[mid] > A[mid - 1] && A[mid] > A[mid+1])
                return mid;
            if (A[mid] > A[mid - 1]) 
                l = mid + 1;
            else
                r = mid - 1;
        }
        return -1; 
    }
};
