# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
#
# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a dictionary to store the indices of elements in arr2
        index_map = {num: i for i, num in enumerate(arr2)}

        # Define a custom sorting function
        def custom_sort(num):
            if num in index_map:
                return (0, index_map[num])  # Sort by appearance order in arr2
            else:
                return (1, num)  # Sort other elements at the end in ascending order

        # Sort arr1 using the custom sorting function
        arr1.sort(key=custom_sort)

        return arr1
