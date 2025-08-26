/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry=0;
        ListNode* final=NULL;
        ListNode* temp = NULL;
        
        while (l1 || l2){
            int sum = carry;

            if(l1){
                sum+=l1->val;
                l1 = l1->next;
            }
            if(l2){
                sum+=l2->val;
                l2 = l2->next; 
            }

            ListNode* node = new ListNode(sum%10);

            if (temp==NULL){
                temp=final=node;
            }else{
                temp->next=node;
                temp=temp->next;
            }
            carry=sum/10;

        }
        if(carry>0){
            temp->next = new ListNode(carry);
        }
        return final;
    }
};