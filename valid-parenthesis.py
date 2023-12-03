#https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:

        counter = {
            '(': 0,
            ')': 0,
            '{': 0,
            '}': 0,
            '[': 0,
            ']': 0
        }

        openChar = ['(', '{', '[']
        closeChar = [')', '}', ']']

        # quick check start-end
        if s[0] not in openChar or s[len(s) - 1] not in closeChar:
            return False

        openCloseDict = dict(zip(openChar, closeChar))

        stack = []
        i = 0

        while i < len(s):
            letter = s[i]
            counter[letter] += 1

            if letter in openChar:
                stack.append(letter)
            
            if letter in closeChar:
                if len(stack) <= 0: 
                    return False
                popedLetter = stack.pop()

                if openChar.index(popedLetter) != closeChar.index(letter):
                    return False
            i = i + 1
                
        if len(stack) != 0:
            return False

        return True



if __name__ == '__main__':

    s = Solution()
    
    testCase = "[]))"
    print("Solution for testCase:", testCase, "is :", s.isValid(testCase))

    testCase = "(([]))"

    print("Solution for testCase:", testCase, "is :", s.isValid(testCase))
