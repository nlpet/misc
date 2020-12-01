
def find_triplet(nums, target):
    nums_set = set(nums)
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            n = target - nums[i] - nums[j]
            if n in nums_set:
                print(f'{nums[i]}x{nums[j]}x{n}={nums[i] * nums[j] * n}')
                return


def main():
    target = 2020
    with open('input.txt', 'r') as fr:
        nums = [int(line.strip()) for line in fr.readlines()]

    find_triplet(nums, target)







if __name__ == '__main__':
    main()
