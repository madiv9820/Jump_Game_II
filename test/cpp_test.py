import unittest
from timeout_decorator import timeout
from source.cpp.solution import cppSolution


class testCppSolution(unittest.TestCase):
    """
    Unit tests for the C++ implementation of Jump Game II.
    The C++ solution is exposed to Python (likely via bindings),
    and these tests validate its correctness.
    """

    def setUp(self):
        """
        Runs before each test.
        Initializes test cases and the C++ solution instance.
        """

        # 📦 Test cases structured as:
        # (input_array, expected_min_jumps)
        self.__testCases = (
            ([2, 3, 1, 1, 4], 2),     # Standard example
            ([2, 3, 0, 1, 4], 2),     # Zero in between, still reachable
            ([0], 0),                 # Single element (already at destination)
            ([1], 0),                 # One element with jump capability
            ([1, 1, 1, 1], 3),        # Worst case: jump at every index
            ([10, 0, 0, 0], 1),       # One jump reaches the end
            ([4, 1, 1, 1, 1], 1),     # First jump covers the entire array
            ([2, 1, 1, 1, 1], 3),     # Validates greedy boundary logic
            ([1, 2, 3], 2),           # Increasing jump lengths
            ([2, 0, 2, 0, 1], 2)      # Zeros that must be skipped carefully
        )

        # 🧠 Instantiate the C++ solution wrapper
        self.__solution = cppSolution()

        super().setUp()

    @timeout(2.0)
    def test(self):
        """
        Main test method.
        Uses subTest so each input array is treated independently.
        """

        # 🔁 Iterate through all test cases
        for nums, expected in self.__testCases:
            with self.subTest(nums=nums):
                # 🚀 Call the C++ jump() method
                actual = self.__solution.jump(nums=nums)

                # ✅ Assert expected vs actual result
                self.assertEqual(
                    actual,
                    expected,
                    f"Failed for input {nums}: expected {expected}, got {actual}"
                )


# ▶️ Enables running this test file directly
if __name__ == '__main__':
    unittest.main()