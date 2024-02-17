from tkinter import *
from tkinter import ttk
import random

generated_random_number = ''  # to store the generated number and make is accessible to all functions.
turn_count = 1  # to store the game turns.

def generate_number(digit : int, is_no_repeat : bool):
    
    """This function Generates a random number with the desired number of digits, 
    also if the generated number should me repetitive or not.
    
    if is_no_repeat is true, then number with no repeating digit is generated, 
    and if its false then the generated number may have repetitive digits

    Returns:
        string: returns the generated number with desired number of digits.
    """    
    generated_num = ''
    if is_no_repeat:
        
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for i in range(0,digit):
            choice = random.choice(numbers)
            numbers.remove(choice)
            generated_num += '{}'.format(choice)
            
        return generated_num
    
    else:
        
        for _ in range(0,digit):
            num = random.randint(0,9)
            generated_num += '{}'.format(num)
            
        return generated_num


def game_turn_counter():
    
    """Checks the game turn value based on mode's value. if mode is 1 then its easy mode which has 10 turns.
    were as mode 2 and 3, normal mode and hard mode respectively have 15 turns.
    it also sets the game turn label to display the current turn.

    Returns:
        bool: if turn count is 11 or 16. means player have guessed for their 10th and 15th turn. it returns true, else if not 11 or 16, it returns false
    """
    global turn_count
    turn_count += 1
    
    if mode.get() == 1:
        return turn_count == 11
    elif mode.get() > 1:
        return turn_count == 16
    game_turn.set('Current Turn: {}'.format(turn_count)) 
    return False    


def turn_over_enable():
    
    """places the turn over label onto the display when called
    """
    turn_over_label.place(x=300, y=245, width=280, height=50, anchor='center')
    
    
def turn_over_disable():
    
    """disables the turn over label when called
    """
    turn_over_label.place_forget()
    

def win_label_enable():
    
    """places the win label onto the display when called
    """
    win_label.place(x=300, y=245, width=350, height=50, anchor='center')
    
    
def win_label_disable():
    
    """disables the win label when called
    """
    win_label.place_forget()
    
    
def check_guess():
    
    """this function first checks if game turns are available or not by calling game_turn_counter() -> bool, 
    if true, calls turn_over_enable() and returns from the function. if False, the function continues to execute.
    
    the player guess is extracted and stored in guess_made : str, then for each character in guess_made, 
    the for loop checks if the guessed character is in the generated random number : str, if False it feeds to the feedback message and guess result with appropriate values. 
    if true then it checks if the guessed character and generated random number character at the current index are equals or not, then it feeds to the 
    feedback message and guess result with appropriate values.
    
    based on the values in guessed result feedback message is again added with encouraging texts
    """
    
    feedback_message = ''
    guess_result = ''
    guess_made = number_entry.get()
    
    for index in range(len(guess_made)):
        
        if generated_random_number.count(guess_made[index]) > 0:
            if guess_made[index] == generated_random_number[index]:
                feedback_message += '{} is at the correct position.\n'.format(guess_made[index])
                guess_result += 'A'
            else:
                feedback_message += '{} is in the number, but at wrong position.\n'.format(guess_made[index])
                guess_result += 'B'                
        else:
            feedback_message += '{} is not in the number.\n'.format(guess_made[index])
            guess_result += 'C'
            
    if guess_result.count('A') == len(guess_made):
        feedback_message += '\nYou have guessed the number correctly!!'
        win_label_enable()
        
    elif guess_result.count('A') < len(generated_random_number) and guess_result.count('A') >= (len(generated_random_number)-1):
        feedback_message += '\nYou just have one more digit left to guess correctly!'
    elif guess_result.__contains__('B') and guess_result.__contains__('A') == False:
        feedback_message += '\nYou have guessed the digits correctly...well not in the correct order though!!'
    elif guess_result.__contains__('C') and guess_result.__contains__('B') == False:
        feedback_message += '\nKeep trying you!!!'
        
    feedback.set(feedback_message)
    if game_turn_counter() == True:
        turn_over_enable()    
        

def disable_start_page():
    
    """disables the following frames and button in start page
    -title_frame, details_frame, difficulty_frame, start_button 
    """
    title_frame.place_forget()
    details_frame.place_forget()
    difficulty_frame.place_forget()
    start_button.place_forget()
    

def enable_start_page():
    
    """enables the start page by placing the following frames and button after calling turn_over_disable() and disable_game_page()
    -title_frame, details_frame, difficulty_frame, start_button
    """
    turn_over_disable()
    win_label_disable()
    disable_game_page()
    
    title_frame.place(x=300, y=40, anchor='n')
    details_frame.place(x=300, y=100, width=550, height=165, anchor='n')
    difficulty_frame.place(x=300, y=285, anchor='n')
    start_button.place(relx=0.5, y=350, anchor='center')

def disable_game_page():
    
    """disables the game page by forgetting the gamepage_frame
    """
    gamepage_frame.pack_forget()
    

def enable_game_page():
    
    """enables the game page calling the generate_random_number() function based on the mode value
    - mode = 1 = easy mode
    - mode = 2 = normal mode
    - mode = 3 = hard mode
    
    then disables the start page by calling disable_start_page().
    cleans the guess number entry and feedback label and places gamepage_frame
    """
    global generated_random_number
    global turn_count
    turn_count = 1
    game_turn.set('Current Turn: 1')
    if mode.get() == 1:
        generated_random_number = generate_number(3, False)
        
    elif mode.get() == 2:
        generated_random_number = generate_number(3, True)
        
    elif mode.get() == 3:
        generated_random_number = generate_number(4, True)
        
    disable_start_page()
    number_entry.delete(0,END)
    feedback.set('Your guess result will be shown here.')
    gamepage_frame.pack(expand=True, fill='both')
    
