# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use Counter to count the frequency of each element in both arrays
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        # Initialize the result list
        result = []

        # Iterate through the first counter and find common elements
        for num in counter1:
            if num in counter2:
                # Find the minimum count for each common element
                min_count = min(counter1[num], counter2[num])
                # Add the element min_count times to the result list
                result.extend([num] * min_count)

        return result