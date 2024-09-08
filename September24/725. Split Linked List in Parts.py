# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
#
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
#
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
#
# Return an array of the k parts.

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Count the number of nodes
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        # Step 2: Calculate the size of each part and the number of extra nodes
        part_size, extra_nodes = divmod(count, k)

        # Step 3: Split the list into k parts
        current = head
        result = []
        for i in range(k):
            part_head = current
            for j in range(part_size - 1 + (i < extra_nodes)):
                if current:
                    current = current.next
            if current:
                next_node = current.next
                current.next = None
                current = next_node
            result.append(part_head)

        return result
