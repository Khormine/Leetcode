class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            total= carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res = str(total % 2) + res
            carry = total // 2
        if carry > 0:
            res = str(1) + res
        return res
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("11","1"))
    print(solution.addBinary("1010", "1011"))
