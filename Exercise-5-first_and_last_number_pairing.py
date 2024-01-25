# Pseudocode
# 1. Ask the user to input a set of numbers
# 2. Evaluate the numbers given by the user
# 3. Check to see if the first and last number of the set is the same 
# 4. If yes return "True" if no return "False"

def firstval_lastval_isequal(number_set):
    print("Given list: ", number_set)

    first_val = number_set[0]
    last_val = number_set[-1]

    if first_val == last_val:
        return True
    else:
        return False
    
