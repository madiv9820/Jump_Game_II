from typing import List

class pySolution:
    def jumps(self, nums: List[int]) -> int:
        """
        Returns the minimum number of jumps to reach the last index of the array.
        This is a **top-down recursive solution with memoization** (DP).
        """

        # 🔢 A large value representing an unreachable state
        infinity: int = 1_000_000

        # 💾 Memoization cache:
        # cache[i] stores the minimum jumps needed from index i to the end
        cache: List[int] = [infinity] * len(nums)

        def Jump(currentIndex: int = 0) -> int:
            """
            Recursive helper function to compute min jumps from currentIndex
            """

            # ✅ Base case: if current index is at or past the last element
            # no jumps are needed
            if currentIndex >= len(nums) - 1:
                return 0

            # ❌ Dead-end case: cannot move forward from this index
            if nums[currentIndex] == 0:
                return infinity

            # 🧠 Memoization check:
            # Only compute if we haven't already stored a result
            if cache[currentIndex] == infinity:
                minJumps = infinity

                # 🔁 Try all possible jumps from current position
                for step in range(1, nums[currentIndex] + 1):
                    minJumps = min(minJumps, Jump(currentIndex + step))

                # ➕ Store the result (+1 for the jump from currentIndex)
                cache[currentIndex] = 1 + minJumps

            # 💾 Return cached result to avoid recomputation
            return cache[currentIndex]

        # 🚀 Start recursion from index 0
        result: int = Jump()

        # 🧹 Cleanup cache to free memory
        del cache

        return result