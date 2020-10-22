# Creating Environment Class
class Env(object):
    def __init__(self):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.loc = {'A': '0', 'B': '0'}

        # take input conditions in locations A and B
        print("---------------------------------------------------------------------------------------------")
        self.loc['A'] =  int(input("Enter 0 for clean and 1 for dirty for BLOCK A(Left) >>>"))  
        self.loc['B'] =  int(input("Enter 0 for clean and 1 for dirty for BLOCK B(Right) >>> "))  

# Creating Simple Reflex Agent Class
class SimpleReflexVacuumAgent(Env):
    def __init__(self, Env):
        # place vacuum at a location
        vacuumLocation =  int(input("Enter Vaccuum Location 0 for A(Left) and 1 for B(Right) >>>"))
        print("---------------------------------------------------------------------------------------------")
        # if vacuum at A
        if vacuumLocation == 0:
            print("Vacuum is placed at Location A.")
            # and Location A is Dirty.
            if Env.loc['A'] == 1:
                print("Location A is Dirty.")
                # suck the dirt  and mark it clean
                Env.loc['A'] = 0
                print("Location A has been Cleaned.")
                # move to B
                print("Moving to Location B...")

                # if B is Dirty
                if Env.loc['B'] == 1:
                    print("Location B is Dirty.")
                    # suck and mark clean
                    Env.loc['B'] = 0
                    print("Location B has been Cleaned.")
            else:
                # move to B
                print("Location A is Cleaned , So Moving to Location B...")
                # if B is Dirty
                if Env.loc['B'] == 1:
                    print("Location B is Dirty.")
                    # suck and mark clean
                    Env.loc['B'] = 0
                    print("Location B has been Cleaned.")
                else:
                    print("Location B is Clean")    

        elif vacuumLocation == 1:
            print("Vacuum  placed at Location B.")
            # and B is Dirty
            if Env.loc['B'] == 1:
                print("Location B is Dirty.")
                # suck and mark clean
                Env.loc['B'] = 0
                print("Location B has been Cleaned.")
                # move to A
                print("Moving to Location A...")
                # if A is Dirty
                if Env.loc['A'] == 1:
                    print("Location A is Dirty.")
                    # suck and mark clean
                    Env.loc['A'] = 0
                    print("Location A has been Cleaned.")
            else:
                # move to A
                print("Location B is Cleaned , So Moving to Location A...")
                # if A is Dirty
                if Env.loc['A'] == 1:
                    print("Location A is Dirty.")
                    # suck and mark clean
                    Env.loc['A'] = 0
                    print("Location A has been Cleaned.")
                else:
                    print("Location A is cleaned")    
        # done cleaning
        if(Env.loc['A'] == 0 and Env.loc['B'] == 0):
            print("No operation !!")


Environment = Env()
VacuumCleanerAgent = SimpleReflexVacuumAgent(Environment)