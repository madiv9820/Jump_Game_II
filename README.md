## Memoization Approach
This solution improves the **pure recursive approach** by adding **memoization** to avoid recomputation of subproblems.

From each index, we try all **possible jumps** (1 to `nums[i]`) and recursively compute the minimum jumps needed to reach the last index.

Results of each index are stored in a **cache** (`cache[i]`) so that repeated visits to the same index return the stored value instead of recomputing.

Base cases:
- ✅ If current index ≥ last index → 0 jumps needed
- ❌ If `nums[i] == 0` → dead end, return a large "infinity" value

The final answer is **1 (current jump) + minimum jumps from all reachable next indices**.

### ⏱️ Time & Space Complexity 📊
- **Time Complexity: `O(n²)`**
    - Each index is computed once, but for each index we may iterate over all possible jumps (`1..nums[i]`) → worst case `O(n²)`.
- **Space Complexity: `O(n)`**
    - Cache of size `n` + recursion stack depth of `n`

### ✅ Key Advantages
- Reduces the **exponential time complexity** of pure recursion (`O(2ⁿ)`) to **polynomial**.
- Handles dead-ends and single-element arrays naturally.
- Provides a clear path to further optimizations:
    - Bottom-Up DP
    - Greedy O(n) solution

### ⚠️ Limitations
- Still **slower for very large arrays** with large jump values due to nested loops.
- Not fully optimal compared to **Greedy `O(n)`**, but excellent for **understanding the problem structure**.
---