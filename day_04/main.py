def reading():
    f = open("input.txt","r")
    content = f.readlines()
    f.close()
    return content

def main1():
    data = reading()
    
    total = 0

    for line in data:
        left, right = line.split('| ')
        game, winning_numbers = left.split(': ')

        winning_numbers = winning_numbers.split()

        scratch_cards = right.split()

        first_num = True

        count = 0

        for i in scratch_cards:
            if i in winning_numbers and first_num:
                count += 1
                first_num = False
            
            elif i in winning_numbers:
                count *= 2

        total += count

    print(total)

def main2():
    data = reading()

    keyList = range(1,204)

    game_counts = dict(zip(keyList, [1]*len(keyList)))

    for i, line in enumerate(data):

        left, right = line.split('| ')
        game, winning_numbers = left.split(': ')

        winning_numbers = winning_numbers.split()

        scratch_cards = right.split()

        count = 0

        for j in scratch_cards:
            if j in winning_numbers:
                count += 1

        for k in range(count):
            try:
                game_counts[i+k+1] += 1 * game_counts[i+1]
            except:
                break

    total = 0

    for i in game_counts:
        try:
            total += int(game_counts[i+1])
        except:
            break

    print(total)


main2()
        

