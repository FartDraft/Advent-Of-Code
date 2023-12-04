with open("a.txt") as f:
    lines = f.readlines()
    cards = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        have = set()
        win = set()
        bar = False
        for num in line.split()[2:]:
            if num == "|":
                bar = True
            elif bar:
                win.add(int(num))
            else:
                have.add(int(num))
        for j in range(i + 1, i + 1 + len(have.intersection(win))):
            cards[j] += cards[i]
    print(sum(cards))
