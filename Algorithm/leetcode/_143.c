struct ListNode {
    int val;
    struct ListNode *next;
};
//Title: Reorder List
//Explanation: The list-rearranging logic is simple. Link from tail-side node
//to current next node and from current node to tail-side node. The point is
//HOW to go backwards from the tail and WHEN do you stop rearranging. You can
//use array to save nodes and can iterate through list backwards using array.
//When l is length of the list, l/2-1+len%2 is the exact count of loop.
void reorderList(struct ListNode* head) {
    struct ListNode* backwards[50000];
	int len = 0;
	struct ListNode* temp = head;
	while(temp) {
		backwards[len++] = temp;	
		temp = temp->next;
	}
	temp = head;
	int count = (len/2)-1+len%2;
    len--;
	for(int i=0; i<count; i++) {
		backwards[len]->next = temp->next;
		temp->next = backwards[len--];
		temp = temp->next->next;
    }
    backwards[len]->next = NULL;
}
