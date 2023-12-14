# 271. Encode and Decode Strings

# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back
# to the original list of strings. Please implement encode and decode

# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"


class Solution:

    def encode(self,l):
        res = ''
        for d in l:
            res+=str(len(d))+'#'+d
        return res

    def decode(self,s):
        res =[]
        for i, v in enumerate(s):
            if s[i]=='#':
              leng = int(s[i-1])+int(i)+1
              res.append(s[i+1:leng])
        return res

sol = Solution()
encoded_data = sol.encode(["lint","code","love","you"])
print(encoded_data)
decoded_data = sol.decode(encoded_data)
print(decoded_data)