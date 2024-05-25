#On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

def reading():
    file = open("Day 1 input.txt","r")
    contents = file.readlines()
    file.close()
    return contents

def part_1():
    count = 0
    contents = reading()

    for line in contents:
        first = 1
        last = 1
        for i in line:
            if i.isdigit():
                first = i   
                break
        
        for j in reversed(line):
            if j.isdigit():
                last = j
                break

        total = first + last
        count += int(total)

    print(count)

def part_2():
    count = 0
    contents = reading()
    numbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

    for line in contents:
        #find first and last int
        first = "c"
        last = 'c'

        for i in range(len(line)):
            if line[i].isdigit():
                first = i   
                break
        
        for j in reversed(range(len(line))):
            if line[j].isdigit():
                last = j
                break

        store = {'first':100, 'last':0}
        str_first = 0
        str_last = 0

        for number in numbers:
            if number in line:
                x = line.index(number)
                y = line[::-1].index(number[::-1])
                y = -(y + len(number)) + len(line)
                if x < store['first']:
                    store['first'] = x
                    str_first = number
                if y > store['last']:
                    store['last'] = y
                    str_last = number

        if first < store['first'] or str_first == 100:
            xx = line[first]
        else:
            xx = numbers[str_first]

        if last > store['last'] or str_last == 0:
            yy = line[last]
        else:
            yy = numbers[str_last]

        total = str(xx) + str(yy)
        count += int(total)

    print(count)

part_2()


