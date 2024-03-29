# Pseudocode
# 1. Ask the user to input a set of numbers
# 2. Evaluate the numbers given by the user
# 3. Check to see if the first and last number of the set is the same 
# 4. If yes return "True" if no return "False"

# Defining the function for comparing the first and last values
def firstval_lastval_isequal(number_set):
    print("Given list: ", number_set)

# Marking which values we want to compare
    first_val = number_set[0]
    last_val = number_set[-1]

# Returning the answer depending on the set analyzation
    if first_val == last_val:
        return True
    else:
        return False

# Sample number set
number_set_a = [12, 13, 0, 4]
print("Are the values equal? ", firstval_lastval_isequal(number_set_a))

number_set_b = [5, 9, 0, 5]
print("Are the values equal? ", firstval_lastval_isequal(number_set_b))