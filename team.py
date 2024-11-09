class Team:
    #init method in the Class Team
    def __init__(self, team_id, date, team_name, team_type, fee_paid):
        self.__team_id = team_id
        self.__date = date
        self.__team_name = team_name
        self.__team_type = team_type
        self.__pay_fee = fee_paid

        # The Participation Cancellation Date will initially be empty.
        self.__date_for_cancellation = None

    #Get velues by using Accessor method and then set values by using Mutator method
    def get_the_team_id(self):
        return self.__team_id

    def get_the_fee_pay(self):
        return self.__pay_fee

    def get_team_type(self):
        return self.__team_type

    def get_team_name(self):
        return self.__team_name

    def set_the_name(self, team_name):
        self.__team_name = team_name

    def set_team_type(self, team_type):
        self.__team_type = team_type

    def set_paid_fee(self, fee_paid):
        self.__pay_fee = fee_paid

    def set_the_cancel_date(self, cancel_date):
        self.__date_for_cancellation = cancel_date

    def get_the_cancel_date(self):
        return self.__date_for_cancellation

    #Get a line that will write the team detail to a text file, .
    def get_the_file_data(self):
        return f"{self.__team_id},{self.__date},{self.__team_name},{self.__team_type},{self.__pay_fee},{self.__date_for_cancellation}"

    #The object is represented by a string.
    #Print a team instance when a print function is called.
    def __str__(self):
        res = f"Hockey team ID: {self.__team_id}\n"
        res += f"Name: {self.__team_name}\n"
        res += f"Date Of registration: {self.__date}\n"
        res += f"Type Of team: {self.__team_type}\n"
        if self.__pay_fee:
            res += f"Has the fee paid?: YES\n"
        else:
            res += f"Has the fee paid?: NO\n"
        if self.__date_for_cancellation:
            res += f"Cancel date Of participation: {self.__date_for_cancellation}\n"
        return res
