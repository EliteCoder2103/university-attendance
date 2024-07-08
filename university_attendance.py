class UniversityAttendance:
    def __init__(self, days):
        """
        Initializes the UniversityAttendance object with the number of days.

        :param days: Number of days in the academic year
        """
        self.days = days
        self.memo = {}

    def count_total_ways_to_attend_class(self):
        """
        Calculates the total number of ways to attend classes over N days.

        :return: Total number of ways to attend classes
        """
        return self._count_total_ways_to_attend_class_helper(self.days, 0)

    def _count_total_ways_to_attend_class_helper(self, days_remaining, missed_streak):
        """
        Recursive helper function to count the ways to attend classes, considering constraints.

        :param days_remaining: Number of days remaining to attend classes
        :param missed_streak: Current streak of missed classes
        :return: Number of ways to attend classes for the remaining days
        """
        if days_remaining == 0:
            return 1

        if (days_remaining, missed_streak) in self.memo:
            return self.memo[(days_remaining, missed_streak)]

        # Attend class today
        ways_attend_today = self._count_total_ways_to_attend_class_helper(days_remaining - 1, 0)

        # Miss class today, if the missed streak is less than 3
        ways_miss_today = 0
        if missed_streak < 3:
            ways_miss_today = self._count_total_ways_to_attend_class_helper(days_remaining - 1, missed_streak + 1)

        total_ways_to_attend_class = ways_attend_today + ways_miss_today
        self.memo[(days_remaining, missed_streak)] = total_ways_to_attend_class
        return total_ways_to_attend_class

    def count_ways_to_miss_graduation(self):
        """
        Calculates the number of ways to miss the graduation ceremony on the last day.

        :return: Number of ways to miss the graduation ceremony
        """
        return self._count_ways_to_miss_graduation_helper(self.days - 1, 1)

    def _count_ways_to_miss_graduation_helper(self, days_remaining, missed_streak):
        """
        Recursive helper function to count the ways to miss the graduation ceremony.

        :param days_remaining: Number of days remaining to graduation
        :param missed_streak: Current streak of missed classes
        :return: Number of ways to miss the graduation ceremony
        """
        if days_remaining == 0:
            return 1 if missed_streak >= 1 else 0

        if (days_remaining, missed_streak) in self.memo:
            return self.memo[(days_remaining, missed_streak)]

        # Attend class today
        ways_attend_today = self._count_ways_to_miss_graduation_helper(days_remaining - 1, 0)

        # Miss class today, if the missed streak is less than 3
        ways_miss_today = 0
        if missed_streak < 3:
            ways_miss_today = self._count_ways_to_miss_graduation_helper(days_remaining - 1, missed_streak + 1)

        total_ways_to_miss_graduation = ways_attend_today + ways_miss_today
        self.memo[(days_remaining, missed_streak)] = total_ways_to_miss_graduation
        return total_ways_to_miss_graduation

    def get_result(self):
        """
        Generates the result string in the format 'ways_to_miss_graduation/total_ways'.

        :return: Result string
        """
        total_ways_to_attend_class = self.count_total_ways_to_attend_class()
        ways_to_miss_graduation = self.count_ways_to_miss_graduation()
        return f"{ways_to_miss_graduation}/{total_ways_to_attend_class}"


if __name__ == "__main__":
    days = int(input("Enter the number of days: "))
    ua = UniversityAttendance(days)
    print(ua.get_result())