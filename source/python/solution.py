from typing import List

class pySolution:
    def jumps(self, nums: List[int]) -> int:
        """
        Returns the minimum number of jumps required
        to reach the last index of the array.

        Approach:
        - Pure recursive (top-down) exploration
        - Tries all possible jumps from each index
        - Uses a large value to simulate infinity
        """

        # 🔢 A large number used to represent an unreachable state
        infinity: int = 1_000_000

        def Jump(currentIndex: int = 0) -> int:
            """
            Recursive helper function.

            Args:
                currentIndex (int): Current position in the array

            Returns:
                int: Minimum jumps needed from currentIndex to reach the end
            """

            # ✅ Base case:
            # If we've reached or crossed the last index,
            # no more jumps are required
            if currentIndex >= len(nums) - 1:
                return 0

            # ❌ Dead-end case:
            # If current position has 0 jump length,
            # it is impossible to move forward
            if nums[currentIndex] == 0:
                return infinity

            # 🎯 Initialize minimum jumps from this index
            minJumps: int = infinity

            # 🔁 Try all possible jump lengths from this index
            # (1 step up to nums[currentIndex] steps)
            for step in range(1, nums[currentIndex] + 1):
                # Recursively compute jumps from the next index
                minJumps = min(
                    minJumps,
                    Jump(currentIndex + step)
                )

            # ➕ Add 1 for the jump taken from currentIndex
            return 1 + minJumps

        # 🚀 Start recursion from index 0
        return Jump()