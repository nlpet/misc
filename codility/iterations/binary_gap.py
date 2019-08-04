
# O(n) solution
def solution_slow(N):
    bin_n = bin(N)
    longest, gap = 0, 0

    for b in bin_n[2:]:
        if b == '0':
            gap += 1
        else:
            longest = max(longest, gap)
            gap = 0

    return longest



# O(log2(N)) solution
def solution(N):
    powers, current_power = [], 0
    largest, gap, n = 0, 0, N

    while 2 ** current_power <= N:
        powers.append(2 ** current_power)
        current_power += 1

    for p in powers[::-1]:
        if n - p >= 0:
            n -= p
            largest = max(largest, gap)
            gap = 0
        else:
            gap += 1


    return largest
