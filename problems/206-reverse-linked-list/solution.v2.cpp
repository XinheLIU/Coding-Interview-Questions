/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 *
 * Approach 2: Iterative head insertion
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Different idea from the pointer-flip: cur stays pinned to the original
        // head (which becomes the tail) while every following node is unhooked
        // and spliced in directly after the dummy. Order emerges by construction.
        if (!head) return head;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* cur = head;
        while (cur->next) {
            ListNode* next_node = cur->next;
            cur->next = next_node->next;   // unhook next_node
            next_node->next = dummy->next; // splice it to the front
            dummy->next = next_node;
        }
        return dummy->next;
    }
};
