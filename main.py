# This function takes the users list as a parameter. The users list will be generated after the all questions are completed in the main() function
def domestic_vacations(user):
    # Dictionary that will be filled
    score_dict = {}
    # counters that will be added to said dictionary
    cole_count = 0
    hubert_count = 0
    cornelius_count = 0
    lebron_count = 0
    darius_count = 0
    rick_count = 0
    # Available domestic vacations
    cole_vacation = "LOS ANGELES, CALIFORNIA"
    hubert_vacation = "MIAMI, FLORIA"
    cornelius_vacation = "NEW ORLEANS, LOUISIANA"
    lebron_vacation = "PORTLAND, OREGON"
    darius_vacation = "HOUSTON, TEXAS"
    rick_vacation = "NEW YORK CITY, NEW YORK"
    default_vacation = "FOR SOME REASON YOU DIDNT ALIGN WITH ANYONE, GO TO TACOMA, WASHINGTON"
    # User Profiles
    user_cole_dom=["Between the ages of 0-18", "washington", "risky", "metal", "explorer", "domestic travel preference", "houston"]
    user_hubert_dom=["Between the ages of 19-35", "new york", "bad", "rap", "relaxer", "domestic travel preference", "portland"]
    user_cornelius_dom=["Between the ages of 36-60", "texas", "good", "country", "explorer", "domestic travel preference", "san francisco"]
    user_lebron_dom=["Between the ages of 61-110", "california", "terrible", "metal", "explorer", "domestic travel preference", "dallas"]
    user_darius_dom=["Between the ages of 19-35", "florida", "terrible", "rap", "relaxer", "domestic travel preference", "seattle"]
    user_rick_dom=["Between the ages of 36-60", "oregon", "risky", "metal", "explorer", "domestic travel preference", "boston"]

    # Logic to compare the user with our premade users, adds a counter for each item that matches
    for i in user_cole_dom:
        for k in user:
            if i == k:
                cole_count += 1

    for i in user_hubert_dom:
        for k in user:
            if i == k:
                hubert_count += 1

    for i in user_cornelius_dom:
        for k in user:
            if i == k:
                cornelius_count += 1

    for i in user_lebron_dom:
        for k in user:
            if i == k:
                lebron_count += 1

    for i in user_darius_dom:
        for k in user:
            if i == k:
                darius_count += 1

    for i in user_rick_dom:
        for k in user:
            if i == k:
                rick_count += 1
    # A dictionary with the premade users and their count (this goes up depending on the user)
    score_dict.update({'Cole': cole_count, 'Hubert': hubert_count, 'Cornelius': cornelius_count, 'Lebron': lebron_count, 'Darius': darius_count, 'Rick': rick_count})

    # Finding out the largest key in the dictionary
    max_key = max(score_dict, key=score_dict.get)

    # If the largest key in the dictionary is X user, then return their preferred vacation. This will be the users vacation given to them.
    if max_key == 'Cole':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + cole_vacation + "!\n")
         print("Your vacation given: ")
         return cole_vacation
    elif max_key == 'Hubert':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + hubert_vacation + "!\n")
         print("Your vacation given: ")
         return hubert_vacation
    elif max_key == 'Cornelius':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + cornelius_vacation + "!\n")
         print("Your vacation given: ")
         return cornelius_vacation
    elif max_key == 'Lebron':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + lebron_vacation + "!\n")
         print("Your vacation given: ")
         return lebron_vacation
    elif max_key == 'Darius':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + darius_vacation + "!\n")
         print("Your vacation given: ")
         return darius_vacation
    elif max_key == 'Rick':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + rick_vacation + "!\n")
         print("Your vacation given: ")
         return rick_vacation

    # default vacation if the program cannot find a good match for the user (should be impossible)
    return default_vacation

