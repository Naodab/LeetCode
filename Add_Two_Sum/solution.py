class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def listToNumber(self, l):
        num = 0
        multiplier = 1
        while l:
            num += l.val * multiplier
            multiplier *= 10
            l = l.next
        return num
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = self.listToNumber(l1)
        num2 = self.listToNumber(l2)
        
        total = num1 + num2
        dummy_head = ListNode(0)
        current = dummy_head
        
        if total == 0:
            return ListNode(0)
        
        while total > 0:
            current.next = ListNode(total % 10)
            current = current.next
            total //= 10
        
        return dummy_head.next

if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    
    # Print the result
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")