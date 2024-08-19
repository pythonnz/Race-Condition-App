class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
                continue
            
            innerString = ""
            while stack and stack[-1] != '[':
                innerString = stack.pop() + innerString
            stack.pop() # Pop '['
            
            multiplier = ""
            while stack and stack[-1].isdigit():
                multiplier = stack.pop() + multiplier
            
            stack.append(int(multiplier) * innerString)
        
        return ''.join(stack)

if __name__ == "__main__":
    s = Solution()
    # print(s.decodeString("3[a2[c]]"))

    inputs = [
        "4[ad]2[lmn]1[xy]",
        "m2[i3[num]um]",
    ]
    for i in inputs:
        print(i, s.decodeString(i))
    #     print(s.decodeString(i))
    # print(s.decodeString("3[a2[c]]"))

    # print(solution())

