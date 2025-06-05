class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    lenA = get_length(headA)
    lenB = get_length(headB)

    # 让headA指向较长的链表
    if lenB > lenA:
        headA, headB = headB, headA
        lenA, lenB = lenB, lenA

    # 长链表先走差值步
    for _ in range(lenA - lenB):
        headA = headA.next

    # 同时遍历，找到第一个相同节点
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None  # 无相交节点


def print_linkedlist(head):
    vals = []
    current = head
    while current:
        vals.append(str(current.val))
        current = current.next
    print(" -> ".join(vals))

# 构造相交链表示例
# 公共部分
common = ListNode(8, ListNode(10))

# 链表A: 3 -> 7 -> 8 -> 10
headA = ListNode(3, ListNode(7, common))

# 链表B: 99 -> 1 -> 8 -> 10
headB = ListNode(99, ListNode(1, common))

print("链表A:")
print_linkedlist(headA)

print("链表B:")
print_linkedlist(headB)

intersection = getIntersectionNode(headA, headB)
if intersection:
    print(f"相交节点值为: {intersection.val}")
else:
    print("无相交节点")
