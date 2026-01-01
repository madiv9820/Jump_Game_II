from typing import List

class pySolution:
    def jumps(self, nums: List[int]) -> int:
        """
        Returns the minimum number of jumps to reach the last index.
        Approach: Greedy (Jump Range Expansion)
        """

        # 🦘 Total number of jumps taken so far
        totalSteps: int = 0

        # 🚀 Farthest index that can be reached within the current jump window
        maxReachableIndex: int = 0

        # 🚧 End boundary of the current jump range
        currentJumpEnd: int = 0

        # 🔁 Traverse the array index by index
        for currentIndex in range(len(nums)):

            # 📈 Update the farthest index we can reach from this position
            maxReachableIndex = max(
                maxReachableIndex,
                currentIndex + nums[currentIndex]
            )

            # 🛑 If we have reached the end of the current jump range,
            # we must take a jump and extend the range
            if currentIndex == currentJumpEnd:

                # ✅ If the last index is already reachable, stop early
                if currentJumpEnd >= len(nums) - 1:
                    break

                # ➕ Commit to a jump
                totalSteps += 1

                # 🔄 Update the next jump range using the farthest reach found
                currentJumpEnd = maxReachableIndex

        # 🎯 Minimum number of jumps required to reach the end
        return totalSteps