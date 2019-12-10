# +++ creating methods that will be ued in the program +++

# This method will be used as a main menu for the porgram
def main_maenu():
    # putting everything in a while loop that will run untill the user enters a vaild input
    while (True):

        # printing out the title so the user knows what menu they are in
        title_text = "Main Menu"
        print(title_text.center(40, '='))

        # asking the user to pick a menu
        print()
        print("         please pick a menu to use")
        print()
        print("(A) Add Participants     (D) Award Points")
        print("(B) View Participants    (E) view Scores")
        print("(C) Name Events          (Q) Quit")

        # getting the user input
        print()
        user_input = input("Enter Menu: ")

        # cheking user input and sending them to the correct menu/ending the program

        # cheking what the user has enterd
        if user_input.lower() == 'a':
            print()
            # calling the correct function
            add_entries()
            print()

        elif user_input.lower() == 'b':
            print()
            view_entries()
            print()

        elif user_input.lower() == 'c':
            print()
            naming_events()
            print()

        elif user_input.lower() == 'd':
            print()
            awarding_points()
            print()

        elif user_input.lower() == 'e':
            print()
            print_out_socres()
            print()

        # if the user enters in e then the main loop will break and end the program
        elif user_input.lower() == 'q':
            break;

        # if the user does not enter in one of the options they will get an error
        else:
            print()
            print("INVALID INPUT")
            print()


# this method will be used to add in values to the arrays that hold the entries
def add_entries():
    # printing out the title so the user knows what menu they are in
    title_text = "Add Participants"
    print(title_text.center(40, '='))

    # this bool will be used as the while loops condition
    # as long as it is true the loop will run
    keep_adding_participants = True

    while keep_adding_participants:

        # while loop will run un till the user enters in a valid input
        while True:
            # asking the user to choose if they are going to add in a
            # solo or team participant
            print("Please pick if this is a team or solo entire:")
            print("(A) Solo")
            print("(B) Team")

            # getting the input from the user
            users_input = input("")
            print()  # adding in blank print statements to make the program more readable

            # braking out of the loop if the users input is a or b
            if users_input.lower() == 'a' or users_input.lower() == 'b':
                break
            else:
                # printing out error message if the user has entered an i valid input
                print("INVALID INPUT")
                print()

        # Entering the correct if statements depending on the users input
        # if the user picks to enter a Solo entire this if statements will run
        if users_input == 'a':

            while True:
                # asking the user to enter in the name of the Participant
                participants_name = input("Please enter in the name of the participants: ")

                # checking to see if the user has only entered in letters for the participants name
                if not participants_name.isalpha():
                    print()
                    print("INVALID INPUT")
                    print("A participants name can only contain letters")
                    print()
                else:
                    # if only letters have been used the loop will break
                    break

            # adding the participants name to the solo_entire array
            solo_entries.append(participants_name)

        # if the user picks to enter in a Team entire this statements will run
        elif users_input == 'b':

            # creating a temporary array to hold the team name an participants name
            temp_team_array = []

            # asking the user for the team name
            team_name = input("Please enter in the name of the team: ")
            # adding in the team name to the first index location of the temp array
            temp_team_array.append(team_name)

            # creating a for loop that will run 5 times so all
            # members of the team can be added
            for i in range(5):

                while True:
                    # asking the user for the name of the team member
                    team_member_name = input("Please enter in the name of the team member " + str(i + 1) + " : ")

                    # checking to see if the user has only entered in letters for the participants name
                    if not team_member_name.isalpha():
                        print()
                        print("INVALID INPUT")
                        print("A participants name can only contain letters")
                        print()
                    else:
                        # if only letters have been used the loop will break
                        break

                # adding the team member to the temp array
                temp_team_array.append(team_member_name)

            # finally the temp array will be added in to team_enties array
            # this will make team entries in to a 2D array
            team_entries.append(temp_team_array)

        # asking the user if they want to enter in a new participants
        print()

        while True:
            add_more_participants = input("Would you like to enter in a new participant \n(Y) Yes \n(N) No\n")
            print()

            # if the user chooses no then the value of keep_adding_participants will be set to false
            # this will cause the while loop to stop running
            if add_more_participants.lower() == 'n':
                keep_adding_participants = False
                break
            elif add_more_participants.lower() == 'y':
                keep_adding_participants = True
                break
            else:
                print("INVALID INPUT")
                print()


