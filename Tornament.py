# +++ creating methods that will be ued in the program +++

# This method will be used as a main menu for the porgram
def main_maenu():

    # putting everything in a while loop that will run untill the user enters a vaild input
    while(True):

        # printing out the title so the user knows what menu they are in
        title_text = "Main Menu"
        print(title_text.center(40,'='))

        # asking the suer to pick a menu
        print()
        print("please pick a menu to use:")
        print()
        print("(A) Add Participants")
        print("(B) Name Events")
        print("(C) Award Points")
        print("(D) view Scores")
        print("(E) Quit")

        # geting the user input
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
            naming_events()
            print()
                
        elif user_input.lower() == 'c':
            print()
            awarding_points()
            print()
                
        elif user_input.lower() == 'd':
            print()
            print_out_socres()
            print()

        # if the user enters in e then the main loop will break and end the program  
        elif user_input.lower() == 'e':
            break;

        # if the user does not enter in one of the options they will get an error 
        else:
            print()
            print("INVALID INPUT")
            print()

# this method will be used to add in values to the arrays that hold the entries
def add_entries():
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
            elif  add_more_participants.lower() == 'y':
                keep_adding_participants =True
                break
            else:
                print("INVALID INPUT")
                print()


# method for naming the events
def naming_events():
    # creating a for loop that will run 5 times
    # so the user can add in all of the names of the events
    for i in range(5):
        # asking the user for the name of the event
        name_of_event = input("please enter in the name of event number " + str(i + 1) + " : ")
        # adding in the name of the event to the array
        event_names.append(name_of_event)


# emethod for awwarding the points
def awarding_points():
    # adding all participants to the points array with a default score of 0

    # adding in values for the solo array
    for names in solo_entries:
        # crating a temp array to hold the name and score
        temp_array = []

        # adding in the name and the score to the temp array
        temp_array.append(names)
        temp_array.append(0)

        # adding the values of the temp array to solo points
        solo_points.append(temp_array)

    # adding in values for the eams array
    for teams in team_entries:
        # crating a temp array to hold the team name and score
        temp_array = []

        # adding in the name and the score to the temp array
        temp_array.append(teams[0])
        temp_array.append(0)

        # adding the values of the temp array to solo points
        team_points.append(temp_array)

    # creating nested for loops to go through each event and allow the user to enter in the scores
    # the first for loop will get the event that is being scored

    # this loop will get the name of every event
    for events in event_names:
        print()

        # this index will be used to access the correct arrays in the temp and solo points arrays
        index = 0
        
        # this for loop will allow the user to add in the scores for the solo entries
        for names in solo_entries:

            valid_input = False
            # while loop will run until the user enters ina vail in put
            while not valid_input:

                # using a try/except block because the user may enter in a value that will break the program
                try:
                    # asking the user to enter in how many points the participants got in the event
                    points = int(input("Enter in how many points did " + names + " get in the " + events + " event : "))

                    # adding the points to the correct place in the solo points array
                    solo_points[index][1] += points

                    # incrementing index by one so we can get access to the exit array in solo points
                    index += 1

                    valid_input = True

                except ValueError:
                    print()
                    print("INVALID INPUT")
                    print("Only numbers may be used as scores ")
                    print()

        # setting index back to 0 and valid_input to false so we can use it agine for the team points array
        index = 0
        valid_input = False

        # allowing the user to add in the points for the Teams
        for teams in team_points:

            # while loop will run until the user enters in a valid input
            while not valid_input:

                # using a try/except block because the user may enter in a value that will break the program
                try:
                    # asking the user to enter in how many points the Team got in the event
                    points = int(input("Enter in how many points did " + team_entries[index][0] + " get in the " + events + " event : "))

                    # adding the points to the correct place in the solo points array
                    team_points[index][1] += points

                    # incrementing index by one so we can get access to the exit array in solo points
                    index += 1

                    valid_input = True

                except ValueError:
                    print()
                    print("INVALID INPUT")
                    print("Only numbers may be used as scores ")
                    print()

            # incrementing index by one so we can get access to the next array in solo points
            index += 1


def print_out_socres():
    # printing out the header for the score bord using the .center function to aline  the text in the center
    print()
    text = "SCORE BOARD"
    print(text.center(40, "#"))

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
