#include <vector>
using namespace std;

class Solution {
private:
    // 🔢 Large number representing an unreachable state (dead-end)
    const int infinity = 1000000;

public:
    // 🚀 Entry point: returns minimum number of jumps to reach the last index
    int jump(vector<int>& nums) {
        int n = nums.size();

        // 💾 DP cache: cache[i] = minimum jumps to reach the end from index i
        vector<int> cache(n, infinity);

        // ✅ Base case: last index requires 0 jumps to reach itself
        cache[n-1] = 0;

        // 🔁 Fill the DP table backwards from second-last element to the first
        for(int currentIndex = n-2; currentIndex >= 0; --currentIndex) {
            int minJumps = infinity;

            // 🔁 Explore all jumps from 1 to nums[currentIndex]
            for(int step = 1; step <= nums[currentIndex]; ++step) {
                // Only consider jumps within array bounds
                if(currentIndex + step < n) {
                    minJumps = min(minJumps, cache[currentIndex + step]);
                }
            }

            // ➕ Store result in cache: 1 jump from currentIndex + min jumps from reachable indices
            cache[currentIndex] = 1 + minJumps;
        }

        // 🚀 Final answer: minimum jumps from index 0
        int result = cache[0];

        // 🧹 Free memory used by cache
        vector<int>().swap(cache);

        return result;
    }
};