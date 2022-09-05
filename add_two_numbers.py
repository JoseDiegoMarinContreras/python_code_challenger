"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    root = cursor = ListNode()
    carry = 0
    while l1 or l2:
        val1 = val2 = 0
        if l1:
            val1 = l1.val
            l1 = l1.next
        if l2:
            val2 = l2.val
            l2 = l2.next
            
        summatory = val1 + val2 + carry
        carry = summatory // 10
        cursor.next = ListNode(summatory%10)
        cursor = cursor.next
    return root.next

# 3 -> 4 -> 2
l1_n1 = ListNode(2)
l1_n2 = ListNode(4, l1_n1)
l1_n3 = ListNode(3, l1_n2)

# 4 -> 6 -> 5
l2_n1 = ListNode(5)
l2_n2 = ListNode(6, l2_n1)
l2_n3 = ListNode(4, l2_n2)

# 7 -> 0 -> 8
print(add_two_numbers(l1_n3, l2_n3))