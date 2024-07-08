import unittest
from university_attendance import UniversityAttendance

class TestUniversityAttendance(unittest.TestCase):

    def test_case_5_days(self):
        ua = UniversityAttendance(5)
        self.assertEqual(ua.get_result(), "14/29")

    def test_case_10_days(self):
        ua = UniversityAttendance(10)
        self.assertEqual(ua.get_result(), "372/773")

if __name__ == "__main__":
    unittest.main()

    