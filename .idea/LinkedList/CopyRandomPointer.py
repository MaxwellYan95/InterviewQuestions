from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head == None:
            return None;
        dictionary = dict();
        cur = head;
        while cur != None:
            dictionary[cur] = Node(cur.val, None, None);
            cur = cur.next;
        cur = head;
        while cur != None:
            copy = dictionary[cur];
            if cur.next != None:
                copy.next = dictionary[cur.next];
            else:
                copy.next = None;
            if cur.random != None:
                copy.random = dictionary[cur.random];
            else:
                copy.random = None;
            cur = cur.next;
        return dictionary[head];

first = Node(7, None, None);
second = Node(13, None, None);
third = Node(11, None, None);
