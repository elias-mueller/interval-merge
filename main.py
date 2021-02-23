def merge(intervals):
    """
    Merges overlapping intervals

    :param intervals: list of tuples; first element < second
    :return: list of merged intervals
    """
    if len(intervals) <= 1:
        return intervals

    # Sorting the intervals is cheap and makes traversal simple.
    intervals.sort(key=lambda x: x[0])

    merged_invervals = []
    min_num = intervals[0][0]
    max_num = intervals[0][1]

    for i in range(len(intervals)):
        a = intervals[i][0]
        b = intervals[i][1]
        if a <= max_num:
            max_num = max(max_num, b)
        else:
            merged_invervals.append([min_num, max_num])
            min_num = a
            max_num = b

    # Add final interval
    merged_invervals.append([min_num, max_num])

    return merged_invervals


if __name__ == '__main__':
    test_input = [[25, 30], [2, 19], [14, 23], [4, 8]]
    target_result = [[2, 23], [25, 30]]
    result = merge(test_input)
    assert result == target_result
