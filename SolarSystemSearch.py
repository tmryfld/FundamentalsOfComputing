# creates planet as a class for menu interface
# depending on user answer in main menu, this will create various versions of the planet, using certain value combinations
class planet():
  def __init__(self, name, mass, moons, distance): # arguments passed into planet class
    self._name = name
    self._mass = mass
    self._moons = moons
    self._distance = distance
   
  def showMass(self): # output for user menu choice 1
    print(f"{self._name} has a mass of {self._mass}.\n\n")
  
  def showMoons(self): # output for user menu choice 2
    print(f"{self._name} has {self._moons}.\n\n")
  
  def showDistance(self): # output for user menu choice 3
    print(f"{self._name} is approximately {self._distance} from the sun.\n\n")
    
  def showEverything(self): # output for user menu choice 4
    print(f"{self._name} has a mass of {self._mass},\n{self._name} has {self._moons},\n{self._name} is {self._distance} from the sun.\n\n")
  
  
  
# creates mainmenu as a class to be displayed to user
class mainMenu():
  def __init__(self, menuChoice):
    self.menuChoice = menuChoice
  
  def interface(): # displays main menu for user
    menuInput = input("""
    Welcome to the Solar Sytem Search Engine!
    Please select a number from the following options:\n
    1 - Show mass information about a planet
    2 - Show moon information about a planet
    3 - Show distance from the sun about a planet
    4 - Show all facts about a planet
    5 - Exit\n
    Alternatively, ask me anything: """)
    mainMenu.menuChoice = menuInput # passes value to menuChoice variable so it can be accessed during menu output stage
    if menuInput == "1": # multiple choices for main menu
      mainMenu.singlePlanetEntry() # uses singlePlanet for efficiency - one module to work out which planet user wants to see
    elif menuInput == "2":
      mainMenu.singlePlanetEntry()
    elif menuInput == "3":
      mainMenu.singlePlanetEntry()
    elif menuInput == "4":
      mainMenu.singlePlanetEntry()
    elif menuInput == "5":
      mainMenu.menuFiveOutput()
    else:
      menuInput = menuInput.replace("'s","") # removes potential errors with earth's not being in dictionary
      menuInput = menuInput.replace("'","") # as above, but covers venus'
      menuInput = menuInput.replace("?","") # removes question mark which concatenates with strings causing errors
      menuInputSplit = menuInput.split() # user input is split into separate words for evaluation
      mainMenu.sentenceKeyword = ""
      mainMenu.sentencePlanet = ""
      for eachword in menuInputSplit: # iterates for each item in the split words
        if eachword.title() in solarSystem: # identifies the planet entered by the user
          mainMenu.sentencePlanet = eachword.title() # stores found planet for later
        elif eachword.title() in keywords: # identifies keywords entered by the user
          mainMenu.sentenceKeyword = eachword.title() # stores found keyword for later
        elif eachword.title() == "Pluto": # looks for Pluto in sentence, as this is not in the dictionary, but likely to be entered by the user
          mainMenu.pluto() # informs the user that Pluto is not a planet, and gives them the option to restart
        else:
          pass

      if mainMenu.sentenceKeyword == "Mass" or mainMenu.sentenceKeyword == "Weight" or mainMenu.sentenceKeyword == "Massive": # looks to see if the user wants to see mass info only
        mainMenu.menuChoice = "1" # links to menuChoice 1 for passing arguments
        mainMenu.userPlanet = mainMenu.sentencePlanet # sets the userPlanet argument to equal what the user searched for
        mainMenu.planetPassArgs() # takes the user to the passing arguments module
      elif mainMenu.sentenceKeyword == "Moon" or mainMenu.sentenceKeyword == "Moons": # as above, but for moon info only
        mainMenu.menuChoice = "2"
        mainMenu.userPlanet = mainMenu.sentencePlanet
        mainMenu.planetPassArgs()
      elif mainMenu.sentenceKeyword == "Distance": # as above, but for distance info only
        mainMenu.menuChoice = "3"
        mainMenu.userPlanet = mainMenu.sentencePlanet
        mainMenu.planetPassArgs()
      elif mainMenu.sentenceKeyword == "Everything" or mainMenu.sentenceKeyword == "All" or mainMenu.sentenceKeyword == "About": # as above, but for all info
        mainMenu.menuChoice = "4"
        mainMenu.userPlanet = mainMenu.sentencePlanet
        mainMenu.planetPassArgs()
      else:
        print("I\'m sorry, I don\'t understand. Please try again.\n\n")
        mainMenu.interface()
      

    
  def singlePlanetEntry(): # used to determine which planet user wants to see information about
    userPlanet = input("\nWhat planet do you want to see? ")
    mainMenu.userPlanet = userPlanet.title() # string handling reduces data errors
    mainMenu.planetPassArgs() # passes single planet entry (numerical menu) to next module


  def planetPassArgs():
    if mainMenu.userPlanet.title() in solarSystem:
      mainMenu.planetData = planet(mainMenu.userPlanet, solarSystem[mainMenu.userPlanet][0], solarSystem[mainMenu.userPlanet][1], solarSystem[mainMenu.userPlanet][2]) #passes arguments to the planet class based on dictionary/user choice
      if mainMenu.menuChoice == "1": 
        mainMenu.menuOneOutput() # redirects to mass based on main menu choice
      elif mainMenu.menuChoice == "2":
        mainMenu.menuTwoOutput() # redirects to moons based on main menu choice
      elif mainMenu.menuChoice == "3":
        mainMenu.menuThreeOutput() # redirects to distance from sun based on main menu choice
      elif mainMenu.menuChoice == "4":
        mainMenu.menuFourOutput() # redirects to everything based on main menu choice
      else:
        print("Sorry, an error has occurred.\nRestarting...\n") # should not be needed, but error handling, just in case, restarts main menu
        mainMenu.interface()
    else: # allows user input to be blank, numerical, or outside of dictionary, will restart to main menu to allow user another attempt
      print("Planet not found in solar system.\nRestarting...\n")
      mainMenu.interface()


  def pluto():
    print("Technically, Pluto is a dwarf planet and is not part of the solar system.\nPlease try another planet.\n")
    mainMenu.menuFiveOutput() # allows the user to quit or restart
    

  def menuOneOutput():
    mainMenu.planetData.showMass() # shows planet mass information, based on user planet choice
    mainMenu.menuFiveOutput() # asks the user if they want to exit, if they don't it will restart to main menu
  
  
  def menuTwoOutput():
    mainMenu.planetData.showMoons() # shows planet moon information, based on user planet choice
    mainMenu.menuFiveOutput()
  
  
  def menuThreeOutput():
    mainMenu.planetData.showDistance() # shows distance from the sun information, based on user planet choice
    mainMenu.menuFiveOutput()
    
    
  def menuFourOutput():
    mainMenu.planetData.showEverything() # shows all planet data, based on user planet choice
    mainMenu.menuFiveOutput()
    
    
  def menuFiveOutput():
    try:
      exitQ = input("Would you like to exit? ") # gives user option to cancel exit, rather than terminate program
      if exitQ[0].upper() == "Y": # checks first digit of user answer, incase of "yeah" instead of "yes"
        print("Goodbye!") 
        quit()
      else:
        mainMenu.interface() # restarts program to main menu if any other character is present first
    except:
      mainMenu.interface()



