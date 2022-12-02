with open("input.txt", "r") as f:
    lines = f.read().split("\n\n")

data = [sum(list(map(int, x.split()))) for x in lines]
print(max(data))

print(sum(sorted(data)[:-4:-1]))
