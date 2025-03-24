# You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
# #
# # Return the count of days when the employee is available for work but no meetings are scheduled.
# #
# # Note: The meetings may overlap.


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        merged_meetings = []
        for meeting in meetings:
            if not merged_meetings or meeting[0] > merged_meetings[-1][1]:
                merged_meetings.append(meeting)
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])

        meeting_days_count = 0
        for start, end in merged_meetings:
            meeting_days_count += end - start + 1

        return days - meeting_days_count
