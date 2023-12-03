with open("a.txt") as f:
    content = f.readlines()
    size = len(content)

    # Find numbers
    nums = [[] for _ in range(size)]  # nums[i]: [[num, j1, j2], ...]
    part = False
    for i in range(size):
        for j in range(size):
            ch = content[i][j]
            if ch.isdecimal():
                if part:  # Continue of the num
                    nums[i][-1][0] += ch
                else:  # New num
                    part = True
                    nums[i].append([ch, j, -1])
            elif part:  # End of the num
                nums[i][-1][2] = j - 1
                part = False
        if part:  # End of the line
            nums[i][-1][2] = size - 1
            part = False

    def is_adjacent(i: int, j: int) -> list[str]:
        result = []
        for row in nums[i - (i > 0) : i + 1 + (i < size - 1)]:
            for num in row:
                if num[1] - 1 <= j <= num[2] + 1:
                    result.append(num[0])
        return result

    total = 0
    for i in range(size):
        for j in range(size):
            ch = content[i][j]
            if ch == "*":
                part_nums = is_adjacent(i, j)
                if len(part_nums) == 2:
                    total += int(part_nums[0]) * int(part_nums[1])
    print(total)
