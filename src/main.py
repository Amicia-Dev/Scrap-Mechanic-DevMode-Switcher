import os
import time
import subprocess


def ConsoleSetup():
    os.system("title SM Devmode Switcher")
    consoleColor("Aqua")

def consoleColor(color):
    if color == "Green":
        os.system("color " + "A")
    elif color == "Aqua":
        os.system("color " + "B")
    elif color == "Red":
        os.system("color " + "C")
    elif color == "Purple":
        os.system("color " + "D")
    elif color == "Yellow":
        os.system("color " + "E")
    elif color == "White":
        os.system("color " + "F")

def debugger():
    consoleColor("Purple")
    print("")
    print("[Debug Mode]")
    print("")
    print("")
    print_path()
    print("")
    print("")
    print("")
    print("DevMode Status:")
    status()
    print("")
    print("")
    print("")
    print("Press Enter To Show Contents Of SurvivalGame.lua.")
    input()
    os.system('cls')
    print("Contents of SurvivalGame.lua:")
    print("")
    print("")
    if os.path.exists('path.x1'):
        with open('path.x1', 'r') as f:
            pathdata = f.read()
            pathdata = pathdata.replace('\n', '')
            luafile = open(pathdata)
            luafilecontent = luafile.read()
            print(luafilecontent)
            print("Scroll Up To See The Contents.")
    else:
        print("Path Not Set :(")
        print("Please Run First Time Setup / Reset Lua Path.")
    print("")
    print("Press Enter To Return To Menu.")
    input()

def find_path():
    consoleColor("Purple")
    print("Searching For SurvivalGame.lua...")
    subprocess.run([r"locatepath.bat"])
    if os.path.exists('path.x1'):
        os.system('cls')
        consoleColor("Green")
        print("Found Lua Path!")
        print("")
        print_path()
        print("")
        print("Press Enter To Return To Menu.")
        input()
    else:
        consoleColor("Yellow")
        os.system('cls')
        print("Lua File Not Found :(")
        print("")
        print("Please Press Enter To Type Your Lua Path Manually Or Exit The Program And Try Again.")
        input()
        os.system('cls')
        manualPathInput()
    return

def manualPathInput():
    
    consoleColor("Aqua")
    print("Enter The Full Path To Your SurvivalGame.lua ")
    print("Example: C:\Program Files (x86)\Steam\steamapps\common\Scrap Mechanic\Survival\Scripts\game\SurvivalGame.lua")
    path = input(">>> ")

    with open('path.x1', 'w') as f:
        f.write(path)
        os.system('cls')
    return

def print_path():

    if os.path.exists('path.x1'):
        with open('path.x1', 'r') as f:
            print("Current Survival Lua Path: ")
            print(f.read())
    else:
        print("Path Not Set :(")
        print("Please Run First Time Setup / Reset Lua Path.")
    return

def deleteSavedPath():

    os.remove("path.x1")
    ftsCheck()
    return

def status():

    HasDev = "local addCheats = true"
    HasDevNot = "local addCheats = g_survivalDev"

    if os.path.exists('path.x1'):
        with open('path.x1', 'r') as f:
            pathdata = f.read()
            pathdata = pathdata.replace('\n', '')

            luafile = open(pathdata)
            luafilecontent = luafile.read()

            if HasDev in luafilecontent:
                consoleColor("Green")
                print("DevMode is enabled!")

            elif HasDevNot in luafilecontent:
                consoleColor("Yellow")
                print("DevMode is NOT enabled")
            else:
                consoleColor("Red")
                print("Lua File Not Found :(")
    else:
        print("Path Not Set :(")
        print("Please Run First Time Setup / Reset Lua Path.")

def ftsCheck():

    if os.path.exists('path.x1'):
        print("Resetting Saved Lua Path.")
        print("")
        deleteSavedPath()
    else:

        find_path()

def devModeCommandList():
    print("""
Command List:      


/ammo "Give ammo (default 40)"
/spudgun "Give the spudgun"
/gatling "Give the potato gatling gun"
/shotgun "Give the fries shotgun"
/sunshake "Give 1 sunshake"
/baguette "Give 1 revival baguette"
/keycard "Give 1 keycard"
/powercore "Give 1 powercore"
/components "Give components (default 10)"
/glowsticks "Give components (default 10)"
/tumble "Set tumble state"
/god "Mechanic characters will take no damage"
/respawn "Respawn at last bed (or at the crash site)"
/encrypt "Restrict interactions in all warehouses"
/decrypt "Unrestrict interactions in all warehouses"
/limited "Use the limited inventory"
/unlimited "Use the unlimited inventory"
/ambush "Starts a 'random' encounter"
/recreate "Recreate world"
/timeofday "Sets the time of the day as a fraction (0.5=mid day)"
/timeprogress "Enables or disables time progress"
/day "Disable time progression and set time to daytime"
/spawn "Spawn a unit: 'woc', 'tapebot', 'totebot', 'haybot'"
/harvestable "Create a harvestable: 'tree', 'stone'"
/cleardebug "Clear debug draw objects"
/export "Exports blueprint $SURVIVAL_DATA/LocalBlueprints/.blueprint"
/import "Imports blueprint $SURVIVAL_DATA/LocalBlueprints/.blueprint"
/starterkit "Spawn a starter kit"
/mechanicstartkit"Spawn a starter kit for starting at mechanic station"
/pipekit "Spawn a pipe kit"
/foodkit "Spawn a food kit"
/seedkit "Spawn a seed kit"
/die "Kill the player"
/sethp "Set player hp value"
/setwater "Set player water value"
/setfood "Set player food value"
/aggroall "All hostile units will be made aware of the player's position"
/goto "Teleport to predefined position"
/raid "Start a level raid at player position at wave in hours."
/stopraid "Cancel all incoming raids"
/disableraids "Disable raids if true"
/camera "Spawn a SplineCamera tool"
/printglobals "Print all global lua variables"
/clearpathnodes "Clear all path nodes in overworld"
/enablepathpotatoes "Creates path nodes at potato hits in overworld and links to previous node"
""")
    print("")
    print("")
    print("Press Enter To Go Back To Main Menu.")
    input()


