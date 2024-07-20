def merge(intervals):
    # ans=[]  # Initialize an empty list to store the merged intervals
    # intervals.sort()  # Sort the intervals based on the start time
    # n=len(intervals)  # Get the length of the intervals list
    # for i in range(n):  # Iterate through each interval
    #     s,e=intervals[i][0],intervals[i][1]  # Get the start and end time of the current interval
    #     if ans and e<=ans[-1][1]:  # If the ans list is not empty and the end time of the current interval is less than or equal to the end time of the last merged interval
    #         continue  # Skip to the next iteration
    #     for j in range(i+1,n):  # Iterate through the remaining intervals
    #         if intervals[j][0]<=e:  # If the start time of the next interval is less than or equal to the end time of the current interval
    #             e=max(e,intervals[j][1])  # Update the end time of the current interval if necessary
    #         else:
    #             break  # Exit the inner loop if the start time of the next interval is greater than the end time of the current interval
    #     ans.append([s,e])  # Add the merged interval to the ans list
    # return ans  # Return the merged intervals
    # # Initialize an empty list to store the merged intervals
    ans = []

    # Sort the intervals based on the start time
    intervals.sort()

    # Iterate through each interval
    for i in range(len(intervals)):
        # If the ans list is empty or the current interval's start time is greater than the end time of the last merged interval
        if not ans or intervals[i][0] > ans[-1][1]:
            # Add the current interval to the ans list
            ans.append(intervals[i])
        else:
            # Update the end time of the last merged interval if necessary
            ans[-1][1] = max(ans[-1][1], intervals[i][1])

    # Return the merged intervals
    return ans