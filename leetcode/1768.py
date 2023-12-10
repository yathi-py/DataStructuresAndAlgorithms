# 1768. Merge Strings Alternately

import timeit
class Solution:
    def two_pointer(self, word1: str, word2: str) -> str:
        i,j= 0, 0
        str3 = []
        while i < len(word1) or j <len(word2):
            if i < len(word1):
                str3 += word1[i]
                i+=1

            if j <len(word2):
                str3 += word2[j]
                j+=1
        return ''.join(str3)

    def merge_alternately(self, word1: str, word2: str) -> str:
        word3 =''
        i = 0

        # Iterate through the characters of both strings until the shorter one is exhausted
        #min(len(word1), len(word2)) --> O(min(N,M)
        while i < len(word1) and i < len(word2):
            word3 += word1[i] + word2[i]
            i+=1

        # Append the remaining characters from the longer string to the result
        # O(max(N,M) to append
        if len(word1) > len(word2):
            word3 += word1[len(word2):]
        else:
            word3 += word2[len(word1):]
        return word3

mergeAlternately = Solution()

code_to_measure = "mergeAlternately.merge_alternately('abc', 'pdfdf')"
print(mergeAlternately.two_pointer(word1 = 'abc', word2 = 'pdf'))
execution_time = timeit.timeit(code_to_measure, globals=globals(), number=100000)
print(f'time taken: {execution_time}')

# the time complexity is O(max(N<M) - min(N,M) --> ignore the lower bound
# O(max(N,M) or it can be written as O(M+N)


