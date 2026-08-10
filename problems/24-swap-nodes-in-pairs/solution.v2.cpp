/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 *
 * Approach 2: Recursive
 */

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        // Recursion carries the "node before the pair" implicitly: the caller
        // holds it, so each frame only swaps its own two nodes and trusts the
        // recursive call to return the already-swapped remainder.
        if (!head || !head->next) return head;  // fewer than two nodes left
        ListNode *first = head, *second = head->next;
        first->next = swapPairs(second->next);
        second->next = first;
        return second;  // second is the new head of this pair
    }
};
