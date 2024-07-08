import unittest

def calculate_ways_and_probability(N):
    if N <= 0:
        return "0/1"  # Edge case: no days to attend

    dp_present = [0] * (N + 1)
    dp_absent = [0] * (N + 1)

    # Base case
    dp_present[0] = 1
    dp_absent[0] = 1

    for i in range(1, N + 1):
        dp_present[i] = dp_present[i - 1] + dp_absent[i - 1]
        if i >= 4:
            dp_absent[i] = dp_present[i - 1]
        else:
            dp_absent[i] = 0

    total_ways = dp_present[N] + dp_absent[N]
    miss_probability = dp_absent[N]

    return f"{miss_probability}/{total_ways}"

class TestAttendanceCalculation(unittest.TestCase):
    
    def test_case_5_days(self):
        self.assertEqual(calculate_ways_and_probability(5), "14/29")

    def test_case_10_days(self):
        self.assertEqual(calculate_ways_and_probability(10), "372/773")

if __name__ == "__main__":
    unittest.main()

