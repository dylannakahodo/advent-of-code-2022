from string import ascii_letters

def priority(c):
    return ascii_letters.index(c) + 1

def get_comparments(rucksack):
    mid = len(rucksack) // 2
    return (rucksack[:mid], rucksack[mid:])

def find_common(compartments):
    compartments = [set(c) for c in compartments]
    return set.intersection(*compartments).pop()


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [l.strip() for l in f.readlines()]

    part1_total = 0
    for l in lines:
        compartments = get_comparments(l)
        common = find_common(compartments)
        part1_total += priority(common)
    print(part1_total)

    part2_total = 0
    for i in range(0, len(lines), 3):
        group = [lines[i], lines[i+1], lines[i+2]]
        common = find_common(group)
        part2_total += priority(common)
    print(part2_total)
