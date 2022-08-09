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
    pointer = result = ListNode()
    op1 = l1
    op2 = l2
    carry = 0
    while op1 or op2:
        sumatory = (op1.val if op1 else 0) + (op2.val if op2 else 0) + carry
        pointer.next = ListNode(sumatory%10)
        carry = sumatory // 10
        pointer = pointer.next
        op1 = op1.next if op1 else None
        op2 = op2.next if op2 else None
    if carry == 1:
        pointer.next = ListNode(1)

    return result.next

# 9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9
l1_n1 = ListNode(9)
l1_n2 = ListNode(9, l1_n1)
l1_n3 = ListNode(9, l1_n2)
l1_n4 = ListNode(9, l1_n3)
l1_n5 = ListNode(9, l1_n4)
l1_n6 = ListNode(9, l1_n5)
l1_n7 = ListNode(9, l1_n6)

# 9 -> 9 -> 9 -> 9
l2_n1 = ListNode(9)
l2_n2 = ListNode(9, l2_n1)
l2_n3 = ListNode(9, l2_n2)
l2_n4 = ListNode(9, l2_n3)

# 7 -> 0 -> 8
print(add_two_numbers(l1_n3, l2_n3))