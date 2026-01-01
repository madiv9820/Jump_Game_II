## Greedy Approach 
The idea is to treat each jump as a **range of indices** rather than choosing a specific jump position.
While traversing the array, we greedily track the **farthest index reachable** from all positions within the current jump range.
- `currentJumpEnd` represents the boundary of the current jump.
- `maxReachableIndex` stores the farthest index that can be reached by exploring all indices within this range.
- When the current index reaches `currentJumpEnd`, we are **forced to take a jump**, and we extend the jump range to `maxReachableIndex`.

This strategy ensures that each jump covers the **maximum possible distance**, resulting in the **minimum number of jumps** required to reach the last index.

### ⏱️ Complexity Analysis
- **Time Complexity: `O(n)`**
    - The array is traversed once, and each index is processed only once.
- **Space Complexity: `O(1)`**
    - No extra data structures are used; only a few variables track the jump state.

### 🎯 Key Insight
Instead of deciding ***where*** to jump, the greedy approach decides ***when*** to jump — always choosing the option that maximizes future reach.
---