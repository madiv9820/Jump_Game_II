## Dynammic Programming Approach
This solution uses **iterative dynamic programming** to compute the **minimum number of jumps** to reach the last index.
- We maintain a **cache** (`cache[i]`) where each entry stores the minimum jumps needed to reach the end from index `i`.
- Start from the **second-last index** and move backward to the first index.
- For each index `i`, we check all possible jumps (1 to `nums[i]`) and update `cache[i]` as:
    ```
    cache[i] = 1 + min(cache[i + step] for all valid steps)
    ```
- Base case:
    - ✅ Last index → 0 jumps
    - ❌ Dead-end (`nums[i] == 0`) → propagated as large `infinity` value

- Finally, `cache[0]` gives the minimum jumps from the first index.

### ⏱️ Time & Space Complexity 📊
- **Time Complexity:** `O(n²)`
    - For each index `i`, we iterate over up to `nums[i]` possible jumps → worst case O(n²)

- **Space Complexity:** `O(n)`
    - Stores the DP cache of size `n`

### ✅ Key Advantages
- Avoids recursion → **stack-safe**
- Handles **dead-ends** naturally
- Clear structure → foundation for **Greedy O(n) optimization**
- Ideal for **interviews and production-ready DP approach**
---