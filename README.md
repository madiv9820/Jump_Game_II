# [Jump Game II](https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150)

### 📌 Problem Overview 
You are given a **0-indexed integer array** `nums`, where each element represents the **maximum jump length** you can make from that index. You start at **index 0**, and your goal is to reach the **last index** (`n - 1`) using the **minimum number of jumps**.

From any index `i`, you may jump forward to **any index within range**:
```
i + j  where  0 ≤ j ≤ nums[i]  and  i + j < n
```

The problem guarantees that **reaching the last index is always possible**, so you do not need to handle unreachable cases.

### 🎯 Objective

Determine the **minimum number of jumps** required to reach the end of the array.

### 🧩 Key Points to Understand
- You can jump **only forward**, never backward.
- Each jump can have a **variable length**, depending on the value at the current index.
- You are free to choose **any valid jump length** at each step.
- The challenge lies in minimizing the **number of jumps**, not the distance.

### 📝 Examples
- **Example 1** <br> **Input:** `[2,3,1,1,4]` <br> **Output:** 2 <br> **Explanation:** Jump from index 0 → 1, then from 1 → 4.

- **Example 2** <br> **Input:** `[2,3,0,1,4]` <br> **Output:** 2

### ⚙️ Constraints
- `1 ≤ nums.length ≤ 10⁴`
- `0 ≤ nums[i] ≤ 1000`
- The last index is always **reachable**

This problem tests your ability to reason about **reachability**, **decision-making under constraints**, and **optimization of steps** — making it a classic and important problem for technical interviews.

---

### Approaches
- [**Recursion**](https://github.com/madiv9820/Jump_Game_II/tree/Approach_01-Recursion)

    Recursively try all possible jumps 🦘 from each index and find the path with the minimum total jumps 🎯. Uses a large number to simulate dead-ends ❌. No memoization is used, so the recursion explores all possibilities 🔁.

- [**Memoization**](https://github.com/madiv9820/Jump_Game_II/tree/Approach_02-Memoization)

    Recursively explore all jumps 🦘 from each index and store the minimum in a cache 💾. Memoization avoids recomputation 🔁, so cache[0] gives the minimum jumps to reach the end 🎯.

- [**Dynamic Programming**](https://github.com/madiv9820/Jump_Game_II/tree/Approach_03-Dynamic_Programming)

    Build a DP cache 💾 from the end 🔁, where each index stores the minimum jumps to reach the last index 🎯. For each position, check all reachable steps and pick the one with fewest jumps 🦘. cache[0] gives the answer ✅.

- [**Greedy**](https://github.com/madiv9820/Jump_Game_II/tree/Approach_04-Greedy)
    
    Greedily expands each jump’s reachable range 🚧 and commits to a jump only when the current range is exhausted 🦘. By always extending to the farthest possible index 🎯, it guarantees the minimum number of jumps to reach the end.
---