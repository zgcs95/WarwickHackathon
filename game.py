def game():
    beginning = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
    player1 = []
    print("Player1, please enter your sets, 0 means clubs and 1 means spades")
    for i in range(5):
        element = []
        print("enter your", int(i+1), "set")
        for j in range(5):
            print("Pick one card")
            print("Your available cards:", beginning, "The first list is spade and the second is club")
            print("Pick spade or club first and type the number")
            colour = int(input())
            number = int(input())
            beginning[colour].remove(number)
            small_element = []
            small_element.append(colour)
            small_element.append(number)
            element.append(small_element)
        player1.append(element)
    print(player1)
    beginning = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
    player2 = []
    print("Player2, please enter your sets, 0 means diamonds and 1 means hearts")
    for i in range(5):
        element = []
        print("enter your", int(i + 1), "set")
        for j in range(5):
            print("Pick one card")
            print("Your available cards:", beginning, "The first list is heart and the second is diamond")
            colour = int(input())
            number = int(input())
            beginning[colour].remove(number)
            small_element = []
            small_element.append(colour)
            small_element.append(number)
            element.append(small_element)
        player2.append(element)
    print(player2)

    def render(thing):
        def check_best(test):
            for i in range(10, 14):
                count = 0
                for j in range(len(test)):
                    if i == test[j][1]:
                        count = count + 1
                    else:
                        pass
                if count != 1:
                    return False
                else:
                    pass
            count_one = 0
            for z in range(len(test)):
                if test[z][1] == 1:
                    count_one = count_one + 1
                else:
                    pass
            if count_one != 1:
                return False

            count0 = 0
            count1 = 0
            for i in range(len(test)):
                if test[i][0] == 0:
                    count0 = count0 + 1
                elif test[i][0] == 1:
                    count1 = count1 + 1
                else:
                    pass
            if count0 != 5 and count1 != 5:
                return False
            else:
                pass
            return True

        def straight_flush(test):
            count0 = 0
            count1 = 0
            for i in range(len(test)):
                if test[i][0] == 0:
                    count0 = count0 + 1
                elif test[i][0] == 1:
                    count1 = count1 + 1
                else:
                    pass
            if count0 != 5 and count1 != 5:
                return None
            else:
                pass

            def finding(test2):
                result = 13
                for a in range(len(test2)):
                    if result > test2[a][1]:
                        result = test2[a][1]
                    else:
                        pass
                return result

            min_num = finding(test)
            print(min_num)
            for b in range(min_num, min_num+5):
                count = 0
                for c in range(len(test)):
                    if test[c][1] == b:
                        count = count + 1
                    else:
                        pass
                if count == 0:
                    return None
                else:
                    pass
            return True

        def check_same_colour(test):
            count0 = 0
            count1 = 0
            for i in range(len(test)):
                if test[i][0] == 0:
                    count0 = count0 + 1
                elif test[i][0] == 1:
                    count1 = count1 + 1
                else:
                    pass
            if count0 != 5 and count1 != 5:
                return False
            else:
                pass
            return True

        def check_straight(test):
            def finding(test2):
                result = 13
                for a in range(len(test2)):
                    if result > test2[a][1]:
                        result = test2[a][1]
                    else:
                        pass
                return result

            min_num = finding(test)
            for b in range(min_num, min_num + 5):
                count = 0
                for c in range(len(test)):
                    if test[c][1] == b:
                        count = count + 1
                    else:
                        pass
                if count == 0:
                    return False
                else:
                    pass
            return True

        def check_twopairs(test):
            total = 0
            for i in range(1, 14):
                count = 0
                for j in range(len(test)):
                    if test[j][1] == i:
                        count = count + 1
                    else:
                        pass
                if count == 2:
                    total = total + 1
                else:
                    pass
            if total == 2:
                return True
            else:
                return False

        def check_onepair(test):
            total = 0
            for i in range(1, 14):
                count = 0
                for j in range(len(test)):
                    if test[j][1] == i:
                        count = count + 1
                    else:
                        pass
                if count == 2:
                    total = total + 1
                else:
                    pass
            if total == 1:
                return True
            else:
                return False

        if check_best(thing) == True:
            return 6
        elif straight_flush(thing) == True:
            return 5
        elif check_same_colour(thing) == True:
            return 4
        elif check_straight(thing) == True:
            return 3
        elif check_twopairs(thing) == True:
            return 2
        elif check_onepair(thing) == True:
            return 1
        else:
            return 0
    rendered1 = []

    for x in range(len(player1)):
        rendered1.append(render(player1[x]))
    print(rendered1)
    rendered2 = []
    for x in range(len(player2)):
        rendered2.append(render(player2[x]))
    print(rendered2)

    score1 = 0
    score2 = 0
    set1 = [1, 2, 3, 4, 5]
    set2 = [1, 2, 3, 4, 5]
    guessing1 = ["unknown", "unknown", "unknown", "unknown", "unknown"]
    guessing2 = ["unknown", "unknown", "unknown", "unknown", "unknown"]
    print("it is player 1 turn")#1
    print("You can choose one card to unveil")
    unveil11 = input()
    unveil12 = input()
    guessing1[int(unveil11)-1] = player2[int(unveil11)-1][int(unveil12)-1]
    print(guessing1)
    print("pick your set")
    print(set1)
    pick_mine1 = input()
    set1.remove(int(pick_mine1))
    print("pick your opponent set")
    print(set2)
    pick_opp1 = input()
    set2.remove(int(pick_opp1))
    guessing1[int(pick_opp1)-1] = player2[int(pick_opp1)-1]
    guessing2[int(pick_mine1)-1] = player1[int(pick_mine1)-1]
    if render(player1[int(pick_mine1)-1]) > render(player2[int(pick_opp1)-1]):
        score1 = score1 + 1
    elif render(player1[int(pick_mine1)-1]) < render(player2[int(pick_opp1)-1]):
        score2 = score2 + 1
    else:
        pass
    print("it is player 2 turn")#2
    print("You can choose one card to unveil")
    unveil21 = input()
    unveil22 = input()
    guessing2[int(unveil21) - 1] = player2[int(unveil21) - 1][int(unveil22) - 1]
    print(guessing2)
    print("pick your set")
    print(set2)
    pick_mine2 = input()
    set2.remove(int(pick_mine2))
    print("pick your opponent set")
    print(set1)
    pick_opp2 = input()
    set1.remove(int(pick_opp2))
    guessing2[int(pick_opp2)-1] = player1[int(pick_opp2)-1]
    guessing1[int(pick_mine2)-1] = player2[int(pick_mine2)-1]
    if render(player1[int(pick_opp2)-1]) > render(player2[int(pick_mine2)-1]):
        score1 = score1 + 1
    elif render(player1[int(pick_opp2)-1]) < render(player2[int(pick_mine2)-1]):
        score2 = score2 + 1
    else:
        pass
    print("it is player 1 turn") #3
    print("You can choose one card to unveil")
    unveil31 = input()
    unveil32 = input()
    guessing1[int(unveil31) - 1] = player2[int(unveil31) - 1][int(unveil32) - 1]
    print(guessing1)
    print("pick your set")
    print(set1)
    pick_mine3 = input()
    set1.remove(int(pick_mine3))
    print("pick your opponent set")
    print(set2)
    pick_opp3 = input()
    set2.remove(int(pick_opp3))
    guessing1[int(pick_opp3) - 1] = player2[int(pick_opp3) - 1]
    guessing2[int(pick_mine3) - 1] = player1[int(pick_mine3) - 1]
    if render(player1[int(pick_mine3)-1]) > render(player2[int(pick_opp3)-1]):
        score1 = score1 + 1
    elif render(player1[int(pick_mine3)-1]) < render(player2[int(pick_opp3)-1]):
        score2 = score2 + 1
    else:
        pass
    print("it is player 2 turn")  # 4
    print("You can choose one card to unveil")
    unveil41 = input()
    unveil42 = input()
    guessing2[int(unveil41) - 1] = player2[int(unveil41) - 1][int(unveil42) - 1]
    print(guessing2)
    print("pick your set")
    print(set2)
    pick_mine4 = input()
    set2.remove(int(pick_mine4))
    print("pick your oppenent set")
    print(set1)
    pick_opp4 = input()
    set1.remove(int(pick_opp4))
    if render(player1[int(pick_opp4)-1]) > render(player2[int(pick_mine4)-1]):
        score1 = score1 + 1
    elif render(player1[int(pick_opp4)-1]) < render(player2[int(pick_mine4)-1]):
        score2 = score2 + 1
    else:
        pass

    if render(player1[0]) > render(player2[0]):
        score1 = score1 + 1
    elif render(player1[0]) < render(player2[0]):
        score2 = score2 + 1
    else:
        pass
    print(score1)
    print(score2)
    if score1 > score2:
        print("player1 won")
    elif score1 < score2:
        print("player2 won")
    else:
        print("tie")



game()

