# Pseudocode
# 1. Ask the user to input a set of numbers
# 2. Evaluate the numbers given by the user
# 3. Check to see if the first and last number of the set is the same 
# 4. If yes return "True" if no return "False"

while True:
    set_input = input("Please input a set of numbers: ")
    if set_input.isdigit():
        set_input = int(set_input)
    else:
        print("Invalid, please input numbers.")
        
        break