# This function is almost the exact same code as the domestic_vacations, just different international vacations instead
def international_vacations(user):
    score_dict = {}
    cole_count = 0
    hubert_count = 0
    cornelius_count = 0
    lebron_count = 0
    darius_count = 0
    rick_count = 0
    cole_vacation = "OSLO, NORWAY"
    hubert_vacation = "CANCÚN, MEXICO"
    cornelius_vacation = "PARIS, FRANCE"
    lebron_vacation = "TOKYO, JAPAN"
    darius_vacation = "MADRID, SPAIN"
    rick_vacation = "REYKJAVIK, ICELAND"
    default_vacation = "FOR SOME REASON YOU DIDNT ALIGN WITH ANYONE, GO TO KABUL, AFGHANISTAN"

    user_cole_int=["Between the ages of 0-18", "washington", "risky", "metal", "explorer", "international travel preference", "russia"]
    user_hubert_int=["Between the ages of 19-35", "new york", "bad", "rap", "relaxer", "international travel preference", "japan"]
    user_cornelius_int=["Between the ages of 36-60", "texas", "good", "country", "explorer", "international travel preference", "italy"]
    user_lebron_int=["Between the ages of 61-110", "california", "risky", "metal", "explorer", "international travel preference", "canada"]
    user_darius_int=["Between the ages of 19-35", "florida", "horrible", "rap", "relaxer", "international travel preference", "japan"]
    user_rick_int=["Between the ages of 36-60", "oregon", "good", "metal", "explorer", "international travel preference", "poland"]

    for i in user_cole_int:
        for k in user:
            if i == k:
                cole_count += 1

    for i in user_hubert_int:
        for k in user:
            if i == k:
                hubert_count += 1

    for i in user_cornelius_int:
        for k in user:
            if i == k:
                cornelius_count += 1

    for i in user_lebron_int:
        for k in user:
            if i == k:
                lebron_count += 1

    for i in user_darius_int:
        for k in user:
            if i == k:
                darius_count += 1

    for i in user_rick_int:
        for k in user:
            if i == k:
                rick_count += 1

    score_dict.update({'Cole': cole_count, 'Hubert': hubert_count, 'Cornelius': cornelius_count, 'Lebron': lebron_count, 'Darius': darius_count, 'Rick': rick_count})

    max_key = max(score_dict, key=score_dict.get)

    if max_key == 'Cole':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + cole_vacation + "!\n")
         print("Your vacation given: ")
         return cole_vacation

    elif max_key == 'Hubert':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + hubert_vacation + "!\n")
         print("Your vacation given: ")
         return hubert_vacation

    elif max_key == 'Cornelius':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + cornelius_vacation + "!\n")
         print("Your vacation given: ")
         return cornelius_vacation

    elif max_key == 'Lebron':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + lebron_vacation + "!\n")
         print("Your vacation given: ")
         return lebron_vacation

    elif max_key == 'Darius':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + darius_vacation + "!\n")
         print("Your vacation given: ")
         return darius_vacation

    elif max_key == 'Rick':
         print("You align extremely close with vacationer " + max_key + "! This vacationer really enjoyed " + rick_vacation + "!\n")
         print("Your vacation given: ")
         return rick_vacation

    return default_vacation

