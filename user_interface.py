
from team import Team

from datetime import date

#Create the UserInterface class
class UserInterface:
    #fee is 200
    def __init__(self, fee=100):

        #All teams will be stored in the follwing list. List is empty initially.
        self.__teams = []
        #Fees variable for team registration
        self.__fee = fee

    #Method for creating ID automatically for hockey team object
    def create_id(self):

        #First registred hockey team will get ID = 1.
        if len(self.__teams) == 0:
            return 1
        else:
            # Call all the ID that has been created from the team list.
            hockey_team_id = max(self.__teams, key=lambda team: team.get_the_team_id())
            if hockey_team_id:
                # Every new ID will be created by adding + 1 from the last ID that has been created in the list.
                return hockey_team_id.get_the_team_id() + 1
            else:
                return 1

    #Method for creating new team.
    def register_hockey_team(self):
        print("***---Hockey team registration---***")
        #While loop for asking the user to enter a team name.
        # It will stop when the user enter a correct value, not a blank line.
        while True:
            #strip() method to remove any extra spaces.
            team_name = str(input("Please enter the name Of your team: ")).strip()  
            if team_name:
                break
        #While loop for asking the user to enter a team type.
        #It will stop when the user enter a correct value i.e boys or girls.
        while True:
            #strip() method to remove any extra spaces.
            #lower() method to convert upper case into lower case
            t_type = str(input("Please enter the type Of your team (boys or girls): ")).strip().lower()
            if t_type != "boys" and t_type != "girls":
                print("Please enter a correct team type.")
            else:
                break
        #While loop for asking the user about the fee pay.
        #It will stop when the user enter a correct value i.e Y or N.
        while True:
            pay_fee = str(input("Has the fee paid? (Y/N) ")).strip().upper()
            if pay_fee != "Y" and pay_fee != "N":
                print("Please enter a valid input!")
            else:
                if pay_fee == "Y":
                    pay_fee = True
                else:
                    pay_fee = False
                break
        #Obtain the new ID for the newly created team
        n_id = self.create_id()

        #Variable today get the current date
        today_date = date.today()

        #Variable new_obj_team is declare to create a new Team object.
        new_obj_team = Team(n_id, today_date, team_name, t_type, pay_fee)

        #Team object is adding in the list
        self.__teams.append(new_obj_team)

        print("\n Congratulations you have registerd the team {} successfully".format(team_name))

    #Method for update the team
    def update_hockey_team(self):
        #The variable made_the_changes will keep track of changes made by users to a Team object.
        made_the_changes = False

        #Try and except for handlig errors.
        try:
            n_id = int(input("\nPlease enter the hockey team ID: "))
            #Search for the team by input (user given ID)
            f_team = [team for team in self.__teams if team.get_the_team_id() == n_id]

            #If record found.
            if f_team:
                #Outcome is the list with 1 element
                f_team = f_team[0]
                print("\n***---Information of hockey team ID {}---***".format(f_team.get_the_team_id()))

                #Print team name that is the outcome of the matched ID
                print("Team name: {}".format(f_team.get_team_name()))

                #User option to change a name or skip to update the name.
                u_name = str(input("Please enter the name you want to update (you can skip by leaving space): ")).strip()
                if u_name:
                    made_the_changes = True
                    f_team.set_the_name(u_name)

                #Print the team type that is the outcome of the matched ID
                print("Type: {}".format(f_team.get_team_type()))
                while True:
                    #User option to change the type or skip to update the type.
                    u_type = str(input("Please enter the type you want to update (boys/girls) (you can skip by leaving space): ")).strip().lower()
                    if u_type != "boys" and u_type != "girls" and u_type:
                        print("Please enter a valid type!")
                    elif not u_type:
                        break
                    else:
                        made_the_changes = True
                        f_team.set_team_type(u_type)
                        break
                
                # If there is any changes 
                if made_the_changes:
                    #User can choose a option to confirm the change or not?
                    changes_confirm = str(input("Are you sure you want to Confirm the changes? (Y/N): ")).strip().upper()
                    if changes_confirm == "Y":
                        #Find the team by ID in the list
                        for t in range(len(self.__teams)):
                            if self.__teams[t].get_the_team_id() == f_team.get_the_team_id():
                                #Update with the object that has been changed.
                                self.__teams[t] = f_team
                                break
                        print("Congratulations you have successfully updated the team.")
                    else:
                        print("You have not made any update.")

            else:
                print("The team ID {} is not found".format(n_id))
        except:
            print("Please enter a correct team ID!")

    #Method for fee payment for a team to pay 
    def participation_fee(self):
        #Try and except for handlig errors.
        try:
            n_id = int(input("\nPlease enter the hockey team ID: "))
            #Search for the team by input (user given ID)
            f_team = [team for team in self.__teams if team.get_the_team_id() == n_id]

            #If record found.
            if f_team:
                #Outcome is the list with 1 element
                f_team = f_team[0]

                #Current team already paid the fees or not.
                if f_team.get_the_fee_pay():
                    print("\nThe team {} has paid the fee.".format(f_team.get_team_name()))
                else:
                    #User can choose a option to confirm the change or not.
                    changes_confirm = str(input("Do you want to proceed the fee(Payment)? (Y/N): ")).strip().upper()
                    if changes_confirm == "Y":
                        f_team.set_paid_fee(True)
                        for t in range(len(self.__teams)):
                            if self.__teams[t].get_the_team_id() == f_team.get_the_team_id():
                                self.__teams[t] = f_team
                                break
                        print("Congratulations you have paid the fees.")
                    else:
                        print("You have not made any update.")

            else:
                print("Sorry entred team ID {} is not found".format(n_id))
        except:
            print("Please enter a correct team ID!")

    #Method for cancel participation
    def cancel_participation(self):
        #Try and except for handlig errors.
        try:
            n_id = int(input("\nPlease enter the hockey team's ID: "))
            #Search for the team by input (user given ID)
            f_team = [team for team in self.__teams if team.get_the_team_id() == n_id]

            #If record found.
            if f_team:
                #Outcome is the list with 1 element
                f_team = f_team[0]

                #Check to see if this team's participation has already been cancelled.
                if f_team.get_the_cancel_date():
                    print("\nTeam {} already cancelled the participation.".format(f_team.get_team_name()))
                else:
                    # User can choose a option to confirm the cancellation or not.
                    changes_confirm = str(input(
                        "Are you sure you want to cancell the participation for team {}? (Y/N): ".format(f_team.get_team_name()))).strip().upper()
                    if changes_confirm == "Y":
                        f_team.set_the_cancel_date(date.today())
                        for t in range(len(self.__teams)):
                            if self.__teams[t].get_the_team_id() == f_team.get_the_team_id():
                                self.__teams[t] = f_team
                                break
                        print("Congratulations you have successfully cancelled the participation for team {}.".format(f_team.get_team_name()))
                    else:
                        print("You have not made any update.")

            else:
                print("Team ID {} is not found.".format(n_id))
        except:
            print("Sorry please enter a correct team ID.")

    #Method to print a team detail by team ID.
    def teams_detail_by_id(self):
        #Try and except for handlig errors.
        try:
            n_id = int(input("\nPlease enter the hockey team ID: "))

            #Search for the team by input (user given ID)
            f_team = [team for team in self.__teams if team.get_the_team_id() == n_id]

            #If record found.
            if f_team:
                print("\n***---Your Requrid Information---***")
                #Outcome is the list with 1 element
                print(f_team[0], end="")
                print("\n")
            else:
                print(" The team ID {} is not found in the record.".format(n_id))
        except:
            print("Please enter a correct team ID.")

    #Method for delete a team by ID
    def delete_team_by_ID(self):
        #Try and except for handlig errors.
        try:
            n_id = int(input("\nPlease enter the ID of hockey team, which you want to delete: "))
            #Search the list for the team with the user given ID.
            f_team = [team for team in self.__teams if team.get_the_team_id() == n_id]

            #If  found 
            if f_team:
                #Outcome is the list with 1 element.
                f_team = f_team[0]
                print(" Team ID {} is found in the record.".format(f_team.get_the_team_id()))

                #Confirmation option to delete the team or not.
                changes_confirm = str(input("Are you sure you want to delete team '{}'? (Y/N): ".format(f_team.get_team_name()))).strip().upper()
                if changes_confirm == "Y":
                    #Filter the list to deleting the team with given ID.
                    self.__teams = [team for team in self.__teams if team.get_the_team_id() != n_id]
                    print("Team {} successfully deleted.".format(f_team.get_team_name()))
                else:
                    print("You have not made any update in the record.")
            else:
                print(" Team ID {} is not found in the record.".format(n_id))
        except:
            print("Plsease enter a correct time ID!")

    #Method for displaying all registred teams record.
    def all_teams_record(self):
        print("\n{} teams are participating in the cup".format(len(self.__teams)))
        if self.__teams:
            print("\n***---Following is the information regarding {} teams---***".format(len(self.__teams)))
            for team in self.__teams:
                # In print() method we can use the team object as we implemented the method __str__() in class Team ()
                print(team, end="")
                print("\n")
                
        else:
            print("\n No team registered yet!")

    #Method for displaying registred teams by type.
    def registred_teams_by_type(self):
        #While loop for enter a team by type
        # It will stop when the user enter a right value i.e girls or boys.
        while True:
            t_type = str(input("\nPlease enter your team by type (boys or girls): ")).strip().lower()
            if t_type != "boys" and t_type != "girls":
                print("Please enter a correct input!")
            else:
                break
        
        # Search the list for the team with this type by using List comprehension.
        teams_found = [team for team in self.__teams if team.get_team_type() == t_type]
        print("\n{} teams of the type {} in the list".format(len(teams_found),t_type))

        if teams_found:
            print("\n***---Following is the information regarding {} {} teams---***".format(len(teams_found),t_type))
            for team in teams_found:
                print(team, end="")
                print("\n")
        else:
            print("\n No teams found with entered type.")

    # Method for printing the total fee amount. 
    def total_fee_paid_amount(self):
        #All teams who paid the fees
        count_fee_paid = len([team for team in self.__teams if team.get_the_fee_pay()])
        amount = count_fee_paid * self.__fee
        print("\nTotal collected amount is {}.".format(amount))

        # Define a method that will print the number of registered team.
    def total_teams_registered(self):
        t_count = len(self.__teams)
        print("\n {} team(S) registred.\n".format(t_count))

    #Method for print the how much percent fee is payed.
    def percent_fee_pay(self):
        
        #Teams that has paid the fees
        count_fee_paid = len([team for team in self.__teams if team.get_the_fee_pay()])

        # Total number of teams
        t_number = len(self.__teams)
        if t_number == 0:
            percent = 0
        else:
            # Calculate the percentage of paid fee
            percent = (count_fee_paid / t_number) * 100.0
        print("\nFess paid by {}% of teams.".format(percent))

    #Mehtod for writing data from program into .text file.
    def save_data_into_file(self):
        if len(self.__teams) == 0:
            print("\nTeams Data Is Not Found To Write!\n")
        else:
            #Try and except for handlig errors.
            try:
                #Opens the teams.txt file to write the data.
                with open('teams.txt', 'w') as file:
                    #For loop for writing data line by line in the text file  
                    for team in self.__teams:
                        file.write(team.get_the_file_data())
                        file.write("\n")
                print("\nCongratulation your data is writen successfully in text file.\n")
            except:
                print("\nSome thing is wrong.\tError occurred!\n")
    #Mehtod for restoring data from .text file to the program .
    def restore_team_data(self):
        #Try and except for handlig errors.
        try:
            # Open the teams.txt file for reading
            with open('teams.txt') as file:
                # Read every line that are in the list.
                f_data = file.readlines()

            if len(f_data) > 0:
                # Clear the current list if there is any data in the file
                self.__teams.clear()

                # Apply the for loop in the list that contains strings
                for f_line in f_data:
                    # Remove any spaces and new lines characters
                    f_line = f_line.replace("\n", "").strip()

                    # id, name, etc are separated by applying comma
                    # Strings are converted into a list by applying split() method
                    values = f_line.split(",")
                    n_id = int(values[0])
                    date_ = values[1]
                    name_ = values[2]
                    type_ = values[3]

                    if values[4] == 'True':
                        pay_fee = True
                    else:
                        pay_fee = False
                    cancel_the_date = values[5]

                    # Declare a team variable to create a Team object
                    team = Team(n_id, date_, name_, type_, pay_fee)
                    if cancel_the_date != 'None':
                        team.set_the_cancel_date(cancel_the_date)

                    # Team object is adding in the list
                    self.__teams.append(team)
                print("\nCongratulations data is restored successfully to the program\n")
            else:
                print("\nSorry no data found, file is empty.\n")
        except:
            print("Some thing is wrong.\tError occurred!\n")    
    #Method for showing menu
    def menu(self):
        print("\n***---Welcome to Youth Hockey Cup---***\n")
        print("Enter 1 for register a new hockey team.")
        print("Enter 2 for print hockey team by ID.")
        print("Enter 3 for print hockey team by type (boys or girls).")
        print("Enter 4 for show all hockey teams.")
        print("Enter 5 for update a hockey team by ID.")
        print("Enter 6 for delete a hockey team by ID.")
        print("Enter 7 for confirm the fee status Of a team.")
        print("Enter 8 for cancellation the participation Of a team.")
        print("Enter 9 for displaying how many percent of all teams that has paid their fee.")
        print("Enter 10 for displaying the total number Of teams. ")
        print("Enter 11 for Total colected amount from fees.")
        print("Enter 12 for Saveing all Team's information from the program into a text file.")
        print("Enter 13 for restore all Team's information from a text file to program.")
        print("Enter 0 for exit from youth hockey cup menu.")

    #Hockey teams management menu calling by input.
    def start_menu(self):

        #Loop fro printing menu
        while True:
            #All Menu options will be printed.
            self.menu()
            input_from_user = -1

            #Try and except for handlig errors.
            try:
                input_from_user = int(input("\nPlease enter your choice: "))
            except:
                pass

            #Following methods will be called according to the user's choice.
            if input_from_user == 1:
                self.register_hockey_team()
            elif input_from_user == 2:
                self.teams_detail_by_id()
            elif input_from_user == 3:
                self.registred_teams_by_type()
            elif input_from_user == 4:
                self.all_teams_record()
            elif input_from_user == 5:
                self.update_hockey_team()
            elif input_from_user == 6:
                self.delete_team_by_ID()
            elif input_from_user == 7:
                self.participation_fee()
            elif input_from_user == 8:
                self.cancel_participation()
            elif input_from_user == 9:
                self.percent_fee_pay()
            elif input_from_user == 10:
                self.total_teams_registered()
            elif input_from_user == 11:
                self.total_fee_paid_amount()
            elif input_from_user == 12:
                self.save_data_into_file()
            elif input_from_user == 13:
                self.restore_team_data()
            elif input_from_user == 0:
                print("Exited successfully.")
                break
            else:
                print("Invalid input. Please try again.")
