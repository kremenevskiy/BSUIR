def merge_intervals(intervals, new_interval):
    ans = []
    up_left, up_right = None, None
    for interval in intervals:
        if interval[0] == new_interval[0] and interval[1] == new_interval[1]:
            return intervals
        if interval[0] > new_interval[1] or interval[1] <= new_interval[0]: # new между
            ans.append(interval)
            continue
        if interval[0] <= new_interval[0] and interval[1] >= new_interval[1]:
            return intervals
        if interval[0] >= new_interval[0] and interval[1] <= new_interval[1]:
            continue
        if interval[0] <= new_interval[0] and interval[1] <= new_interval[1]:
            up_right = interval
        if interval[0] >= new_interval[0] and interval[1] >= new_interval[1]:
            up_left = interval

    if up_left is None and up_right is None:
        ans.append(new_interval)
    elif up_right is None:
        up_left[0] = new_interval[0]
        ans.append(up_left)
    elif up_left is None:
        up_right[1] = new_interval[1]
        ans.append(up_right)
    else:
        ans.append([up_right[0], up_left[1]])
    return ans

intervals = [[3,5],[8,10],[1,2],[6,7],[12,16]]
print(merge_intervals(intervals, [4, 8]))
