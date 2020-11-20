from capitals import states
import random 

# random.shuffle(states)
# # print(states)
# #game being called
# def game_intro():
#     print('Welcome to States and Capitals! The game were we give you the state and you give us the capital')
#     user = input('Ready to play? y or n:')
#     if(user == 'y'):
#         play_game()
#     else:
#         print('exit')



# def play_game():
#     incorrect_score = 0
#     correct_score = 0
#     #test states below!!!!!!!!!!!!!!!!!!!!!!!!!!
#     # states1 = [{'name': 'Virginia', 'capital': 'Richmond'}, {'name': 'Washington', 'capital': 'Olympia'}, {'name': 'West Virginia', 'capital': 'Charleston'}, {'name': 'Wisconsin', 'capital': 'Madison'}, {'name': 'Wyoming', 'capital': 'Cheyenne'}]
#     for i in range(len(states)):
#         # print(state[i])
#         state = states[i]['name']
#         capital = states[i]['capital']
    
#         answer = input(f'What is the capital of {state}?:')
#         if(answer == capital):
#             print(f'Correct, the answer is {capital}')
#             correct_score = correct_score + 1
#             print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
#         else:
#             print(f'Incorrect, the answer is {capital}')
#             incorrect_score = incorrect_score + 1
#             print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
#     final_score = correct_score - incorrect_score
#     print(f'Total Score:{final_score}')
#     print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
#     play_again = input('Would you like to play again? y or n:')
#     if(play_again == 'y'):
#         game_intro()
#     else:
#         print('Thanks for playing!')


# game_intro()

###bonuses#####################################


random.shuffle(states)
# print(states)
#game being called
def game_intro():
    print('Welcome to States and Capitals! The game were we give you the state and you give us the capital')
    user = input('Ready to play? y or n:')
    if(user == 'y'):
        play_game()
    else:
        print('exit')



def play_game():
    incorrect_score = 0
    correct_score = 0
    print(states)
    #test states below!
    # states1 = [{'name': 'Virginia', 'capital': 'Richmond'}, {'name': 'Washington', 'capital': 'Olympia'}, {'name': 'West Virginia', 'capital': 'Charleston'}, {'name': 'Wisconsin', 'capital': 'Madison'}, {'name': 'Wyoming', 'capital': 'Cheyenne'}]
    for i in range(len(states)):
        # print(states1)
        state = states[i]['name']
        capital = states[i]['capital']
    
        answer = input(f'What is the capital of {state}?:')
        if(answer == capital):
            print(f'Correct, the answer is {capital}')
            correct_score = correct_score + 1
            print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
            #trying to make new key
            if 'Correct' in states[i].keys():   
                states[i]['Correct'] += 1
                print(states[i])
            else:
                states[i]['Correct'] = states[i].get('Correct', 0) +1
                print(states[i])
        else:
            print(f'Incorrect, the answer is {capital}')
            incorrect_score = incorrect_score + 1
            print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
            if 'Incorrect' in states[i].keys():   
                states[i]['Incorrect'] += 1
                print(states[i])
            else:
                states[i]['Incorrect'] = states[i].get('Incorrect', 0) +1
                print(states[i])

    final_score = correct_score - incorrect_score
    print(f'Total Score:{final_score}')
    print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
    play_again = input('Would you like to play again? y or n:')
    if(play_again == 'y'):
        game_intro()
    else:
        print('Thanks for playing!')
    return states

# def key_incrementor(state):
#     print(state)
#     # state['Correct'] 

states = play_game()
game_intro()