def switcher():

    print("1. Normal Mode")
    print("2. Dev Mode")
    print("3. Back")
    print("")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        os.system('cls')
        normalMode()
    elif choice == 2:
        os.system('cls')
        devMode()
    elif choice == 3:
        os.system('cls')
    return

def normalMode():
    consoleColor("Purple")
    print("Selecting Normal Mode...")
    with open('path.x1', 'r') as f:
            pathdata = f.read()
            pathdata = pathdata.replace('\n', '')
            luafile = open(pathdata)
            luafilecontent = luafile.read()
            modifiedLuaFile = luafilecontent.replace('local addCheats = true', 'local addCheats = g_survivalDev')

    with open(pathdata, 'w') as f2:
        f2.write(modifiedLuaFile)

    print("Mode Switched To Normal Mode!")
    print("")
    print("Press Enter To Go Back To Main Menu.")
    input()
def devMode():
    consoleColor("Purple")
    print("Selecting Normal Mode...")
    with open('path.x1', 'r') as f:
            pathdata = f.read()
            pathdata = pathdata.replace('\n', '')
            luafile = open(pathdata)
            luafilecontent = luafile.read()
            modifiedLuaFile = luafilecontent.replace('local addCheats = g_survivalDev', 'local addCheats = true')

    with open(pathdata, 'w') as f2:
        f2.write(modifiedLuaFile)

    print("Mode Switched To Dev Mode!")
    print("")
    print("Press Enter To Go Back To Main Menu.")
    input()
def info():

    consoleColor("White")
    print("")
    print("Scrap Mechanic Dev Mode Switcher.")
    print("Made by: Amicia")
    print("Web: https://amicia.rf.gd")
    print("Discord: amicia.dev")
    print("Version: 1.0.0")
    print("")
    print("")
    print("[Instructions]")
    print("")
    print("""1. Select "First Time Setup / Reset Lua Path" and let it finish. (It might take some time depending on your computer)""")
    print("If it doesn't find lua path, type path manually.")
    print("")
    print("2. Select Mode Switcher")
    print("Select which mode you want.")
    print("")
    print("3. Restart your game if you have it open.")
    print("")
    print("")
    print("[Extra Info]")
    print("")
    print("You can check which mode you currently have selected by selecting Dev Status in the main menu.")
    print("")
    print("You have a list of all the Scrap Mechanic commands by selecting Scrap Mechanic Command List in the main menu.")
    print("")
    print("In the debug mode, you can see the contents of the Lua file and some other info to help you debug.")
    print("")
    print("You can have scrap mechanic downloaded on any drive and that shouldn't be an issue.")
    print("")
    print("")
    print("[Possible Issues]")
    print("")
    print("If you have multiple copies of Scrap Mechanic on the same drive, it might cause issues, I'm not sure.")
    print("If you have multiple copies of Scrap Mechanic on different drives, it shouldn't be an issue since it selects")
    print("the installation on the lowest letter drive.")
    print("")
    print("If you move the game to another folder or drive it will cause issues.")
    print("""To resolve this and many other issues, simply run the "first time setup / reset lua" path again.""")
    print("")
    print("If you have any issues, please contact me on discord.")
    print("")
    print("")
    print("Thank you for using Scrap Mechanic Dev Mode Switcher.")
    print("")
    print("Scroll Up To See The Instructions.")
    print("Press Enter To Go Back To Main Menu.")
    input()

def main():

    os.system('cls')
    consoleColor("Aqua")

    while True:
        os.system('cls')
        consoleColor("Aqua")
        print("Scrap Mechanic Survival DevMode Toggle.")
        print("")
        print("1. First Time Setup / Reset Lua Path")
        print("2. Mode Switcher")
        print("3. DevMode Status")
        print("4. Scrap Mechanic Command List")
        print("5. Debug")
        print("6. Help")
        print("7. Exit")
        print("")

        choice = int(input("Enter Your Choice: "))
        
        if choice == 1: #First Time Setup Choice
            os.system('cls')
            ftsCheck()
            print("")
        elif choice == 2: #Switcher Choice
            os.system('cls')
            switcher()
            os.system('cls')
        elif choice == 3: #Dev Status Choice
            os.system('cls')
            status()
            print("")
            for i in range(3, 0, -1):
                print(i, end="\r")
                time.sleep(1)
            print("")
        elif choice == 4: #Scrap Mechanic Command List Choice
            os.system('cls')
            devModeCommandList()
            os.system('cls')        
        elif choice == 5: #Debug Choice
            os.system('cls')
            debugger()
            os.system('cls')
        elif choice == 6: #Help Choice
            os.system('cls')
            info()
            os.system('cls')
        elif choice == 7:
            quit()
        elif choice >= 7 or choice <= 0 or choice == None or choice == '':
            print("Invalid Choice. Please Try Again.")
            time.sleep(1)
            os.system('cls')

        else:
            print("Invalid Choice. Please Try Again.")
            time.sleep(1)
            os.system('cls')

if __name__ == '__main__':
    os.chdir("data")
    ConsoleSetup()
    main()
    quit()