/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 // ListNode* reverseList(ListNode* head) {
    //     if (!head) return head;
    //     ListNode *dummy = new ListNode(-1);
    //     dummy->next = head;
    //     ListNode *cur = head;
    //     while (cur->next) {
    //         ListNode *tmp = cur->next;
    //         cur->next = tmp->next;
    //         tmp->next = dummy->next;
    //         dummy->next = tmp;
    //     }
    //     return dummy->next;
    // }
    
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* p=head;
        head=reverseList(p->next);
        p->next->next=p;
        p->next=NULL;
        return head;
    }
};