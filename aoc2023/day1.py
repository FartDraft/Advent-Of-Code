from re import compile

first_letter = compile(r"[1-9]|one|two|three|four|five|six|seven|eight|nine").search
last_letter = compile(
    r".*([1-9]|one|two|three|four|five|six|seven|eight|nine).*?"
).search
letters = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("day1b.txt") as f:
    print(
        sum(
            [
                int(
                    letters[first_letter(line).group()]
                    + letters[last_letter(line).group(1)]
                )
                for line in f.read().splitlines()
            ]
        )
    )