# Main function, this is where the program will ask the user questions in order to figure out what vacation would be best for them
def main():
    # A list of all 50 states
    states = [
        "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
        "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
        "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana",
        "maine", "maryland", "massachusetts", "michigan", "minnesota",
        "mississippi", "missouri", "montana", "nebraska", "nevada", "new hampshire",
        "new jersey", "new mexico", "new york", "north carolina", "north dakota",
        "ohio", "oklahoma", "oregon", "pennsylvania", "rhode island",
        "south carolina", "south dakota", "tennessee", "texas", "utah",
        "vermont", "virginia", "washington", "west virginia", "wisconsin",
        "wyoming"
    ]

    # Our bool variables for input validation
    bool_main = False
    bool_age = False
    bool_valid_state = False
    bool_choice = False
    bool_music = False
    bool_activity = False
    bool_travel = False

    # Empty user list that will be filled
    user = []

    # What the user is going to see when they run the program first
    print("Hello!!\n Are you ready for your next dream vacation?")
    user_input = input("Enter Y/N\n").lower()

    # Game loop
    while bool_main == False:
        # if user input is y, then the game will start
        if user_input == 'y':
            print("Great!, lets get started!")
            # getting the users name
            user_name = input("What is your name?\n")
            print("Nice to meet you " + user_name)
            print("")
            print("I would like to learn more about you before sending you on your dream vacation....")
            print("Please answer everything truthfully, it will help me find your dream vacation!\n")

            # getting the users age (with validation)
            print("How old are you? Select your age group please: ")
            print("a: 3-18, b: 19-35, c: 36-60, d: 61-110 ")
            user_age = input("Enter A, B, C, or D\n").lower()
            while not bool_age:
                if user_age == 'a':
                    user.append("Between the ages of 0-18")
                    print(user_name + " is between the ages of 0-18")
                    bool_age = True
                elif user_age == 'b':
                    user.append("Between the ages of 19-35")
                    print(user_name + " is between the ages of 19-35")
                    bool_age = True
                elif user_age == 'c':
                    user.append("Between the ages of 36-60")
                    print(user_name + " is between the ages of 36-60")
                    bool_age = True
                elif user_age == 'd':
                    user.append("Between the ages of 61-110")
                    print(user_name + " is between the ages of 61-110")
                    bool_age = True
                else:
                    print("Enter a valid age please")
                    print("How old are you? Select your age group please: ")
                    print("a: 3-18, b: 19-35, c: 36-60, d: 61-110 ")
                    user_age = input("Enter A, B, C, or D\n").lower()
            # getting the users state (with validation (must be a valid state in the United States))
            user_home = input("What State Are You From?\n").lower()
            while not bool_valid_state:
                if user_home in states:
                    user.append(user_home)
                    bool_valid_state = True
                else:
                    print("Please try again, check your spelling and enter a valid state!")
                    user_home = input("What State Are You From?\n").lower()

            print("You're from " + user_home + "!\n")

            # Asking the user a hypothetical question with input validation
            print("Here is a question, please select option a, b, c, or d\n")
            print("You have been mailed a mysterious notebook of death, upon receiving it, you turn on the news and test it out on the leader of the Taliban, 5 minutes later its confirmed he is dead from a heart attack.")
            print("You get freaked out and don't touch the notebook for weeks, upon realizing that nothing has happened to you yet, you take another look at the notebook, what do you do from here?")
            print("Option a: You turn the notebook into the police")
            print("Option b: You consult your friends and family and ask them what you should do with the Notebook")
            print("Option c: You proceed to continue using the notebook")
            print("Option d: You go deep into the woods and burn the notebook before burying the ashes")
            user_choice = input("What should you do with the notebook? Enter: a, b, c, or d\n").lower()
            while not bool_choice:
                if user_choice == 'a':
                    print("Interesting choice! You have good intentions")
                    user.append("terrible")
                    bool_choice = True
                elif user_choice == 'b':
                    print("Very interesting, hopefully they have your best intentions in mind!")
                    user.append("bad")
                    bool_choice = True
                elif user_choice == 'c':
                    print("Oh no! Let me be on your good side!!!")
                    user.append("risky")
                    bool_choice = True
                elif user_choice == 'd':
                    print("This is probably the wisest move, nobody should have that sort of power")
                    user.append("good")
                    bool_choice = True
                else:
                    print("Enter a valid answer and try again please!")
                    user_choice = input("What should you do with the notebook? Enter: a, b, c, or d\n").lower()

            # printing out what the user has entered thus far
            print("")
            print("If you're scratching your head, don't worry! You're this much closer to getting your dream vacation!")
            print("Ok so far, here is what we know about you: ")
            print("1. Your name is " + user_name)
            print("2. You're " + user[0])
            print("3. You're from " + user[1])
            print("4. And you make " + user[2] + " choices!")
            print(" ")
            print("I just need to know a little more about you!\n")

            # asking the user about their taste in music with validation
            print("What type of music do you like the most between these 3 genres? Enter a, b, or c!")
            user_music = input("a: Metal, b: Country, c: Hip Hop\n").lower()
            while not bool_music:
                if user_music == 'a':
                    user.append("metal")
                    bool_music = True
                elif user_music == 'b':
                    user.append("country")
                    bool_music = True
                elif user_music == 'c':
                    user.append("hip hop")
                    bool_music = True
                else:
                    print("Enter a valid answer please")
                    print("What type of music do you like the most between these 3 genres? Enter a, b, or c!")
                    user_music = input("a: Metal, b: Country, c: Hip Hop\n").lower()

            print("You like " + user[3] + " music wow!\n")

            # asking if a user is active or a relaxer
            print("Does your ideal getaway involve exploring and doing as many things as possible? Or would you rather relax and unwind? Enter a or b!")
            user_activity = input("a: Exploring, b: Relaxing\n").lower()
            while not bool_activity:
                if user_activity == 'a':
                    user.append("explorer")
                    bool_activity = True
                elif user_activity == 'b':
                    user.append("relaxer")
                    bool_activity = True
                else:
                    print("Enter a valid answer please")
                    print("Does your ideal getaway involve exploring and doing as many things as possible? Or would you rather relax and unwind? Enter a or b!")
                    user_activity = input("a: Exploring, b: Relaxing\n").lower()

            # asking if a user wants to travel domestically or internationally, depending on their choice here they will be given a dom or int vacation
            print("Are you interested in traveling domestically or internationally? Enter a or b")
            user_travel = input("a: Domestic, b: International\n").lower()
            while not bool_travel:
                if user_travel == 'a':
                    user.append("domestic travel preference")
                    user_never1 = input("Ok for the last part, type a city you will never go to again\n").lower()
                    user.append(user_never1)
                    print("Ok! We can move on now!")
                    print("Now, I will use my secret AI technology to give you a place you will really really like visiting!")
                    print("**************GENERATING*****************")
                    print("**************GENERATING*****************")
                    print("**************GENERATING*****************")
                    print("**************GENERATING*****************")
                    domestic_vacation = domestic_vacations(user)
                    print(domestic_vacation)
                    bool_travel = True
                    bool_main = True
                elif user_travel == 'b':
                    user.append("international travel preference")
                    user_never1 = input("Ok for the last part, type a Country you will never vacation at again\n").lower()
                    user.append(user_never1)
                    print("Ok! We can move on now!")
                    print("Now, I will use my secret AI technology to give you a place you will really really like visiting!")
                    print("                         **************GENERATING*****************")
                    print("                         **************GENERATING*****************")
                    print("                         **************GENERATING*****************")
                    print("                         **************GENERATING*****************")
                    international_vacation = international_vacations(user)
                    print(international_vacation)
                    bool_travel = True
                    bool_main = True
                # input validation
                else:
                    print("Enter a valid answer please")
                    print("Are you interested in traveling domestically or internationally? Enter a or b")
                    user_travel = input("a: Domestic, b: International\n").lower()
        # input validation for the game loop
        else:
            print("Oh...... You're being silly of course you want a dream vacation! Enter the key "'y'" to continue!")
            user_input = input("Enter Y/N\n").lower()
main()


