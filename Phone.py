class Feature:
    def screen(self):
        print("size=3 by 2.5")
        print("No multimedia")
    def buttons(self):
        print("grid order. No Qwerty")
    def calling(self):
        print("Calling Feature")
    def Messaging(self):
        print("Messaging feature")
    def game(self):
        print("only 2-d game")

class Smart(Feature):
    def screen(self):
        print("size=5 by 3.5")
        print("Multimedia Available")
    def buttons(self):
        print("Qwerty keypad")
    def game(self):
        print("2-d and 3-d games")

blackberry=Smart()
blackberry.screen()
blackberry.game()
blackberry.calling()                   
