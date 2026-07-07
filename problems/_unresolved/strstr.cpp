class Solution {
public:
    int strStr(const char *source, const char *target) {
        if (source == NULL || target == NULL) {
            return -1;
        }
        int target_size = strlen(target);
        int source_size = strlen(source);
        int i, j;
        for (i = 0; i < source_size - target_size + 1; i++) {
            for (j = 0; j < target_size; j++) {
                if (source[i + j] != target[j]) {
                    break;
                }
            }
            if (j == target_size) {
                return i;
            }
        }
        return -1;
    }
};

// Standard Approach KMP Algorithm (hard
// better solution : Robin Karp