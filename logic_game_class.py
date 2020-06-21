from bson import ObjectId

class Game:
    def __init__(self, mongo_client):
        self.field_of_play = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
        self.number_of_moves = 0
        self.winner = 0
        self.mongo = mongo_client

    def setFirstUser(self, user, name):
        print name
        self.user_1 = user
        self.user_1_name = name

    def setSecondUser(self, user, name):
        print name
        self.user_2 = user
        self.user_2_name = name

    def vivod(self):
        print(self.field_of_play)

    def victory(self,field):
        if (field == 1):
            print("Victory ", self.user_1)
            # self.exit_game()
            self.winner = 1
            self.increaseUserScore(self.user_1_name)
            return 1
        elif (field == 2):
            print("Victory ", self.user_2)
            # self.exit_game()
            self.winner = 2
            self.increaseUserScore(self.user_2_name)
            return 2
        elif (field == 3):
            print("No one won")
            # self.exit_game()
            self.winner = 3
            return 3
    def exit_game(self):
        print("let's start again")
        self.number_of_moves = 0
        self.field_of_play = [[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]
        self.winner = 0

    def increaseUserScore(self, name):
        scores = self.mongo.db.scoreboard
        output = None
        for s in scores.find({"useName": name}):
            output = {'userName': s['userName'], 'winCount': s['winCount'], "_id": str(s['_id'])}
            break
        if(output):
            self.mongo.db.scoreboard.update({"_id": ObjectId(output.get('_id'))}, {"$set": {"winCount": int(output.get('winCount')) + 1}})
        else:
            id = ObjectId()
            self.mongo.db.scoreboard.insert({"_id": id, "userName": name, "winCount": 1})