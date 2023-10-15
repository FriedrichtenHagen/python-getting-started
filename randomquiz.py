
import random
import os
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

header = 'Please write down the matching capital to each state. \n \n'
answer_letters = ['A', 'B', 'C', 'D']

def createTests():
    for i in range(3):
        only_states = list(capitals.keys())
        random.shuffle(only_states)
        only_capitals = list(capitals.values())
        random.shuffle(only_capitals)

        # write test
        test = open(f'/Users/friedrichtenhagen/coding/python-getting-started/tests/test{i}.txt', 'w')   
        test.write(header)
        for state in only_states:
            test.write(f'What is the capital of {state}? ')
            test.write('\n')

            # get 1 right answer
            right_answer = capitals[f'{state}']
            # and 3 wrong answers
            capitals_right_answer_removed = only_capitals.copy()
            del capitals_right_answer_removed[capitals_right_answer_removed.index(right_answer)]
            wrong_answers = random.sample(capitals_right_answer_removed, 3)
            # sum all 4 answers
            four_answers = [right_answer] + wrong_answers
            random.shuffle(four_answers)

            for f in range(4):
                test.write(f'{answer_letters[f]}: {four_answers[f]}')
                test.write('\n')
            test.write('\n')
        test.close()


createTests()