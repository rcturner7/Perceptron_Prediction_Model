# A 1 layer perceptron prediction model

# Welcome and instruction statements by the perceptron bot
print("Welcome, my name is Neuryan. I am a single neuron, at your service.\n")
print("I would like to predict what you might choose based on 5 inputs of statements,\n& rate these statements from 0 "
      "to 1.\nThis means 0 is less likely to 1 being the most likely.\nBe sure to use decimals if higher then 0, "
      "but less than 1.\nFor example: 0.1, 0.2, 0.3, etc....\n")

# The Perceptron Algorithm
# Frank Rosenblatt suggested this algorithm: (1957)
# 1. Set a threshold value
# 2. Multiply all inputs with its weights
# 3. Sum all the results
# 4. Activate the output

# Asking the user what to predict
choice_title_prediction = input("What choice would you like me to predict if you might choose yes or no to a topic?\n")

# Getting user's statements to rate
user_data_statements1 = input("State your first statement or question to rate based on what you want me to predict.\n")
user_data_statements2 = input("State your second statement or question to rate based on what you want me to predict.\n")
user_data_statements3 = input("State your third statement or question to rate based on what you want me to predict.\n")
user_data_statements4 = input("State your fourth statement or question to rate based on what you want me to predict.\n")
user_data_statements5 = input("State your fifth statement or question to rate based on what you want me to predict.\n")

# Threshold value
threshold_value = 1.5

# True or false of the user's opinion to each statement - 0 being false, and 1 being true -- These are the node values:
user_true_false_statement1 = int(input("Is your first statement True or False based on your feelings? "
                                       "0 being false, and 1 being True.\n"))
user_true_false_statement2 = int(input("Is your second statement True or False based on your feelings? "
                                       "0 being false, and 1 being True.\n"))
user_true_false_statement3 = int(input("Is your third statement True or False based on your feelings? "
                                       "0 being false, and 1 being True.\n"))
user_true_false_statement4 = int(input("Is your fourth statement True or False based on your feelings? "
                                       "0 being false, and 1 being True.\n"))
user_true_false_statement5 = int(input("Is your fifth statement True or False based on your feelings? "
                                       "0 being false, and 1 being True.\n"))

# User rating each of their statements node values -- These are the node weights:
user_rating_statement1 = float(input("Rate your first statement from 0 to 1, for example: 0, 0.1, 0.2, etc.. to 1.\n"))
user_rating_statement2 = float(input("Rate your second statement from 0 to 1.\n"))
user_rating_statement3 = float(input("Rate your third statement from 0 to 1.\n"))
user_rating_statement4 = float(input("Rate your fourth statement from 0 to 1.\n"))
user_rating_statement5 = float(input("Rate your fifth statement from 0 to 1.\n"))

# Multiplying rating inputs with the weights v1 * w1 = ?
user_rating_calculation1 = user_true_false_statement1 * user_rating_statement1
user_rating_calculation2 = user_true_false_statement2 * user_rating_statement2
user_rating_calculation3 = user_true_false_statement3 * user_rating_statement3
user_rating_calculation4 = user_true_false_statement4 * user_rating_statement4
user_rating_calculation5 = user_true_false_statement5 * user_rating_statement5

# Sum all the results
sum_results = user_rating_calculation1 + user_rating_calculation2 + user_rating_calculation3 + \
              user_rating_calculation4 + user_rating_calculation5

# making the prediction
if float(sum_results) > threshold_value:
      print(f"My prediction of {choice_title_prediction} you will most likely choose YES.\n")
else:
      print(f"My prediction of {choice_title_prediction} is your answer will most likely be NO.\n")
