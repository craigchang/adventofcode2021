# https://adventofcode.com/2021/day/1

def readFile():
    with open("./day1/input.txt", "r") as f:
        return [int(l.strip()) for l in f]

def part1():
    depths = readFile()
    print( sum( [1 for i in range(1, len(depths)) if depths[i] > depths[i-1]] ) )

def part2():
    depths = readFile()
    inc = 0
    for i in range(3, len(depths)):
        sumA = depths[i-3] + depths[i-2] + depths[i-1]
        sumB = depths[i-2] + depths[i-1] + depths[i]
        if sumB > sumA:
            inc += 1
    print(inc)

part1()
part2()