#The elf has a small bag and some cubes which are either red, green, or blue. 
#Each time you play this game, he will hide a secret number of cubes of each color in the bag
#Your goal is to figure out information about the number of cubes.
#The Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

#Each game is listed with its ID number (like the 11 in Game 11: ...) 
#Each game has a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).
#Example: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

#!!!!!The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes? (Add the possible game numbers together)!!!!!

def reading():
    f = open("Day 2 input.txt","r")
    content = f.readlines()
    f.close()
    return content

def p1_main():
    count = 0
    content = reading()

    for line in content:
        game, cont = line.split(": ")
        x,game_num = game.split()

        valid = True
        
        hand = cont.split("; ")
        for i in hand:
            color_num = i.split(", ")
            for j in color_num:
                num, color = j.split()
                if color == "blue" and int(num) > 14:
                        valid = False
                if color == "green" and int(num) > 13:
                        valid = False
                if color == "red" and int(num) > 12:
                        valid = False
        
        if valid:
            count += int(game_num)
            print(count)

def p2_main():
    count = 0
    content = reading()

    for line in content:
        high_red = 0
        high_green = 0
        high_blue = 0

        game, cont = line.split(": ")
        
        hand = cont.split("; ")
        for i in hand:
            color_num = i.split(", ")
            for j in color_num:
                num, color = j.split()
                if color == "blue" and int(num) > int(high_blue):
                    high_blue = num
                if color == "green" and int(num) > int(high_green):
                    high_green = num
                if color == "red" and int(num) > int(high_red):
                    high_red = num

        count += int(high_red) * int(high_green) * int(high_blue)

    print(count)

p2_main()
