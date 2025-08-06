# this program detects if a linked list has a cycle


def has_cycle(head):
    slowP = head
    fastP = head.next
    while fastP and fastP.next:
        if slowP == fastP:
            return True
        slowP = slowP.next
        fastP = fastP.next.next

    return False