# method will print out all of the names of the entries inside of the arrays
def view_entries():
    # printing out the name of the menu
    print()
    text = "VIEW ENTRIES"
    print(text.center(40, "="))
    print()

    # printing out the names of the solo entries array
    print("Solo Entries")
    index = 1
    for names in solo_entries:
        print(str(index).ljust(10, ".") + names)
        index += 1

    print()
    print()

    index = 1
    print("Team Entries")
    # printing out the names in the team arrays
    # first for loop is to get the individual team arrays
    for teams in team_entries:
        print()
        # bool will be used to print out extra text for the team name
        name_of_team = True

        # second for loop is for getting the items out of each array
        for names in teams:
            # if it is the first item in the array it will be the team name
            if name_of_team:
                print(str(index).ljust(10, ".") + names)
                index += 1
                name_of_team = False
            else:
                print(names)

    # asking the user to press a key to go back to the main menu
    print("Press any key to leave menu")
    input()


# method for naming the events
def naming_events():
    # printing out the title so the user knows what menu they are in
    title_text = "Name Events"
    print(title_text.center(40, '='))

    # making sure the array that holds the names is all ways empty at the start of the method
    event_names.clear()

    # creating a for loop that will run 5 times
    # so the user can add in all of the names of the events
    for i in range(5):
        # asking the user for the name of the event
        name_of_event = input("please enter in the name of event number " + str(i + 1) + " : ")
        # adding in the name of the event to the array
        event_names.append(name_of_event)


