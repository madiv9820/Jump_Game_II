## Recursive Approach

This solution uses a **pure recursive (top-down) approach** to compute the **minimum number of jumps** needed to reach the last index 🚀.

From each index, we try **all possible jump lengths** (from `1` up to `nums[i]`) and recursively compute the minimum jumps required from the next reachable positions. The answer for the current index is calculated as: 
```
1️⃣ (current jump) + minimum jumps from all reachable next indices
```

To handle **unreachable paths** (when `nums[i] == 0`), a large value (`infinity`) is returned ❌ so that such paths are automatically ignored while taking the minimum.

### 🧠 Key Observations 🔍
- ✅ If the current index is at or beyond the last index → **0 jumps needed**
- ❌ If `nums[i] == 0` → **dead end**
- 🔁 The algorithm explores **every possible path** to ensure the minimum result

This clearly exposes the **problem structure** and makes it an excellent foundation for **DP or Greedy optimizations** later.

### ⏱️ Time & Space Complexity 📊
- **🕒 Time Complexity**
    - **`O(2ⁿ)` (Exponential)**
    - Each index can branch into multiple recursive calls, leading to repeated computations

- **🧠 Space Complexity**
    - **`O(n)`**
    - Due to the recursion call stack in the worst case

### ⚠️ Limitations 🚧
- ❌ Results in **TLE** for large inputs
- ❌ Recomputes the same subproblems multiple times
- ❌ Not suitable for production as-is

### ✅ Why this approach is still useful 🌱
- 📚 Great for **understanding recursion**
- 🧩 Helps naturally derive **memoization (DP)**
- 💡 Makes the **greedy `O(n)` solution easier to justify**

### 🔜 Next Steps 🚀
- Add **memoization** → reduce time complexity to **`O(n²)`**
- Use **greedy strategy** → optimal **`O(n)`** solution
---