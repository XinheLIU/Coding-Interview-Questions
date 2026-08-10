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
    bool hasCycle(ListNode *head) {
        // Floyd's cycle detection: fast moves two steps per one of slow, so the
        // gap between them grows by exactly one each iteration. Inside a cycle of
        // length L that gap is taken mod L, so it eventually hits 0 — they meet.
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {  // only fast can fall off; checking it covers both
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
    }
};
