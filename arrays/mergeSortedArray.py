from components.ListNode import ListNode


def mergeSortedArray(nums1: ListNode, nums2: ListNode):
    dummy = ListNode()
    ptr = dummy
    while nums1 and nums2:
        if nums1.val < nums2.val:
            ptr.next = nums1
            nums1 = nums1.next
        else:
            ptr.next = nums2
            nums2 = nums2.next
        ptr = ptr.next
    if nums1:
        ptr.next = nums1
    if nums2:
        ptr.next = nums2
    return dummy.next
