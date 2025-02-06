from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = self.convertToArray(head);
        lst.sort();
        return self.convertToLinkedList(lst);

    def convertToArray(self, head: Optional[ListNode]) -> list[int]:
        if head == None:
            return [];
        lst = self.convertToArray(head.next);
        lst.append(head.val);
        return lst;

    def convertToLinkedList(self, lst: list[int]) -> Optional[ListNode]:
        if len(lst) == 0:
            return None;
        if len(lst) == 1:
            return ListNode(lst[0], None);
        next = self.convertToLinkedList(lst[1:]);
        return ListNode(lst[0], next);

sol = Solution()
sol.convertToLinkedList([1, 2, 3, 4]);