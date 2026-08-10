/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        // Invariant: prev sits immediately before the pair being swapped, so
        // prev -> first -> second becomes prev -> second -> first.
        // The dummy head turns the first pair into an interior case like the rest.
        ListNode *dummy = new ListNode(-1), *prev = dummy;
        dummy->next = head;
        while (prev->next && prev->next->next) {  // a lone final node stays put
            ListNode *first = prev->next, *second = prev->next->next;
            // Order matters: first must adopt second's successor before second
            // points back at first, or the tail of the list is dropped.
            first->next = second->next;
            second->next = first;
            prev->next = second;
            prev = first;  // first is now the tail of the swapped pair
        }
        return dummy->next;
    }
};