# method for awarding the points
def awarding_points():

    # making sure that all of the entries have been entered in to the 
    if len(event_names) == 0:
        print()
        print("You must enter in the name of the events first")
        print()
        return
    if len(solo_entries) == 0 or len(team_entries) == 0:
        print()
        print("You must enter in the partcipants first")
        print()
        return
    
    # printing out the title so the user knows what menu they are in
    title_text = "Awarding Points"
    print(title_text.center(40, '='))

    # while loop will run until the user gives a valid input
    while True:
        print()
        # asking the user what event they would like to give points for
        index = 1
        for names in event_names:
            print(str(index).ljust(10, ".") + names)
            index += 1

        print()
        user_input = input("Please enter what event you would like to give Points for: ")
        if user_input == "1":
            event_picked = event_names[0]
            break
        elif user_input == "2":
            event_picked = event_names[1]
            break
        elif user_input == "3":
            event_picked = event_names[2]
            break
        elif user_input == "4":
            event_picked = event_names[3]
            break
        elif user_input == "5":
            event_picked = event_names[4]
            break
        else:
            print("Invalid Input")

    # asking the user if the points will go to a team or solo entire
    # loop will run until user gives a valid input
    while True:
        print()
        print("(A) To give points to a Solo Entire")
        print("(B) To give points to a Team Entire")
        user_input = input()

        if user_input.lower() == "a":
            
            # loop will run until the user has selected a person to give points to
            while True:
                # printing out all of the solo entries if the user picked A
                print("Solo Entries")
                index = 1
                for names in solo_entries:
                    print(str(index).ljust(10, ".") + names)
                    index += 1

                

                # try block to catch any errors
                try:

                    # asking the user who to give to points to
                    user_input = int(input("select a person to award points to: "))
                    
                    # this will hold the name that the user has selected
                    person_selected = solo_entries[user_input - 1]
                  

                    # first we will look to see if this person is all ready in the solo  points array
                    not_in_array = True
                    index = 0
                    
                    for names in solo_points:
                        # if the name is found in the array not_in_array will be set to falls
                        if person_selected in solo_points[index][0]:
                            not_in_array = False
                        index += 1   

                    # if not_in_array is still true then a new item will be created in the points array for them
                    if not_in_array:
                        temp_array = []
                        temp_array.append(person_selected)
                        temp_array.append(0)
                        solo_points.append(temp_array)
                        
                    # the user will now enter in how many poitns they would like to give to there selection
                    while True:
                        print()
                        points = input("Enter in how many points did " + str(person_selected) + " got in the "  + event_picked + " event: ")

                        # if the user entered in a whole number then the program will move on
                        if points.isdigit():
                            break
                        else:
                            print()
                            print("Can only give whole numbers as points")
                            print()
                        

                    # finding the corect person in the points array and giving them the points
                    for i in range(len(solo_points)):
                        for j in range(len(solo_points[i])):
                            if person_selected == solo_points[i][j]:
                                solo_points[i][1] += int(points)

                    break
                            
                    
                except Exception as err:
                    print()
                    print("INVALID INPUT")
                    print()
     
            
        elif user_input.lower() == "b":
            # printing out all of the teams
            index = 1
            print("Team Entries")
            # printing out the names in the team arrays
            # first for loop is to get the individual team arrays
            for teams in team_entries:
                print()
                # bool will be used to print out extra text for the team name
                name_of_team = True

                # second for loop is for getting the items out of each array
                for names in teams:
                    # if it is the first item in the array it will be the team name
                    if name_of_team:
                        print(str(index).ljust(10, ".") + names)
                        index += 1
                        name_of_team = False
                    else:
                        print(names)

                
                # try block to catch any errors
                try:

                    # asking the user who to give to points to
                    user_input = int(input("select a Team to award points to: "))
                    
                    # this will hold the name that the user has selected
                    team_selected = team_entries[user_input - 1][0]

                    # looking to see if this team is all ready in the team  points array
                    not_in_array = True
                    index = 0
                    
                    for names in team_points:
                        # if the name is found in the array not_in_array will be set to false
                        if team_selected in team_points[index][0]:
                            not_in_array = False
                        index += 1   

                    # if not_in_array is still true then a new item will be created in the points array for them
                    if not_in_array:
                        temp_array = []
                        temp_array.append(team_selected)
                        temp_array.append(0)
                        # adding the team in to the array
                        team_points.append(temp_array)

                    # the user will now enter in how many poitns they would like to give to there selection
                    while True:
                        print()
                        points = input("Enter in how many points did " + str(team_selected) + " get in the "  + event_picked + " event: ")

                        # if the user has entered in a whole number then the program will move on
                        if points.isdigit():
                            break
                        else:
                            print()
                            print("Can only give whole numbers as points")
                            print()
                            
                    # finding the corect team in the points array and giving them the points
                    for i in range(len(team_points)):
                        for j in range(len(team_points[i])):
                            if team_selected == team_points[i][j]:
                                team_points[i][1] += int(points)
                    break
                    
                except Exception as err:
                    print()
                    print("INVALID INPUT")
                    print()

        break


def print_out_socres():
    # printing out the header for the score bord using the .center function to aline  the text in the center
    print()
    text = "SCORE BOARD"
    print(text.center(40, "="))

    # printing out the scores for the solo entries
    print()
    print("SOLO ENTRIES")

    for names in solo_points:
        print(names[0].ljust(10, ".") + str(names[1]))

    # printing out the Scores for the teams
    print()
    print("TEAM SCORES")

    for teams in team_points:
        print(teams[0].ljust(10, ".") + str(teams[1]))


# +++ Start of the main program +++
# arrays that will hold the solo and team participants

solo_entries = []  # solo entries will be held in a 1D array
team_entries = []  # team entries will become a 2D array a new array per team

# this will be the array that the event names are held in
event_names = []

# points will be sotred in a 2d array
solo_points = []
team_points = []

main_maenu()
