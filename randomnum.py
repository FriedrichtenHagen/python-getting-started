'''
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.
'''

import random 

def random_list():
    result_list = []
    for i in range(100): 
        result_list.append(random.randint(0, 1))
    return result_list

def check_for_streak(list):
    num_of_streaks = 0
    streak_list = []
    for index, item in enumerate(list):
        # check if streak has reached 6
        if len(streak_list) == 6:
            num_of_streaks += 1
            streak_list = []
        else:
            # if streak list is empty
            if not streak_list:
                # streak_list is empty
                streak_list.append(item)
            else:
                # streak continues
                if item in streak_list:
                    streak_list.append(item)
                # streak is broken
                else:
                    streak_list = []
    return num_of_streaks


def sample_ten_thousand():
    list_with_min_one_streak = 0
    for i in range(10000):
        ranlist = random_list()
        streak_number = check_for_streak(ranlist)
        if streak_number:
            list_with_min_one_streak += 1
    print(f'{list_with_min_one_streak} lists with min. one streak of 6 of one kind in a row in 10.000 ')


sample_ten_thousand()