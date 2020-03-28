"""
KEYBOARD ASSEMBLY

A malicious prankster has disassembled all of UQCS's keyboards and stolen some keys!

The committee needs to reassemble as much of a keyboard as possible, using the remaining keys.

Given a list of letters A-Z, print an ASCII QWERTY keyboard using only those letters and spaces 
for missing keys. For example, if we had all the letters the keyboard would be this:

Q W E R T Y U I O P
 A S D F G H J K L
  Z X C V B N M

Input Format:
- The first line is , the number of keys available.
- The next  lines are the available letters, from A-Z.

Constraints: A particular letter can appear at most once.

Output Format: An ASCII keyboard in this layout, with spaces for missing keys.

Q W E R T Y U I O P
 A S D F G H J K L
  Z X C V B N M

Sample Input: 5, [P, X, R, F, S]

Sample Output:
      R           P
   S   F          
    X          
Note that there is trailing whitespace on the second and third lines.
"""
# Complete the 'draw_keyboard' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER num_letters
#  2. CHARACTER_ARRAY letters

def replace_missing(keyboard, letters):
    # Create array of a new keyboard line
    new_keyboard = ["  "]*len(keyboard)

    # Check actual keyboard line for letters
    for char in keyboard:
        for letter in letters:
            if letter == char:
                # Put letter in new line at same index as actual line with space         
                new_keyboard[keyboard.index(char)] = letter + " "    
    
    # Convert keyboard line array to string 
    new_keyboard_string = ''.join(new_keyboard)
    return new_keyboard_string


def draw_keyboard(num_letters, letters):
    # Array for each line of actual keyboard
    keyboard_1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
    keyboard_2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ]
    keyboard_3 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']

    # Create new lines of keyboard with only letters
    new_keyboard_1 = replace_missing(keyboard_1, letters)
    new_keyboard_2 = replace_missing(keyboard_2, letters)
    new_keyboard_3 = replace_missing(keyboard_3, letters)
    
    # Add all the lines together with spacing
    # 2nd line has 1 space before and 1 space after
    # 3rd line has 2 space before and 4 spaces after    
    new_keyboard_final = f'{new_keyboard_1}\n' \
        + f' {new_keyboard_2} \n' \ 
        + f'  {new_keyboard_3}    \n'

    return(new_keyboard_final)

# Example 
keyboard_example = draw_keyboard(5, ['P', 'X', 'R', 'F', 'S'])
print(keyboard_example)