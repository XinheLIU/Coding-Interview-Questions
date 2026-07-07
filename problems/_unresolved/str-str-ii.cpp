class Solution {
public:
    /**
     * @param source a source string
     * @param target a target string
     * @return an integer as index
     */
    int base = 1000000;
    int strStr2(const char* source, const char* target) {
       /* 通常我们认为标准的解决办法为 KMP 算法。但是 KMP 算法有着较高的学习和实现难度。这里介绍另外一种算法 - Rabin Karp。该算法与 KMP 有着同等的时间复杂度 O(n+m) ，但实现方法却更简单，也更容易理解。更能够帮助我们进一步理解哈希函数的特性和原理
       */
        if(target == NULL) {
            return -1;
        }
        int m = strlen(target);
        if(m == 0) {
            return 0;
        }
        if(source == NULL) {
            return -1;
        }
         int n = strlen(source);
        if(n == 0) {
            return -1;
        }
        if (m == 0) {
            return 0;
        }
        // mod could be any big integer
        // just make sure mod * 33 wont exceed max value of int.
        int mod =INT_MAX / 33;
        int hash_target = 1;

        // 33 could be something else like 26 or whatever you want
        for (int i = 0; i < m; ++i) {
            hash_target = (hash_target * 33 + target[i] - 'a') % mod;
            if (hash_target < 0) {
                hash_target += mod;
            }
        }
        int m33 = 1;
        for (int i = 0; i < m - 1; ++i) {
            m33 = m33 * 33 % mod;
        }
        int value = 1;
        for (int i = 0; i < n; ++i) {
            if (i >= m) {
                value = (value - m33 * (source[i]- 'a')) % mod;
            }
            value = (value * 33 + source[i] - 'a') % mod;
            if (value < 0) {
                value += mod;
            }
            if (i >= m - 1 && value == hash_target) {
                // you have to double check by directly compare the string
                // if (target.equals(source.substring(i - m + 1, i + 1))) {
                string target1(target); 
                string source1(source);
                if (target1.compare(source1.substr(i - m + 1, i + 1)) == 0) {
                    return i - m + 1;
                }
               // }
            }
        }
        return -1;
    }
};