class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

def list_to_linkedlist(lst):
    if not lst:
        return None
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试代码
head_list = [1, 1, 2, 3, 3]
head = list_to_linkedlist(head_list)

solution = Solution()
new_head = solution.deleteDuplicates(head)

print(linkedlist_to_list(new_head))  # 输出：[1, 2, 3]