window = Tk()
w_width = 600
w_height = 400
w_bg_color='#ffffff'  # color for background of the application
x = int((window.winfo_screenwidth()/2) - (w_width/2))
y = int((window.winfo_screenheight()/2) - (w_height/2))
window.geometry(f'{w_width}x{w_height}+{x}+{y}')
window.config(background=w_bg_color)
window.title('Guessing Number')

# Welcome label
title_frame = ttk.Frame(window)
welcome_label = ttk.Label(title_frame, text="LET'S GUESS THE NUMBER", font=('arial', 25, 'bold'), anchor='center', background=w_bg_color)
welcome_label.pack()
#title_frame.place(x=300, y=40, anchor='n')


'''difficulty selection'''
# difficulty details
details_frame = ttk.Frame(window)
details_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')
details_frame.columnconfigure(0, weight=1, uniform='a')
'''for background color of start page'''
ttk.Label(details_frame, background=w_bg_color).grid(row=0, column=0, rowspan=6, sticky='news')

# Easy mode definition
ttk.Label(details_frame, text='Easy Mode', font=('arial', 12, 'bold'), background=w_bg_color).grid(row=0, column=0, sticky='s')
ttk.Label(details_frame, text='3-digit number which may have repeated digits - 10 Tries to guess the number.', font=('arial', 11), background=w_bg_color).grid(row=1, column=0, sticky='n')

# Normal mode definition
ttk.Label(details_frame, text='Normal Mode', font=('arial', 12, 'bold'), background=w_bg_color).grid(row=2, column=0, sticky='s')
ttk.Label(details_frame, text='3-digit number with no repeated digits - 15 Tries to guess the number.', font=('arial', 11), background=w_bg_color).grid(row=3, column=0, sticky='n')

# Hard mode definition
ttk.Label(details_frame, text='Hard Mode', font=('arial', 12, 'bold'), background=w_bg_color).grid(row=4, column=0, sticky='s')
ttk.Label(details_frame, text='4-digit number with no repeated digits - 15 Tries to guess the number.', font=('arial', 11), background=w_bg_color).grid(row=5, column=0, sticky='n')

'''RadioButtons for selection of difficulty mode'''
mode = IntVar(value=1)
difficulty_frame = ttk.Frame(window)
# easy mode
easy_mode = ttk.Radiobutton(difficulty_frame, text='Easy mode', width=20,
                            variable=mode,
                            value=1)
easy_mode.pack(side='left')

# normal mode
normal_mode = ttk.Radiobutton(difficulty_frame, text='Normal mode', width=20,
                            variable=mode,
                            value=2)
normal_mode.pack(side='left')

# Hard mode
hard_mode = ttk.Radiobutton(difficulty_frame, text='Hard mode',
                            variable=mode,
                            value=3)
hard_mode.pack(side='left')

# start button
start_button = ttk.Button(window, text='Start', padding=5, width=15, command=enable_game_page)

'''Game page section '''
# game page
gamepage_frame = Frame(window)
gamepage_frame.columnconfigure((0, 1, 2), weight=1, uniform='b')
gamepage_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='b')
'''for background color of game page'''
ttk.Label(gamepage_frame, background=w_bg_color).grid(row=0, column=0, rowspan=6, columnspan=3, sticky='news')

# game turn label
game_turn = StringVar(value='Current Turn: ')
turn_label = ttk.Label(gamepage_frame, textvariable=game_turn, font=('arial', 12, 'bold'), background=w_bg_color)
turn_label.grid(row=0, column=0, sticky='s')
turn_over_label = ttk.Label(window, text='Your turns are over!', font=('arial', 22), background='#cc5c29', anchor='center')

# back button
back_button = ttk.Button(gamepage_frame, text='Back', padding=2.5, width=10, command=enable_start_page)
back_button.grid(row=0, column=2, sticky='s')

# number entry box    
ttk.Label(gamepage_frame, text='Enter your guess here.', font=('arial', 12), background=w_bg_color).grid(row=1, column=1)
def digit_validate(value):
    ''' this checks the length of the entry input to allow only the desired number of digits to be types'''
    if mode.get()<=2:
        return len(value) <= 3
    elif mode.get() == 3:
        return len(value) <= 4
validation = window.register(digit_validate)  # registering the validation function
number_entry = ttk.Entry(gamepage_frame, font=('arial', 20, 'bold'), width=4, justify='center', validate='key', validatecommand=(validation, '%P'))
number_entry.grid(row=2, column=1, rowspan=1, sticky='news')

submit_button = ttk.Button(gamepage_frame, text='Submit', padding=5, width=15, command=check_guess)
submit_button.grid(row=3, column=1, rowspan=1, sticky='s')

feedback = StringVar(value='Your guess result will be shown here.')
feedback_label = ttk.Label(gamepage_frame, textvariable=feedback, font=('arial', 12), background=w_bg_color, anchor='center')
feedback_label.grid(row=4, column=0, rowspan=2, columnspan=3, sticky='ns')

'''win label'''
win_label = ttk.Label(window, text='Correct Guess! You Won!', font=('arial', 22), background='#3bed32', anchor='center')

'''calling enable_start_page() to display the start page'''
enable_start_page()

window.mainloop() 