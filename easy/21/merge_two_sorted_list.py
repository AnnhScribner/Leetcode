# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __str__(self):
        return f"[{self.val}, {self.next}]"

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def arr_to_linked_list(lst: list[int]) -> Optional[ListNode]:
    if len(lst) == 0:
        return None

    node = ListNode(val=lst[0])
    curr = node
    for i in range(1, len(lst)):
        curr.next = ListNode(lst[i])
        curr = curr.next
    return node

class Solution:
    def mergeTwoLists(self, list1 : ListNode, list2 : ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        final_list = None #create an empty ListNode
        curr_final_list = final_list
        curr1 = list1
        curr2 = list2

        while curr1 or curr2:
            if curr1 is None:
                curr_final_list.next = curr2
                return final_list
            elif curr2 is None:
                curr_final_list.next = curr1
                return final_list
            else:
                if curr1.val <= curr2.val: # if a <= b a comes first
                    if final_list is None:
                        final_list = curr1
                        curr_final_list = curr1
                        curr1 = curr1.next
                    else:
                        curr_final_list.next = curr1
                        curr_final_list = curr_final_list.next
                        curr1 = curr1.next
                elif final_list is None:
                    final_list = curr2
                    curr_final_list = curr2
                    curr2 = curr2.next
                else:
                    curr_final_list.next = curr2
                    curr_final_list = curr_final_list.next
                    curr2 = curr2.next

        return final_list



s = Solution()
list1 = arr_to_linked_list([1,2,4])
list2 = arr_to_linked_list([1, 3, 4])

print(s.mergeTwoLists(list1,list2))












