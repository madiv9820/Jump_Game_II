#include <vector>
using namespace std;

class Solution {
private:
    // 🔢 A large value representing an unreachable state
    int infinity = 1000000;

    // 📦 Store the input array for recursive access
    vector<int> nums;

    // 💾 Memoization cache:
    // cache[i] stores the minimum jumps needed from index i to the end
    vector<int> cache;

    // 🔁 Recursive helper function to compute minimum jumps from currentIndex
    int Jump(int currentIndex = 0) {
        // ✅ Base case: if we have reached or passed the last index,
        // no more jumps are required
        if(currentIndex >= nums.size() - 1) 
            return 0;

        // ❌ Dead-end case: cannot move forward from this index
        if(nums[currentIndex] == 0) 
            return infinity;

        // 🧠 Check if result is already computed in cache
        if(cache[currentIndex] == infinity) {
            int minJumps = infinity;

            // 🔁 Try all possible jumps from current index
            for(int step = 1; step <= nums[currentIndex]; ++step) {
                minJumps = min(minJumps, Jump(currentIndex + step));
            }

            // ➕ Store the result in cache (+1 for the jump from currentIndex)
            cache[currentIndex] = 1 + minJumps;
        }

        // 💾 Return cached result to avoid recomputation
        return cache[currentIndex];
    }

public:
    // 🚀 Entry point for computing minimum jumps
    int jump(vector<int>& nums) {
        // 📥 Store input array in class member
        this->nums = nums;

        // 💾 Initialize memoization cache with "infinity"
        this->cache = vector<int>(nums.size(), infinity);

        // 🧠 Compute minimum jumps starting from index 0
        int result = Jump();

        // 🧹 Clean up memory
        vector<int>().swap(nums);
        vector<int>().swap(cache);

        return result;        
    }
};