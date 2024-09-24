import math

class Solution:
    def lcm(self, N, M):
        gcd = math.gcd(N, M)
        lcm = (N * M) // gcd
        return lcm

if __name__ == "__main__":
    # Test Cases
    print(Solution().lcm(4, 6))         # Output: 12
    print(Solution().lcm(5, 10))        # Output: 10
    print(Solution().lcm(7, 3))         # Output: 21
    print(Solution().lcm(1, 987654321)) # Output: 987654321
    print(Solution().lcm(123456, 789012)) # Output: 8117355456

    # User Input
    N, M = map(int, input("enter two numbers spillted by space: ").split())  # Taking input for two integers
    print(Solution().lcm(N, M))