# solar system data found on Wikipedia, created as dictionary with list definitions for individual access
solarSystem = {
"Mercury":("330,110,000,000,000,000,000,000 kg (0.055 Earths)","0 natural moons","29 million miles (46 million km)"),
"Venus":("4,867,500,000,000,000,000,000,000 kg (0.815 Earths)","0 natural moons","67 million miles (108 million km)"),
"Earth":("5,972,168,000,000,000,000,000,000 kg","1 moon, called \'The Moon\'","93 million miles (150 million km)"),
"Mars":("641,710,000,000,000,000,000,000 kg (0.107 Earths)","2 moons, called \'Phobos\' and \'Deimos\'","143 million miles (230 million km)"),
"Jupiter":("1,898,200,000,000,000,000,000,000,000 kg (317.8 Earths)","97 moons, with the four largest called \'Io\', \'Europa\', \'Ganymede\', and \'Callisto\'","484 million miles (778 million km"),
"Saturn":("568,000,000,000,000,000,000,000,000 kg (95.159 Earths)","274 known moons, with 63 of these being given names. \'Titan\' is the largest moon of these","886 million miles (1.4 billion km)"),
"Uranus":("86,810,000,000,000,000,000,000,000 kg (14.536 Earths)","29 known natural moons, with the main 5 called \'Miranda\', \'Ariel\', \'Umbriel\', \'Titania\', \'Oberon\'","1.8 billion miles (2.9 billion km)"),
"Neptune":("102,409,000,000,000,000,000,000,000 kg (17.147 Earths)","16 known moons, with the largest called \'Triton\'","2.8 billion miles (4.4 billion km)")
}
#Planet Data:
#https://en.wikipedia.org/wiki/Mercury_(planet)
#https://en.wikipedia.org/wiki/Venus
#https://en.wikipedia.org/wiki/Earth
#https://en.wikipedia.org/wiki/Mars
#https://en.wikipedia.org/wiki/Jupiter
#https://en.wikipedia.org/wiki/Saturn
#https://en.wikipedia.org/wiki/Neptune
#https://en.wikipedia.org/wiki/Uranus

keywords = ("Mass","Weight","Massive","Moon","Moons","Distance","Everything","All","About") # keywords to be used in ask me anything mode

mainMenu.interface() # launches main menu class, interface module
