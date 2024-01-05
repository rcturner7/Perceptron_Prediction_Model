# Perceptron_Prediction_Model
## Introduction to Perceptron:
This application uses the Perceptron Algorithm from Frank Rosenblatt. Frank Rosenblatt invented this program in 1957. He explained that perceptron could be similar to brain neurons. The Perceptron Algorithm is like a 1 layer neuron algorithm.
I incorporated the algorithm into my application to allow a universal input/inputs from the user for the prediction model, using a 1 layer neural network. This is the framework from the Perceptron Algorithm.

# Steps in Application:
 - Prints welcome statements and instruction statements naming the application NeuRyan.
 - Asks user what topic statement of a Yes or No choice for the application to predict if the user is going to say yes or no. For example:
   - Am I going to eat chinese food today when I am also craving other types of food?
 - Then application asks the user to state 5 statements related to the prediction choice that relates to their opinions that might relate to being more likely to say yes or no.
  - # (This simulates how we as humans when we have a choice to make we might normally weight the options in our heads, for example:)
   - Am I going to eat chinese food today when I am also craving other types of food? (This would be the main question of action to decide yes or no)
    - The 5 statements of human thinking:
     -  How long has it been since I have had chinese food?
     -  What else am I craving, and has it been longer since I'v had my other craving?
     -  Will I be more satisfied eating Chinese food?
     -  Will Chinese food help my tummy?
     -  Will I be dissatisfied?
  - The application sets a threshold ( the application is set at 1.5 for the threshold. )
  - Then Asks user to answer yes/no to each of the 5 statements with 0 being false, 1 being true. (These are called the values -- This is the first part of perceptron inputs also called nodes.)
  - Then the application then asks the user to weigh with a rating from each of the 5 node values from 0 or 1 with a rating from 0 - 1. For example: 0, 0.1, 0.2, 0.3, etc... (These are called weights -- This is the second part of the perceptron inputs, also called nodes.)
  - The application then multiplies the inputs value * weight = ?
  - Then adds the sum from all 5 of the statements related to the user's choice to make prediction.
  - Then if the value is greater than 1.5 then the algorithm will predict the user will choose yes to their decision -- or ---
  - else the application will predict the user will say no to their future choice they need to make.
