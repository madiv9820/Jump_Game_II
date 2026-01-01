from typing import List

class pySolution:
    def jumps(self, nums: List[int]) -> int:
        """
        Returns the minimum number of jumps required to reach the last index of the array.
        Approach: Bottom-Up Dynamic Programming (iterative)
        """

        # 🔢 Length of the input array
        n: int = len(nums)

        # 🔢 Large number representing an unreachable state (dead-end)
        self.__infinity: int = 1_000_000

        # 💾 DP cache: cache[i] = minimum jumps to reach the end from index i
        cache: List[int] = [self.__infinity] * n

        # ✅ Base case: last index needs 0 jumps to reach itself
        cache[n-1] = 0

        # 🔁 Fill the DP table backwards from second-last element to the first
        for currentIndex in range(n-2, -1, -1):
            # 🎯 Initialize minJumps for this index
            minJumps: int = self.__infinity

            # 🔁 Explore all jumps from 1 to nums[currentIndex]
            for step in range(1, nums[currentIndex] + 1):
                # Only consider jumps that stay within array bounds
                if currentIndex + step < n:
                    minJumps = min(minJumps, cache[currentIndex + step])

            # ➕ Store result in cache: 1 jump from currentIndex + min jumps from reachable indices
            cache[currentIndex] = 1 + minJumps

        # 🚀 Final answer: minimum jumps from index 0
        result: int = cache[0]

        # 🧹 Cleanup cache to free memory
        del cache

        return result