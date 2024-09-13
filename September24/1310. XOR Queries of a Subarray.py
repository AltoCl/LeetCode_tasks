# You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].
#
# For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).
#
# Return an array answer where answer[i] is the answer to the ith query.

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0 for _ in range(len(arr))]
        prefix[0] = arr[0]

        # calculating the prefix array of xor of all elements from 0th index to ith index
        for i in range(1, len(arr)):
            prefix[i] = prefix[i - 1] ^ arr[i]

        xor_arr = []  # result array
        for query in queries:
            low_index, high_index = query[0] - 1, query[1]
            if low_index == -1:  # i.e take xor from 0th index
                xor_arr.append(prefix[high_index])
            else:
                xor_arr.append(prefix[high_index] ^ prefix[low_index])
                # ex.   query = [1,3]  ans = (xor till 3rd index) ^ (xor till 0th index)
        return xor_arr