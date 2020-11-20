from capitals import states
import random 

random.shuffle(states)
# print(states)


#first functino should introduce game and ask for player input
#on if they want to play, if yes call playgame function if not exit
def game_intro():
    print('Welcome to States and Capitals! The game were we give you the state and you give us the capital')
    user = input('Ready to play? y or n:')
    if(user == 'y'):
        #call playergame function
        play_game()
    else:
        print('exit')



def play_game():
    incorrect_score = 0
    correct_score = 0
    #test states below!!!!!!!!!!!!!!!!!!!!!!!!!!
    # states1 = [{'name': 'Virginia', 'capital': 'Richmond'}, {'name': 'Washington', 'capital': 'Olympia'}, {'name': 'West Virginia', 'capital': 'Charleston'}, {'name': 'Wisconsin', 'capital': 'Madison'}, {'name': 'Wyoming', 'capital': 'Cheyenne'}]
    for i in range(len(states)):
        # print(state[i])
        state = states[i]['name']
        capital = states[i]['capital']
    
        answer = input(f'What is the capital of {state}?:')
        if(answer == capital):
            print(f'Correct, the answer is {capital}')
            correct_score = correct_score + 1
            print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
        else:
            print(f'Incorrect, the answer is {capital}')
            incorrect_score = incorrect_score + 1
            print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
    final_score = correct_score - incorrect_score
    print(f'Total Score:{final_score}')
    print(f'Correct: {correct_score} Incorrect:{incorrect_score}')
    play_again = input('Would you like to play again? y or n:')
    if(play_again == 'y'):
        game_intro()
    else:
        print('Thanks for playing!')


game_intro()
