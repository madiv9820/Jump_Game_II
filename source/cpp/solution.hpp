#include <vector>
using namespace std;

class Solution {
private:
    // 📦 Stores the input array so it can be accessed by the recursive function
    vector<int> nums;

    // 🔢 A large value used to represent an unreachable state
    int infinity = 1000000;

    // 🔁 Recursive helper function to compute minimum jumps
    int Jump(int currentIndex = 0) {
        // ✅ Base case:
        // If we have reached or crossed the last index,
        // no more jumps are needed
        if (currentIndex >= nums.size() - 1)
            return 0;

        // ❌ Dead-end case:
        // If the current position has zero jump length,
        // we cannot move forward
        if (nums[currentIndex] == 0)
            return infinity;

        // 🎯 Initialize minimum jumps from this index
        int minJumps = infinity;

        // 🔁 Try all possible jump lengths from current index
        // (1 step up to nums[currentIndex] steps)
        for (int step = 1; step <= nums[currentIndex]; ++step) {
            minJumps = min(
                minJumps,
                Jump(currentIndex + step)
            );
        }

        // ➕ Add 1 jump for the move taken from currentIndex
        return 1 + minJumps;
    }

public:
    // 🚀 Entry point called by the test / main function
    int jump(vector<int>& nums) {
        // 📥 Store input array in class member for recursion
        this->nums = nums;

        // 🧠 Compute minimum jumps starting from index 0
        int result = Jump();

        // 🧹 Clear the local copy of nums to free memory
        vector<int>().swap(this->nums);

        return result;
    }
};