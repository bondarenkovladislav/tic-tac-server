class Game:
    def __init__(self):
        self.field_of_play = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
        self.number_of_moves = 0

    def setFirstUser(self, user):
        self.user_1 = user

    def setSecondUser(self, user):
        self.user_2 = user

    def vivod(self):
        print(self.field_of_play)

    def victory(self,field):
        if (field == 1):
            print("Victory ", self.user_1)
            self.exit_game()
            return self.user_1
        elif (field == 2):
            print("Victory ", self.user_2)
            self.exit_game()
            return self.user_2
        elif (field == 3):
            print("No one won")
            self.exit_game()
            return "No one won"
    def exit_game(self):
        print("let's start again")
        self.number_of_moves = 0
        self.field_of_play = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
