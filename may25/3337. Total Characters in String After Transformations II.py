# You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:
#
# Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
# The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
# Return the length of the resulting string after exactly t transformations.
#
# Since the answer may be very large, return it modulo 109 + 7.

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        def vec_mult(v, A):
            return [sum(v[k]*A[k][j] for k in range(26))%MOD
                    for j in range(26)]

        def mat_mult(A, B):
            C = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if A[i][k]:
                        aik = A[i][k]
                        for j in range(26):
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
            return C

        def apply_pow(v, A, e):
            res_v, base, first = v[:], A, True
            while e:
                if e & 1:
                    res_v = vec_mult(res_v, base) if not first else vec_mult(v, base)
                    first = False
                base = mat_mult(base, base)
                e >>= 1
            return res_v


        M = [[0]*26 for _ in range(26)]
        freq, MOD = [0] * 26, 10**9 + 7
        for ch in s:
            freq[ord(ch) - 97] += 1

        for i in range(26):
            for k in range(1, nums[i] + 1):
                M[i][(i + k) % 26] += 1

        final_vec = apply_pow(freq, M, t)
        return sum(final_vec) % MOD