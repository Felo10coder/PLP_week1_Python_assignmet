# Assignment 1: Design Your Own Class
# Base class
class PremierLeague:
    def __init__(self, club, trophies_won):
        self.club = club
        self.trophies_won = trophies_won

    def __str__(self):
        return f"{self.club} has won {self.trophies_won} trophies"


# Inherited class
class Team(PremierLeague):
    def __init__(self, club, trophies_won, ucl_status):
        # initialize attributes directly
        self.club = club
        self.trophies_won = trophies_won
        self.ucl_status = ucl_status

    # polymorphism method
    def Ucl(self):
        return f"{self.club} is {self.ucl_status} playing UCL football"
        

# different team objects
arsenal = Team("Arsenal", 14, "currently")
man_u   = Team("Man-U", 13, "not")
chelsea = Team("Chelsea", 5, "currently")
wolves  = Team("Wolves", 0, "not")

# Demonstration
print(arsenal)
print(man_u)
print(chelsea)
print(wolves)


print("\n--- UCL Status of Clubs ---")
for team in [arsenal, man_u, chelsea, wolves]:
    print(team.Ucl())
    
    
 ## Activity 2: Polymorphism Challenge   
class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing 🚤"

class Bicycle:
    def move(self):
        return "Pedaling 🚴"

# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())

