import numpy as np

f = open('input.txt', 'r')

content = f.read()

content_split = content.split('\n')

opp_hand_dict = {'A': 0,
                 'B': 1,
                 'C': 2}

my_hand_dict = {'X': 0,
                'Y': 1,
                'Z': 2}

def score_round(my_hand, opp_hand):
    this_round = 0
    
    if opp_hand == my_hand:
        this_round += 3
    elif (my_hand+1)%3 == opp_hand:
        this_round += 0
    else:
        this_round += 6

    this_round += my_hand + 1

    return this_round

pts_partA = 0
pts_partB = 0
for line in content_split[:-1]:
    opp_hand = opp_hand_dict[line[0]]
    my_hand = my_hand_dict[line[2]]

    this_round = score_round(my_hand, opp_hand)

    pts_partA += this_round

    # print(line, this_round)

    # part B
    my_hand_strat = my_hand
    if my_hand_strat == 0:
        my_hand = (opp_hand-1+3)%3
    elif my_hand_strat == 1:
        my_hand = opp_hand
    else:
        my_hand = (opp_hand+1)%3
    
    this_round = score_round(my_hand, opp_hand)
    pts_partB += this_round

print(pts_partA)
print(pts_partB)

