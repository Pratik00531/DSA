class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p = ListNode(0)
        curr = p
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry, digit = divmod(total, 10)
            curr.next = ListNode(digit)
            curr = curr.next

        return p.next   