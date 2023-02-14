from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = ""
        ptr = self
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next
        res = res.strip(", ")
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        last = head
        current = head.next
        while(current is not None):
            if current.val == last.val:
                last.next = current.next
            else:
                last = current
            current = current.next
        return head

if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2)))))
    print(solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))))
