#include <vector>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        /*
        Returns the minimum number of jumps to reach the last index.
        Approach: Greedy (Jump Range Expansion)
        */

        // 🦘 Total number of jumps taken so far
        int totalSteps = 0;

        // 🚀 Farthest index that can be reached within the current jump window
        int maxReachableIndex = 0;

        // 🚧 End boundary of the current jump range
        int currentJumpEnd = 0;
        
        // 🔁 Traverse the array index by index
        for(int currentIndex = 0; currentIndex < nums.size(); ++currentIndex) {

            // 📈 Update the farthest index reachable from currentIndex
            maxReachableIndex = max(
                maxReachableIndex,
                currentIndex + nums[currentIndex]
            );

            // 🛑 When we reach the end of the current jump range,
            // we must commit to a jump
            if(currentIndex == currentJumpEnd) {

                // ✅ If the last index is already reachable, stop early
                if(currentJumpEnd >= nums.size() - 1)
                    break;

                // ➕ Commit to the next jump
                totalSteps++;

                // 🔄 Extend the jump range to the farthest reachable index
                currentJumpEnd = maxReachableIndex;
            }
        }

        // 🎯 Minimum number of jumps required to reach the last index
        return totalSteps;
    }
};