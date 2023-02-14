class Solution:
    # Programmation dynamique :
    #                _
    #              _| |
    #            _| | |
    #          _| | | |
    #        _| | | | |
    #       |_|_|_|_|_|
    #      0 1 2 3 4 5
    # PD  [8,5,3,2,1,1] 
    # Formule u_{n-2} = u_{n-1} + u_{n}
    def climbStairs(self, n: int) -> int:
        u0, u1 = 1, 1
        for i in range(1,n):
            u0, u1 = u0 + u1, u0
        return u0

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
