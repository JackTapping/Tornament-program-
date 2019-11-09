# +++ creating methods that will be ued in the program +++

# this method will be used to add in values to the arrays that hold the entries
def add_entries():
    # this bool will be used as the while loops condition
    # as long as it is true the loop will run
    keep_adding_participants = True

    while keep_adding_participants:

        # asking the user to choose if they are going to add in a
        # solo or team participant
        print("Please pick if this is a team or solo entire:")
        print("(A) Solo")
        print("(B) Team")

        # getting the input from the user
        users_input = input("")
        print()  # adding in blank print statements to make the program more readable

        # Entering the correct if statements depending on the users input
        # if the user picks to enter a Solo entire this if statements will run
        if users_input == 'a':
            # asking the user to enter in the name of the Participant
            participants_name = input("Please enter in the name of the participants: ")

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
                # asking the user for the name of the team member
                team_member_name = input("Please enter in the name of the team member " + str(i + 1) + " : ")
                # adding the team member to the temp array
                temp_team_array.append(team_member_name)

            # finally the temp array will be added in to team_enties array
            # this will make team entries in to a 2D array
            team_entries.append(temp_team_array)

        # asking the user if they want to enter in a new participants
        print()
        add_more_participants = input("Would you like to enter in a new participant \n(Y) Yes \n(N) No\n")
        print()

        # if the user chooses no then the value of keep_adding_participants will be set to false
        # this will cause the while loop to stop running
        if add_more_participants == 'n':
            keep_adding_participants = False


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

        # this index will be used to access the correct arrys in the teamp and solo points arrays
        index = 0
        # this for loop will allow the user to add in the scores for the solo entries
        for names in solo_entries:
            # asking the user to enter in how many points the paricipants got in the event
            points = int(input("Enter in how many ponits did " + names + " get in the " + events + " event : "))

            # adding the points to the correct place in the solo points array
            solo_points[index][1] += points

            # increamenting index by one so we can get access to the exit array in solo points
            index += 1

        # setting index back to 0 so we can use it agine for the team points array
        index = 0

        # allowing the user to add in the points for the Teams
        for teams in team_points:
            # asking the user to enter in how many points the paricipants got in the event
            points = int(
                input("Enter in how many ponits did " + team_entries[index][0] + " get in the " + events + " event : "))

            # adding the points to the correct place in the solo points array
            team_points[index][1] += points

            # increamenting index by one so we can get access to the enxt array in solo points
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

add_entries()
naming_events()
awarding_points()
print_out_socres()
