def reading():
    listin = []
    f = open("input.txt","r")
    content = f.readlines()
    for i in content:
        listin.append(i.strip())
    f.close()
    return listin

def find_part_numbers(grid, row, col):
    part_numbers = []

    for i in range(row - 1, row + 1):
        for j in range(col - 1, col + 1):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j].isdigit():
                part_numbers.append(int(grid[i][j]))

    return part_numbers

def calculate_sum():
    symbols = ['@','#','$','%','&','*','-','+','=','/']
    grid = reading()
    total_sum = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in symbols:
                part_numbers = find_part_numbers(grid, i, j)
                total_sum += sum(part_numbers)

    return total_sum

result = calculate_sum()
print("Sum of part numbers:", result)