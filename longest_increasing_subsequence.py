"""
Given an array, find the longest increasing (not necessarily consecutive)
subsequence.
"""


def subsequence(array):
    """
    :list : array (input array)
    """
    if not array:
        return array

    length = len(array)

    starting_points = [None] * length
    previous_elements = [None] * length

    # Since the array is non-empty, it contains at least an
    # increasing subsequence of length 1 (tracker)
    tracker = 1
    starting_points[0] = 0

    # Starting from the 2nd element
    for i in range(1, length):
        # Perform binary search - find the largest
        # index which is <= tracker
        lower = 0
        upper = tracker

        if array[starting_points[upper - 1]] < array[i]:
            indx = upper
        else:
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if array[starting_points[mid - 1]] < array[i]:
                    lower = mid
                else:
                    upper = mid

            indx = lower

        previous_elements[i] = starting_points[indx - 1]

        if indx == tracker or array[i] < array[starting_points[indx]]:
            starting_points[indx] = i
            tracker = max(tracker, indx + 1)

    result = []
    position = starting_points[tracker - 1]
    for _ in range(tracker):
        result.append(array[position])
        position = previous_elements[position]

    return result[::-1]


if __name__ == '__main__':
    A = [10, 12, 11, 3, 5, 60, 50, 55, 56, 68, 59, 60]
    print "Array is: %s" % " ".join([str(n) for n in A])
    subseq = subsequence(A)
    print "Longest subseq is: %s" % " ".join([str(n) for n in subseq])
