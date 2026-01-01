import unittest
from timeout_decorator import timeout
from source.python.solution import pySolution


class testPySolution(unittest.TestCase):
    """
    Unit tests for Jump Game II solution.
    Each test validates the minimum number of jumps
    required to reach the last index.
    """

    def setUp(self):
        """
        Runs before every test case.
        Used to initialize test data and solution instance.
        """

        # 📦 Test cases in the form:
        # (input_array, expected_min_jumps)
        self.__testCases = (
            ([2, 3, 1, 1, 4], 2),     # Normal case
            ([2, 3, 0, 1, 4], 2),     # Zero in between, still reachable
            ([0], 0),                 # Single element (already at end)
            ([1], 0),                 # One element with jump capacity
            ([1, 1, 1, 1], 3),        # Worst case: jump at every index
            ([10, 0, 0, 0], 1),       # Large jump covers entire array
            ([4, 1, 1, 1, 1], 1),     # First jump reaches the end
            ([2, 1, 1, 1, 1], 3),     # Greedy decision validation
            ([1, 2, 3], 2),           # Increasing jump lengths
            ([2, 0, 2, 0, 1], 2)      # Zeros that must be skipped carefully
        )

        # 🧠 Create instance of the solution class
        self.__solution = pySolution()

        super().setUp()

    @timeout(2.0)
    def test(self):
        """
        Main test method.
        Uses subTest so each input is treated as an independent test.
        """

        # 🔁 Iterate over all test cases
        for nums, expected in self.__testCases:
            with self.subTest(nums=nums):
                # 🚀 Call the solution method
                actual = self.__solution.jumps(nums=nums)

                # ✅ Validate the result
                self.assertEqual(
                    actual,
                    expected,
                    f"Failed for input {nums}: expected {expected}, got {actual}"
                )


# ▶️ Allows running the test file directly
if __name__ == '__main__':
    unittest.main()