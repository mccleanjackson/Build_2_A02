"""
Jackson McClean
IS 303 - A02
Color Mixer
This program explains to users what color a user will get when mixing two primary colors together. Invalid colors will be rejected. 


Inputs: 
-Are you mixing normal paint or spray paint?
-2 colors (string)
-primary colors: Red, Blue, Yellow
-Possible outcomes: Green, Purple, Orange

Process:
- Ask what type of paint they are mixing. If spray paint, tell them thats a terrible idea.
- Ask for what two colors they are using, find what color they make

Outputs:
- Display what color someone will get if they mix primary colors
- Display an error message if they put in an incorrect color 

"""
question = "Are you mixing normal paint or spray paint? "
decision_bad = "You arent Picasso, dont try to mix spray paint. "
decision_good = "What primary colors are you using? "

decision = input(question)
decision = decision.lower()
mix_colors = False


#Inputs for what they are mixing

if decision == "spray paint" or decision == "spray":
    print(f"You arent Picasso, dont try to mix spray paint. ")
elif decision == "normal paint" or decision == "normal":
    colors = input(decision_good)
    colors = colors.lower()
    colors = colors.replace(" + ", " and ")
    colors = colors.replace(" & ", " and ")

#Process
#Outputs
    if colors == "red and blue" or colors == "blue and red":
        print(f"Mixing red and blue will give you purple! ")
    elif colors == "red and yellow" or colors == "yellow and red":
        print(f"Mixing red and yellow will give you orange! ")
    elif colors == "blue and yellow" or colors == "yellow and blue":
        print(f"Mixing blue and yellow will give you green! ")
    else:
        print("I can only tell you color outcomes of mixing primary colors: Red, Blue, or Yellow. ")
else:
    print("You should only be mixing normal paint. Head to Home Depot. ")