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
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # empty list
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        # head
        if list1.val < list2.val:
            temp = head = ListNode(list1.val)
            list1 = list1.next
        else:
            temp = head = ListNode(list2.val)
            list2 = list2.next

        # merge until one list is empty
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next

        # add all nodes in l1/l2
        while list1 is not None:
            temp.next = ListNode(list1.val)
            list1 = list1.next
            temp = temp.next
        while list2 is not None:
            temp.next = ListNode(list2.val)
            list2 = list2.next
            temp = temp.next
        return head

if __name__ == "__main__":
    solution = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    print(solution.mergeTwoLists(list1, list2))

    list1 = None
    list2 = None
    print(solution.mergeTwoLists(list1, list2))

    list1 = None
    list2 = ListNode(0)
    print(solution.mergeTwoLists(list1, list2))