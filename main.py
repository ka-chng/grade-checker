while True: # loop
    score = float(input("Enter a score between 0.0 and 1.0 ")) # create the input variable which is used to take data from the user
    if score < 0.0 or score > 1.0: # this checks for errors
        print("Error: Score is out of range") # prints the error if an error is detected
    elif score >= 0.9: # if the score is equal to or greater than 0.9 print the grade which is "A"
        print("Grade: A") # printing the grade
    elif score >= 0.8: # if the score is equal to or greater than 0.8 print the grade which is "B"
        print("Grade: B") # printing the grade
    elif score >= 0.7: # if the score is equal to or greater than 0.7 print the grade which is "C"
        print("Grade: C") # printing the grade
    elif score >= 0.6: # if the score is equal to or greater than 0.6 print the grade which is "D"
        print("Grade: D") # printing the grade
    else:
        print("Grade: F") # prints the grade is "F" if its less than all the other values supplied
