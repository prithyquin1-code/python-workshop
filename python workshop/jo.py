class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        currnode = head
        while currnode:
            result.append(currnode.val)
            currnode=currnode.next 
        return result == result[::-1]
        
