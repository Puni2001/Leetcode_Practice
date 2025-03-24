class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # sort meetings by start time
        meetings.sort(key=lambda meeting: meeting[0])

        # add available days before starting the first meeting
        free_days=max(meetings[0][0]-1, 0)
        # merged_interval will have the merged intervals, initialize it with the first meeting 
        merged_interval=meetings[0]

        for i in range(1, len(meetings)):
            # if the new meeting has the starting time > merged interval's ending time then we can safely add the available day
            if meetings[i][0]> merged_interval[1]:
                # add available days
                free_days+=max(meetings[i][0]-merged_interval[1]-1, 0)
                # this interval cannot be merged, update merged interval
                merged_interval=meetings[i]
            else:
                # merge the interval with min of starting times and max of ending times
                merged_interval=[merged_interval[0] , max(meetings[i][1], merged_interval[1])]

        # add available days after the last meeting
        free_days+=max(days - merged_interval[1], 0)

        return free_days