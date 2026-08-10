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
    ListNode* reverseList(ListNode* head) {
        // Recurse to the tail first, then flip links on the way back up.
        // new_head is the original tail, passed through every frame unchanged.
        if (!head || !head->next) return head;
        ListNode* cur = head;
        ListNode* new_head = reverseList(cur->next);
        // cur->next is still the node ahead of us; point it back at cur,
        // then cut cur's forward link or the two nodes form a cycle.
        cur->next->next = cur;
        cur->next = NULL;
        return new_head;
    }
};
