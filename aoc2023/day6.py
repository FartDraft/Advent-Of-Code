with open("a.txt") as f:
    content = f.readlines()
    times = list(map(int, content[0].split()[1:]))
    distances = list(map(int, content[1].split()[1:]))

    total = 1
    for time, distance in zip(times, distances):
        ways = 0
        for speed in range(1, time):
            if speed * (time - speed) > distance:
                ways += 1
        total *= ways
    print(total)
