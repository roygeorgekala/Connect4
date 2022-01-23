'''Computer Project submitted by the group(Roy George, Arwxnav Bansal, Noel ,Sujay students of DPS Bangalore East) for the academic year
2016. Designed on Python 2.7 and graphics built using Tkinter '''


# Importing Tkinter for GUI
import tkinter as tk
import tkinter.messagebox as tkMessageBox

# Importing time for using the sleep functionality
import time as t

# Using the PIL to manipulate pictures for the logo(Not a standard library module)
from PIL import Image, ImageTk


# Intializing score variables for both colors' score outside the definition of the game so that scores are not lost while resetting
RedScore = 0
BlueScore = 0

# The variable that decides which color will start
Starter = 0

# Defining a continue function to be used while clicking continue buttons on the information screens


def Continue():
    root.destroy()


# Creating a small Tkinter window to display the rules and instructions
root = tk.Tk()
root.wm_title("Instructions and Rules of the game:")
root.configure(background="navajowhite")
root.iconbitmap("rulebook.ico")


Instructions = tk.Label(root, bd=50, bg="indianred", fg="white", text="The 'Join 4' game: \n\n1.  The objective is to get any 4 of the same colour without a break in between.\n\n2.  The 4 can be continously placed in a row column OR DIAGONALLY.\n\n3  .Do not click on the same checkbox two times.\n\n4  .The first turn belongs to the player playing as the color blue\n\n5.  One Undo is allowed per turn.")
Instructions.pack()


ContinueButton = tk.Button(
    root, text="Click here to continue..", command=Continue, bd=10)
ContinueButton.pack(side="bottom")
root.mainloop()

# Defining the entire game as a function


def Game():
    # Creating the parent widget and naming the whole window as CONNECT 4
    root = tk.Tk()
    root.wm_title("JOIN 4")
    root.iconbitmap("logo.ico")

    # Creating a variable integer to help in the alternation process between red and blue
    x = tk.IntVar()
    x.set(Starter)

    # Last click is stored
    global LastClick
    LastClick = 0
    global Checker
    Checker = 0

    # Creating 2 lists so that we can identify which buttons were clicked and which colour each clicked checkbox is now
    SetOfClicksRed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    SetOfClicksBlue = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Making lists of all the possibilies:
    # List of all possibilities in the Horizontal direction
    PossH1 = [1, 2, 3, 4]
    PossH2 = [2, 3, 4, 5]
    PossH3 = [3, 4, 5, 6]
    PossH4 = [7, 8, 9, 10]
    PossH5 = [8, 9, 10, 11]
    PossH6 = [9, 10, 11, 12]
    PossH7 = [13, 14, 15, 16]
    PossH8 = [14, 15, 16, 17]
    PossH9 = [15, 16, 17, 18]
    PossH10 = [19, 20, 21, 22]
    PossH11 = [20, 21, 22, 23]
    PossH12 = [21, 22, 23, 24]
    PossH13 = [25, 26, 27, 28]
    PossH14 = [26, 27, 28, 29]
    PossH15 = [27, 28, 29, 30]
    PossH16 = [31, 32, 33, 34]
    PossH17 = [32, 33, 34, 35]
    PossH18 = [33, 34, 35, 36]

    # List of all possibilities in the Vertical direction
    PossV1 = [1, 7, 13, 19]
    PossV2 = [7, 13, 19, 25]
    PossV3 = [13, 19, 25, 31]
    PossV4 = [2, 8, 14, 20]
    PossV5 = [8, 14, 20, 26]
    PossV6 = [14, 20, 26, 32]
    PossV7 = [3, 9, 15, 21]
    PossV8 = [9, 15, 21, 27]
    PossV9 = [15, 21, 27, 33]
    PossV10 = [4, 10, 16, 22]
    PossV11 = [10, 16, 22, 28]
    PossV12 = [16, 22, 28, 34]
    PossV13 = [5, 11, 17, 23]
    PossV14 = [11, 17, 23, 29]
    PossV15 = [17, 23, 29, 35]
    PossV16 = [6, 12, 18, 24]
    PossV17 = [12, 18, 24, 30]
    PossV18 = [18, 24, 30, 36]

    # List of all possibilities in the Diagonal directions
    PossD1 = [1, 8, 15, 22]
    PossD2 = [8, 15, 22, 29]
    PossD3 = [15, 22, 29, 36]
    PossD4 = [2, 9, 16, 23]
    PossD5 = [9, 16, 23, 30]
    PossD6 = [3, 10, 17, 24]
    PossD7 = [7, 14, 21, 28]
    PossD8 = [14, 21, 28, 35]
    PossD9 = [13, 20, 27, 34]
    PossD10 = [6, 11, 16, 21]
    PossD11 = [11, 16, 21, 26]
    PossD12 = [16, 21, 26, 31]
    PossD13 = [5, 10, 15, 20]
    PossD14 = [10, 15, 20, 25]
    PossD15 = [4, 9, 14, 19]
    PossD16 = [12, 17, 22, 27]
    PossD17 = [17, 22, 27, 32]
    PossD18 = [18, 23, 28, 33]

    # This funtion changes colour of the clicked checkbox
    def ColorChange(identifier):
        global Starter
        global LastClick

        LastClick = identifier

        if x.get() % 2 == 1:
            Turn["text"] = "Blue's Turn"
            Turn["bg"] = "darkcyan"
        elif x.get() % 2 == 0:
            Turn["text"] = "Red's Turn"
            Turn["bg"] = "indianred"

        # Doing this helps to convert the identifier to a set so that we can check with the other sets if it has been lciked earlier or not
        m = [identifier]

        # This if-else statement helps confirm whether the button has been clicked previously or not
        # Checks if current identifier is a subset of either the blue or red clicked buttons
        if set(m) < set(SetOfClicksRed) or set(m) < set(SetOfClicksBlue):

            if Turn["bg"] == "indianred":
                Turn["bg"] = "darkcyan"
                Turn["text"] = "Blue's Turn"

            elif Turn["bg"] == "darkcyan":
                Turn["bg"] = "indianred"
                Turn["text"] = "Red's Turn"

            if identifier == 1:
                chkbutton1.deselect()

            elif identifier == 2:
                chkbutton2.deselect()

            elif identifier == 3:
                chkbutton3.deselect()

            elif identifier == 4:
                chkbutton4.deselect()

            elif identifier == 5:
                chkbutton6.deselect()

            elif identifier == 6:
                chkbutton6.deselect()

            elif identifier == 7:
                chkbutton7.deselect()

            elif identifier == 8:
                chkbutton8.deselect()

            elif identifier == 9:
                chkbutton9.deselect()

            elif identifier == 10:
                chkbutton10.deselect()

            elif identifier == 11:
                chkbutton11.deselect()

            elif identifier == 12:
                chkbutton12.deselect()

            elif identifier == 13:
                chkbutton13.deselect()

            elif identifier == 14:
                chkbutton14.deselect()

            elif identifier == 15:
                chkbutton15.deselect()

            elif identifier == 16:
                chkbutton16.deselect()

            elif identifier == 17:
                chkbutton17.deselect()

            elif identifier == 18:
                chkbutton18.deselect()

            elif identifier == 19:
                chkbutton19.deselect()

            elif identifier == 20:
                chkbutton20.deselect()

            elif identifier == 21:
                chkbutton21.deselect()

            elif identifier == 22:
                chkbutton22.deselect()

            elif identifier == 23:
                chkbutton23.deselect()

            elif identifier == 24:
                chkbutton24.deselect()

            elif identifier == 25:
                chkbutton25.deselect()

            elif identifier == 26:
                chkbutton26.deselect()

            elif identifier == 27:
                chkbutton27.deselect()

            elif identifier == 28:
                chkbutton28.deselect()

            elif identifier == 29:
                chkbutton29.deselect()

            elif identifier == 30:
                chkbutton30.deselect()

            elif identifier == 31:
                chkbutton31.deselect()

            elif identifier == 32:
                chkbutton32.deselect()

            elif identifier == 33:
                chkbutton33.deselect()

            elif identifier == 34:
                chkbutton34.deselect()

            elif identifier == 35:
                chkbutton35.deselect()

            elif identifier == 36:
                chkbutton36.deselect()

        else:

            # Increments x value to change the colour of the next clicked button
            x.set(x.get() + 1)
            # The if-else helps to alternate the colours between red and blue
            if x.get() % 2 == 0:
                # Under the if statement if a clicked button is clicked the first time and every subsequent alternate time, it will turn red

                # Identifier helps to identify which checkbox was clicked
                if identifier == 1:
                    # After identification the color of the checkbox is changed to requimaroon color and background is changed to slategray
                    chkbutton1["selectcolor"] = "darkred"
                    chkbutton1["bg"] = "slategray"
                    chkbutton1.deselect()

                elif identifier == 2:
                    chkbutton2["selectcolor"] = "darkred"
                    chkbutton2["bg"] = "slategray"
                    chkbutton2.deselect()

                elif identifier == 3:
                    chkbutton3["selectcolor"] = "darkred"
                    chkbutton3["bg"] = "slategray"
                    chkbutton3.deselect()

                elif identifier == 4:
                    chkbutton4["selectcolor"] = "darkred"
                    chkbutton4["bg"] = "slategray"
                    chkbutton4.deselect()

                elif identifier == 5:
                    chkbutton5["selectcolor"] = "darkred"
                    chkbutton5["bg"] = "slategray"
                    chkbutton5.deselect()

                    chkbutton6.deselect()
                elif identifier == 6:
                    chkbutton6["selectcolor"] = "darkred"
                    chkbutton6["bg"] = "slategray"
                    chkbutton6.deselect()

                elif identifier == 7:
                    chkbutton7["selectcolor"] = "darkred"
                    chkbutton7["bg"] = "slategray"
                    chkbutton7.deselect()

                elif identifier == 8:
                    chkbutton8["selectcolor"] = "darkred"
                    chkbutton8["bg"] = "slategray"
                    chkbutton8.deselect()

                elif identifier == 9:
                    chkbutton9["selectcolor"] = "darkred"
                    chkbutton9["bg"] = "slategray"
                    chkbutton9.deselect()

                elif identifier == 10:
                    chkbutton10["selectcolor"] = "darkred"
                    chkbutton10["bg"] = "slategray"
                    chkbutton10.deselect()

                elif identifier == 11:
                    chkbutton11["selectcolor"] = "darkred"
                    chkbutton11["bg"] = "slategray"
                    chkbutton11.deselect()

                elif identifier == 12:
                    chkbutton12["selectcolor"] = "darkred"
                    chkbutton12["bg"] = "slategray"
                    chkbutton12.deselect()

                elif identifier == 13:
                    chkbutton13["selectcolor"] = "darkred"
                    chkbutton13["bg"] = "slategray"
                    chkbutton13.deselect()

                elif identifier == 14:
                    chkbutton14["selectcolor"] = "darkred"
                    chkbutton14["bg"] = "slategray"
                    chkbutton14.deselect()

                elif identifier == 15:
                    chkbutton15["selectcolor"] = "darkred"
                    chkbutton15["bg"] = "slategray"
                    chkbutton15.deselect()

                elif identifier == 16:
                    chkbutton16["selectcolor"] = "darkred"
                    chkbutton16["bg"] = "slategray"
                    chkbutton16.deselect()

                elif identifier == 17:
                    chkbutton17["selectcolor"] = "darkred"
                    chkbutton17["bg"] = "slategray"
                    chkbutton17.deselect()

                elif identifier == 18:
                    chkbutton18["selectcolor"] = "darkred"
                    chkbutton18["bg"] = "slategray"
                    chkbutton18.deselect()

                elif identifier == 19:
                    chkbutton19["selectcolor"] = "darkred"
                    chkbutton19["bg"] = "slategray"
                    chkbutton19.deselect()

                elif identifier == 20:
                    chkbutton20["selectcolor"] = "darkred"
                    chkbutton20["bg"] = "slategray"
                    chkbutton20.deselect()

                elif identifier == 21:
                    chkbutton21["selectcolor"] = "darkred"
                    chkbutton21["bg"] = "slategray"
                    chkbutton21.deselect()

                elif identifier == 22:
                    chkbutton22["selectcolor"] = "darkred"
                    chkbutton22["bg"] = "slategray"
                    chkbutton22.deselect()

                elif identifier == 23:
                    chkbutton23["selectcolor"] = "darkred"
                    chkbutton23["bg"] = "slategray"
                    chkbutton23.deselect()

                elif identifier == 24:
                    chkbutton24["selectcolor"] = "darkred"
                    chkbutton24["bg"] = "slategray"
                    chkbutton24.deselect()

                elif identifier == 25:
                    chkbutton25["selectcolor"] = "darkred"
                    chkbutton25["bg"] = "slategray"
                    chkbutton25.deselect()

                elif identifier == 26:
                    chkbutton26["selectcolor"] = "darkred"
                    chkbutton26["bg"] = "slategray"
                    chkbutton26.deselect()

                elif identifier == 27:
                    chkbutton27["selectcolor"] = "darkred"
                    chkbutton27["bg"] = "slategray"
                    chkbutton27.deselect()

                elif identifier == 28:
                    chkbutton28["selectcolor"] = "darkred"
                    chkbutton28["bg"] = "slategray"
                    chkbutton28.deselect()

                elif identifier == 29:
                    chkbutton29["selectcolor"] = "darkred"
                    chkbutton29["bg"] = "slategray"
                    chkbutton29.deselect()

                elif identifier == 30:
                    chkbutton30["selectcolor"] = "darkred"
                    chkbutton30["bg"] = "slategray"
                    chkbutton30.deselect()

                elif identifier == 31:
                    chkbutton31["selectcolor"] = "darkred"
                    chkbutton31["bg"] = "slategray"
                    chkbutton31.deselect()

                elif identifier == 32:
                    chkbutton32["selectcolor"] = "darkred"
                    chkbutton32["bg"] = "slategray"
                    chkbutton32.deselect()

                elif identifier == 33:
                    chkbutton33["selectcolor"] = "darkred"
                    chkbutton33["bg"] = "slategray"
                    chkbutton33.deselect()

                elif identifier == 34:
                    chkbutton34["selectcolor"] = "darkred"
                    chkbutton34["bg"] = "slategray"
                    chkbutton34.deselect()

                elif identifier == 35:
                    chkbutton35["selectcolor"] = "darkred"
                    chkbutton35["bg"] = "slategray"
                    chkbutton35.deselect()

                elif identifier == 36:
                    chkbutton36["selectcolor"] = "darkred"
                    chkbutton36["bg"] = "slategray"
                    chkbutton36.deselect()

                # Sets the x-th term of the set of red clicked buttons to the identifier
                SetOfClicksRed[x.get()] = identifier

            else:
                # Under the else statement if a clicked button is clicked the second time and every subsequent alternate time, it will turn blue
                if identifier == 1:
                    chkbutton1["selectcolor"] = "blue"
                    chkbutton1["bg"] = "slategray"
                    chkbutton1.deselect()

                elif identifier == 2:
                    chkbutton2["selectcolor"] = "blue"
                    chkbutton2["bg"] = "slategray"
                    chkbutton2.deselect()

                elif identifier == 3:
                    chkbutton3["selectcolor"] = "blue"
                    chkbutton3["bg"] = "slategray"
                    chkbutton3.deselect()

                elif identifier == 4:
                    chkbutton4["selectcolor"] = "blue"
                    chkbutton4["bg"] = "slategray"
                    chkbutton4.deselect()

                elif identifier == 5:
                    chkbutton5["selectcolor"] = "blue"
                    chkbutton5["bg"] = "slategray"
                    chkbutton5.deselect()

                elif identifier == 6:
                    chkbutton6["selectcolor"] = "blue"
                    chkbutton6["bg"] = "slategray"
                    chkbutton6.deselect()

                elif identifier == 7:
                    chkbutton7["selectcolor"] = "blue"
                    chkbutton7["bg"] = "slategray"
                    chkbutton7.deselect()

                elif identifier == 8:
                    chkbutton8["selectcolor"] = "blue"
                    chkbutton8["bg"] = "slategray"
                    chkbutton8.deselect()

                elif identifier == 9:
                    chkbutton9["selectcolor"] = "blue"
                    chkbutton9["bg"] = "slategray"
                    chkbutton9.deselect()

                elif identifier == 10:
                    chkbutton10["selectcolor"] = "blue"
                    chkbutton10["bg"] = "slategray"
                    chkbutton10.deselect()

                elif identifier == 11:
                    chkbutton11["selectcolor"] = "blue"
                    chkbutton11["bg"] = "slategray"
                    chkbutton11.deselect()

                elif identifier == 12:
                    chkbutton12["selectcolor"] = "blue"
                    chkbutton12["bg"] = "slategray"
                    chkbutton12.deselect()

                elif identifier == 13:
                    chkbutton13["selectcolor"] = "blue"
                    chkbutton13["bg"] = "slategray"
                    chkbutton13.deselect()

                elif identifier == 14:
                    chkbutton14["selectcolor"] = "blue"
                    chkbutton14["bg"] = "slategray"
                    chkbutton14.deselect()

                elif identifier == 15:
                    chkbutton15["selectcolor"] = "blue"
                    chkbutton15["bg"] = "slategray"
                    chkbutton15.deselect()

                elif identifier == 16:
                    chkbutton16["selectcolor"] = "blue"
                    chkbutton16["bg"] = "slategray"
                    chkbutton16.deselect()

                elif identifier == 17:
                    chkbutton17["selectcolor"] = "blue"
                    chkbutton17["bg"] = "slategray"
                    chkbutton17.deselect()

                elif identifier == 18:
                    chkbutton18["selectcolor"] = "blue"
                    chkbutton18["bg"] = "slategray"
                    chkbutton18.deselect()

                elif identifier == 19:
                    chkbutton19["selectcolor"] = "blue"
                    chkbutton19["bg"] = "slategray"
                    chkbutton19.deselect()

                elif identifier == 20:
                    chkbutton20["selectcolor"] = "blue"
                    chkbutton20["bg"] = "slategray"
                    chkbutton20.deselect()

                elif identifier == 21:
                    chkbutton21["selectcolor"] = "blue"
                    chkbutton21["bg"] = "slategray"
                    chkbutton21.deselect()

                elif identifier == 22:
                    chkbutton22["selectcolor"] = "blue"
                    chkbutton22["bg"] = "slategray"
                    chkbutton22.deselect()

                elif identifier == 23:
                    chkbutton23["selectcolor"] = "blue"
                    chkbutton23["bg"] = "slategray"
                    chkbutton23.deselect()

                elif identifier == 24:
                    chkbutton24["selectcolor"] = "blue"
                    chkbutton24["bg"] = "slategray"
                    chkbutton24.deselect()

                elif identifier == 25:
                    chkbutton25["selectcolor"] = "blue"
                    chkbutton25["bg"] = "slategray"
                    chkbutton25.deselect()

                elif identifier == 26:
                    chkbutton26["selectcolor"] = "blue"
                    chkbutton26["bg"] = "slategray"
                    chkbutton26.deselect()

                elif identifier == 27:
                    chkbutton27["selectcolor"] = "blue"
                    chkbutton27["bg"] = "slategray"
                    chkbutton27.deselect()

                elif identifier == 28:
                    chkbutton28["selectcolor"] = "blue"
                    chkbutton28["bg"] = "slategray"
                    chkbutton28.deselect()

                elif identifier == 29:
                    chkbutton29["selectcolor"] = "blue"
                    chkbutton29["bg"] = "slategray"
                    chkbutton29.deselect()

                elif identifier == 30:
                    chkbutton30["selectcolor"] = "blue"
                    chkbutton30["bg"] = "slategray"
                    chkbutton30.deselect()

                elif identifier == 31:
                    chkbutton31["selectcolor"] = "blue"
                    chkbutton31["bg"] = "slategray"
                    chkbutton31.deselect()

                elif identifier == 32:
                    chkbutton32["selectcolor"] = "blue"
                    chkbutton32["bg"] = "slategray"
                    chkbutton32.deselect()

                elif identifier == 33:
                    chkbutton33["selectcolor"] = "blue"
                    chkbutton33["bg"] = "slategray"
                    chkbutton33.deselect()

                elif identifier == 34:
                    chkbutton34["selectcolor"] = "blue"
                    chkbutton34["bg"] = "slategray"
                    chkbutton34.deselect()

                elif identifier == 35:
                    chkbutton35["selectcolor"] = "blue"
                    chkbutton35["bg"] = "slategray"
                    chkbutton35.deselect()

                elif identifier == 36:
                    chkbutton36["selectcolor"] = "blue"
                    chkbutton36["bg"] = "slategray"
                    chkbutton36.deselect()

                # Sets the x-th term of the set of blue clicked buttons to the identifier
                SetOfClicksBlue[x.get()] = identifier

        # The if statement checks if any of the possibilities are a subset of all clicked red buttons
        global Starter
        if set(PossH1) < set(SetOfClicksRed) or set(PossH2) < set(SetOfClicksRed) or set(PossH3) < set(SetOfClicksRed) or set(PossH4) < set(SetOfClicksRed) or set(PossH5) < set(SetOfClicksRed) or set(PossH6) < set(SetOfClicksRed) or set(PossH7) < set(SetOfClicksRed) or set(PossH8) < set(SetOfClicksRed) or set(PossH9) < set(SetOfClicksRed) or set(PossH10) < set(SetOfClicksRed) or set(PossH11) < set(SetOfClicksRed) or set(PossH12) < set(SetOfClicksRed) or set(PossH13) < set(SetOfClicksRed) or set(PossH14) < set(SetOfClicksRed) or set(PossH15) < set(SetOfClicksRed) or set(PossH16) < set(SetOfClicksRed) or set(PossH17) < set(SetOfClicksRed) or set(PossH18) < set(SetOfClicksRed) or set(PossV1) < set(SetOfClicksRed) or set(PossV2) < set(SetOfClicksRed) or set(PossV3) < set(SetOfClicksRed) or set(PossV4) < set(SetOfClicksRed) or set(PossV5) < set(SetOfClicksRed) or set(PossV6) < set(SetOfClicksRed) or set(PossV7) < set(SetOfClicksRed) or set(PossV8) < set(SetOfClicksRed) or set(PossV9) < set(SetOfClicksRed) or set(PossV10) < set(SetOfClicksRed) or set(PossV11) < set(SetOfClicksRed) or set(PossV12) < set(SetOfClicksRed) or set(PossV13) < set(SetOfClicksRed) or set(PossV14) < set(SetOfClicksRed) or set(PossV15) < set(SetOfClicksRed) or set(PossV16) < set(SetOfClicksRed) or set(PossV17) < set(SetOfClicksRed) or set(PossV18) < set(SetOfClicksRed) or set(PossD1) < set(SetOfClicksRed) or set(PossD2) < set(SetOfClicksRed) or set(PossD3) < set(SetOfClicksRed) or set(PossD4) < set(SetOfClicksRed) or set(PossD5) < set(SetOfClicksRed) or set(PossD6) < set(SetOfClicksRed) or set(PossD7) < set(SetOfClicksRed) or set(PossD8) < set(SetOfClicksRed) or set(PossD9) < set(SetOfClicksRed) or set(PossD10) < set(SetOfClicksRed) or set(PossD11) < set(SetOfClicksRed) or set(PossD12) < set(SetOfClicksRed) or set(PossD13) < set(SetOfClicksRed) or set(PossD14) < set(SetOfClicksRed) or set(PossD15) < set(SetOfClicksRed) or set(PossD16) < set(SetOfClicksRed) or set(PossD17) < set(SetOfClicksRed) or set(PossD18) < set(SetOfClicksRed):

            WinStatement()  # Declares the winner of the round

            global RedScore
            RedScore += 1  # Increments the score of the red player

            Starter = 0

            t.sleep(0.75)

            Reset()  # Resets to advance to next round

        # The elif statement checks if any of the possibilities are a subset of all clicked blue buttons
        elif set(PossH1) < set(SetOfClicksBlue) or set(PossH2) < set(SetOfClicksBlue) or set(PossH3) < set(SetOfClicksBlue) or set(PossH4) < set(SetOfClicksBlue) or set(PossH5) < set(SetOfClicksBlue) or set(PossH6) < set(SetOfClicksBlue) or set(PossH7) < set(SetOfClicksBlue) or set(PossH8) < set(SetOfClicksBlue) or set(PossH9) < set(SetOfClicksBlue) or set(PossH10) < set(SetOfClicksBlue) or set(PossH11) < set(SetOfClicksBlue) or set(PossH12) < set(SetOfClicksBlue) or set(PossH13) < set(SetOfClicksBlue) or set(PossH14) < set(SetOfClicksBlue) or set(PossH15) < set(SetOfClicksBlue) or set(PossH16) < set(SetOfClicksBlue) or set(PossH17) < set(SetOfClicksBlue) or set(PossH18) < set(SetOfClicksBlue) or set(PossV1) < set(SetOfClicksBlue) or set(PossV2) < set(SetOfClicksBlue) or set(PossV3) < set(SetOfClicksBlue) or set(PossV4) < set(SetOfClicksBlue) or set(PossV5) < set(SetOfClicksBlue) or set(PossV6) < set(SetOfClicksBlue) or set(PossV7) < set(SetOfClicksBlue) or set(PossV8) < set(SetOfClicksBlue) or set(PossV9) < set(SetOfClicksBlue) or set(PossV10) < set(SetOfClicksBlue) or set(PossV11) < set(SetOfClicksBlue) or set(PossV12) < set(SetOfClicksBlue) or set(PossV13) < set(SetOfClicksBlue) or set(PossV14) < set(SetOfClicksBlue) or set(PossV15) < set(SetOfClicksBlue) or set(PossV16) < set(SetOfClicksBlue) or set(PossV17) < set(SetOfClicksBlue) or set(PossV18) < set(SetOfClicksBlue) or set(PossD1) < set(SetOfClicksBlue) or set(PossD2) < set(SetOfClicksBlue) or set(PossD3) < set(SetOfClicksBlue) or set(PossD4) < set(SetOfClicksBlue) or set(PossD5) < set(SetOfClicksBlue) or set(PossD6) < set(SetOfClicksBlue) or set(PossD7) < set(SetOfClicksBlue) or set(PossD8) < set(SetOfClicksBlue) or set(PossD9) < set(SetOfClicksBlue) or set(PossD10) < set(SetOfClicksBlue) or set(PossD11) < set(SetOfClicksBlue) or set(PossD12) < set(SetOfClicksBlue) or set(PossD13) < set(SetOfClicksBlue) or set(PossD14) < set(SetOfClicksBlue) or set(PossD15) < set(SetOfClicksBlue) or set(PossD16) < set(SetOfClicksBlue) or set(PossD17) < set(SetOfClicksBlue) or set(PossD18) < set(SetOfClicksBlue):

            WinStatement()  # Declares the winner of the round

            global BlueScore
            BlueScore += 1  # Increments the score of the blue player

            Starter = 1

            t.sleep(0.75)

            Reset()  # Resets to advance to next round

    # Defining the quit and reset commands for the respective buttons

    def Quit():
        global BlueScore
        global RedScore

        if BlueScore > RedScore:
            tkMessageBox.showinfo(
                "The winner is...", "\n          Player Blue wins the game          \n")
        elif BlueScore < RedScore:
            tkMessageBox.showinfo(
                "The winner is...", "\n          Player Red wins the game           \n")
        else:
            tkMessageBox.showinfo("The winner is...",
                                  "\n           Its a draw!          ")

        root.destroy()

    def Reset():
        root.destroy()
        Game()

    def ScoreReset():
        root.destroy()

        global BlueScore
        BlueScore = 0

        global RedScore
        RedScore = 0
        Game()

    def Undo():
        global Checker
        global LastClick

        if LastClick == Checker:
            tkMessageBox.showinfo(
                "Warning!", "Only one undo per turn allowed.")

        else:

            Checker = LastClick

            if LastClick == 1:
                chkbutton1["selectcolor"] = "white"
                chkbutton1["bg"] = "gainsboro"
                chkbutton1.deselect()

            elif LastClick == 2:
                chkbutton2["selectcolor"] = "white"
                chkbutton2["bg"] = "gainsboro"
                chkbutton2.deselect()

            elif LastClick == 3:
                chkbutton3["selectcolor"] = "white"
                chkbutton3["bg"] = "gainsboro"
                chkbutton3.deselect()

            elif LastClick == 4:
                chkbutton4["selectcolor"] = "white"
                chkbutton4["bg"] = "gainsboro"
                chkbutton4.deselect()

            elif LastClick == 5:
                chkbutton5["selectcolor"] = ""
                chkbutton5["bg"] = "gainsboro"
                chkbutton5.deselect()

            elif LastClick == 6:
                chkbutton6["selectcolor"] = "white"
                chkbutton6["bg"] = "gainsboro"
                chkbutton6.deselect()

            elif LastClick == 7:
                chkbutton7["selectcolor"] = "white"
                chkbutton7["bg"] = "gainsboro"
                chkbutton7.deselect()

            elif LastClick == 8:
                chkbutton8["selectcolor"] = "white"
                chkbutton8["bg"] = "gainsboro"
                chkbutton8.deselect()

            elif LastClick == 9:
                chkbutton9["selectcolor"] = "white"
                chkbutton9["bg"] = "gainsboro"
                chkbutton9.deselect()

            elif LastClick == 10:
                chkbutton10["selectcolor"] = "white"
                chkbutton10["bg"] = "gainsboro"
                chkbutton10.deselect()

            elif LastClick == 11:
                chkbutton11["selectcolor"] = "white"
                chkbutton11["bg"] = "gainsboro"
                chkbutton11.deselect()

            elif LastClick == 12:
                chkbutton12["selectcolor"] = "white"
                chkbutton12["bg"] = "gainsboro"
                chkbutton12.deselect()

            elif LastClick == 13:
                chkbutton13["selectcolor"] = "white"
                chkbutton13["bg"] = "gainsboro"
                chkbutton13.deselect()

            elif LastClick == 14:
                chkbutton14["selectcolor"] = "white"
                chkbutton14["bg"] = "gainsboro"
                chkbutton14.deselect()

            elif LastClick == 15:
                chkbutton15["selectcolor"] = "white"
                chkbutton15["bg"] = "gainsboro"
                chkbutton15.deselect()

            elif LastClick == 16:
                chkbutton16["selectcolor"] = "white"
                chkbutton16["bg"] = "gainsboro"
                chkbutton16.deselect()

            elif LastClick == 17:
                chkbutton17["selectcolor"] = "white"
                chkbutton17["bg"] = "gainsboro"
                chkbutton17.deselect()

            elif LastClick == 18:
                chkbutton18["selectcolor"] = "white"
                chkbutton18["bg"] = "gainsboro"
                chkbutton18.deselect()

            elif LastClick == 19:
                chkbutton19["selectcolor"] = "white"
                chkbutton19["bg"] = "gainsboro"
                chkbutton19.deselect()

            elif LastClick == 20:
                chkbutton20["selectcolor"] = "white"
                chkbutton20["bg"] = "gainsboro"
                chkbutton20.deselect()

            elif LastClick == 21:
                chkbutton21["selectcolor"] = "white"
                chkbutton21["bg"] = "gainsboro"
                chkbutton21.deselect()

            elif LastClick == 22:
                chkbutton22["selectcolor"] = "white"
                chkbutton22["bg"] = "gainsboro"
                chkbutton22.deselect()

            elif LastClick == 23:
                chkbutton23["selectcolor"] = "white"
                chkbutton23["bg"] = "gainsboro"
                chkbutton23.deselect()

            elif LastClick == 24:
                chkbutton24["selectcolor"] = "white"
                chkbutton24["bg"] = "gainsboro"
                chkbutton24.deselect()

            elif LastClick == 25:
                chkbutton25["selectcolor"] = "white"
                chkbutton25["bg"] = "gainsboro"
                chkbutton25.deselect()

            elif LastClick == 26:
                chkbutton26["selectcolor"] = "white"
                chkbutton26["bg"] = "gainsboro"
                chkbutton26.deselect()

            elif LastClick == 27:
                chkbutton27["selectcolor"] = "white"
                chkbutton27["bg"] = "gainsboro"
                chkbutton27.deselect()

            elif LastClick == 28:
                chkbutton28["selectcolor"] = "white"
                chkbutton28["bg"] = "gainsboro"
                chkbutton28.deselect()

            elif LastClick == 29:
                chkbutton29["selectcolor"] = "white"
                chkbutton29["bg"] = "gainsboro"
                chkbutton29.deselect()

            elif LastClick == 30:
                chkbutton30["selectcolor"] = "white"
                chkbutton30["bg"] = "gainsboro"
                chkbutton30.deselect()

            elif LastClick == 31:
                chkbutton31["selectcolor"] = "white"
                chkbutton31["bg"] = "gainsboro"
                chkbutton31.deselect()

            elif LastClick == 32:
                chkbutton32["selectcolor"] = "white"
                chkbutton32["bg"] = "gainsboro"
                chkbutton32.deselect()

            elif LastClick == 33:
                chkbutton33["selectcolor"] = "white"
                chkbutton33["bg"] = "gainsboro"
                chkbutton33.deselect()

            elif LastClick == 34:
                chkbutton34["selectcolor"] = "white"
                chkbutton34["bg"] = "gainsboro"
                chkbutton34.deselect()

            elif LastClick == 35:
                chkbutton35["selectcolor"] = "white"
                chkbutton35["bg"] = "gainsboro"
                chkbutton35.deselect()

            elif LastClick == 36:
                chkbutton36["selectcolor"] = "white"
                chkbutton36["bg"] = "gainsboro"
                chkbutton36.deselect()

            if x.get() % 2 == 0:
                SetOfClicksRed.remove(LastClick)
            else:
                SetOfClicksBlue.remove(LastClick)
            x.set(x.get()-1)

            if x.get() % 2 == 0:
                Turn["text"] = "Blue's Turn"
                Turn["bg"] = "darkcyan"
            elif x.get() % 2 == 1:
                Turn["text"] = "Red's Turn"
                Turn["bg"] = "indianred"

    # Defining the Winning statement funtion to display the winner of a round

    def WinStatement():
        if x.get() % 2 == 0:
            tkMessageBox.showinfo("And the winner is ....",
                                  "The winner of this round is Red")

        else:
            tkMessageBox.showinfo("And the winner is ....",
                                  "The winner of this round is Blue")

    # Creating the frames in the parent widget:

    # Creating a parent frame for all other frames
    frame_parent = tk.Frame(root, bd=40, bg="lavender")
    frame_parent.pack()

    # Frame for the logo created
    frame_logo = tk.Frame(frame_parent, bd=10, bg="lightsteelblue")
    frame_logo.pack(side="top")

    # A label is created to display game logo
    img2 = ImageTk.PhotoImage(Image.open("logo.gif"))
    Head2 = tk.Label(frame_logo, image=img2)
    Head2.pack()

    # Spacer labels used to place the Turn and Starting labels in the appropiate spot
    Spacer1 = tk.Label(frame_logo, bd=2, bg="lightsteelblue")
    Spacer1.pack(side="top")

    Spacer2 = tk.Label(frame_logo, bd=5, bg="lightsteelblue")
    Spacer2.pack(side="left")

    # Label that shows who starts
    Starting = tk.Label(frame_logo, bd=5)
    Starting.pack(side="left")
    if Starter == 1:
        Starting["text"] = "Red Starts"
        Starting["bg"] = "indianred"
    elif Starter == 0:
        Starting["text"] = "Blue Starts"
        Starting["bg"] = "darkcyan"

    Spacer3 = tk.Label(frame_logo, bd=5, bg="lightsteelblue")
    Spacer3.pack(side="left")

    UndoButton = tk.Button(frame_logo, command=Undo, text="Undo ", width=8)
    UndoButton.pack(side="left")

    Spacer4 = tk.Label(frame_logo, bd=5, bg="lightsteelblue")
    Spacer4.pack(side="right")

    # Label that shows whos turn it is
    Turn = tk.Label(frame_logo, bd=5)
    Turn.pack(side="right")
    if Starter == 1:
        Turn["text"] = "Red's Turn"
        Turn["bg"] = "indianred"
    elif Starter == 0:
        Turn["text"] = "Blue's Turn"
        Turn["bg"] = "darkcyan"

    # Frame for the checkbuttons, score and control buttons is made
    frame_game = tk.Frame(frame_parent, bd=10, bg="lightsteelblue")
    frame_game.pack(side="bottom")

    # Frame for all 36 checkbuttons is created
    frame_chkbuttons = tk.Frame(frame_game, relief="solid", bg="blue")
    frame_chkbuttons.pack()

    # Frame for the control buttons (i.e reset and quit) is created
    frame_controlbuttons = tk.Frame(
        frame_game, height=50, bd=10, bg="lightsteelblue", relief="ridge")
    frame_controlbuttons.pack(side="bottom")

    frame_controlbuttons1 = tk.Frame(
        frame_controlbuttons, height=50, bd=4, bg="lightsteelblue")
    frame_controlbuttons1.pack(side="top")

    frame_controlbuttons2 = tk.Frame(
        frame_controlbuttons, height=50, bd=4, bg="lightsteelblue")
    frame_controlbuttons2.pack(side="bottom")

    # Frame for displaying the red players score is created
    frame_RedScore = tk.Frame(
        frame_game, bd=2, relief="ridge", bg="lightsteelblue")
    frame_RedScore.pack(side="left")

    # Frame for displaying the blue players score is created
    frame_BlueScore = tk.Frame(
        frame_game, bd=2, relief="ridge", bg="lightsteelblue")
    frame_BlueScore.pack(side="right")

    # Text to be displayed as the scores
    TextRed = "Red Score", RedScore
    TextBlue = "Blue Score", BlueScore

    # Labels displaying the respective scores of the players is created
    Label_RedScore = tk.Label(
        frame_RedScore, text=TextRed, fg="red", bd=10, bg="yellow")
    Label_RedScore.pack()
    Label_BlueScore = tk.Label(
        frame_BlueScore, text=TextBlue, fg="blue", bd=10, bg="yellow")
    Label_BlueScore.pack()

    # Creating the exit and reset buttons:
    FrameForScoreReset = tk.Frame(
        frame_controlbuttons1, bd=3, bg="lightsteelblue")
    FrameForScoreReset.pack(side="right")
    ScoreResetButton = tk.Button(
        FrameForScoreReset, bd=5, relief="raised", width=10, command=ScoreReset, text="Reset Score")
    ScoreResetButton.pack()

    FrameForReset = tk.Frame(frame_controlbuttons1, bd=3, bg="lightsteelblue")
    FrameForReset.pack(side="left")
    ResetButton = tk.Button(FrameForReset, text="Reset Grid", command=Reset,
                            width=10, relief="raised", bd=5)  # , bg = "palegoldenrod")
    ResetButton.pack()

    FrameForExit = tk.Frame(frame_controlbuttons2, bg="lightsteelblue")
    FrameForExit.pack()
    ExitButton = tk.Button(FrameForExit, text="Quit", command=Quit,
                           width=20, relief="raised", bd=5)  # , bg = "palegoldenrod")
    ExitButton.pack()

    # Creating the checkboxes; ColorChange function is called with identifer being the same as checkbox number to help identify it
    chkbutton1 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda: ColorChange(1), relief="raised", cursor="dot")
    chkbutton2 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda:  ColorChange(2), relief="raised", cursor="dot")
    chkbutton3 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda:  ColorChange(3), relief="raised", cursor="dot")
    chkbutton4 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda:  ColorChange(4), relief="raised", cursor="dot")
    chkbutton5 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda:  ColorChange(5), relief="raised", cursor="dot")
    chkbutton6 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda:  ColorChange(6), relief="raised", cursor="dot")
    chkbutton7 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda:  ColorChange(7), relief="raised", cursor="dot")
    chkbutton8 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda:  ColorChange(8), relief="raised", cursor="dot")
    chkbutton9 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                command=lambda:  ColorChange(9), relief="raised", cursor="dot")
    chkbutton10 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(10), relief="raised", cursor="dot")
    chkbutton11 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(11), relief="raised", cursor="dot")
    chkbutton12 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(12), relief="raised", cursor="dot")
    chkbutton13 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(13), relief="raised", cursor="dot")
    chkbutton14 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(14), relief="raised", cursor="dot")
    chkbutton15 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(15), relief="raised", cursor="dot")
    chkbutton16 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(16), relief="raised", cursor="dot")
    chkbutton17 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(17), relief="raised", cursor="dot")
    chkbutton18 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(18), relief="raised", cursor="dot")
    chkbutton19 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(19), relief="raised", cursor="dot")
    chkbutton20 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(20), relief="raised", cursor="dot")
    chkbutton21 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(21), relief="raised", cursor="dot")
    chkbutton22 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(22), relief="raised", cursor="dot")
    chkbutton23 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(23), relief="raised", cursor="dot")
    chkbutton24 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(24), relief="raised", cursor="dot")
    chkbutton25 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(25), relief="raised", cursor="dot")
    chkbutton26 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(26), relief="raised", cursor="dot")
    chkbutton27 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(27), relief="raised", cursor="dot")
    chkbutton28 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(28), relief="raised", cursor="dot")
    chkbutton29 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(29), relief="raised", cursor="dot")
    chkbutton30 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(30), relief="raised", cursor="dot")
    chkbutton31 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(31), relief="raised", cursor="dot")
    chkbutton32 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(32), relief="raised", cursor="dot")
    chkbutton33 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(33), relief="raised", cursor="dot")
    chkbutton34 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(34), relief="raised", cursor="dot")
    chkbutton35 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(35), relief="raised", cursor="dot")
    chkbutton36 = tk.Checkbutton(frame_chkbuttons, height=2, width=2,
                                 command=lambda:  ColorChange(36), relief="raised", cursor="dot")

    # It is packed in a grid form
    chkbutton1.grid(column=1, row=1)
    chkbutton2.grid(column=2, row=1)
    chkbutton3.grid(column=3, row=1)
    chkbutton4.grid(column=4, row=1)
    chkbutton5.grid(column=5, row=1)
    chkbutton6.grid(column=6, row=1)
    chkbutton7.grid(column=1, row=2)
    chkbutton8.grid(column=2, row=2)
    chkbutton9.grid(column=3, row=2)
    chkbutton10.grid(column=4, row=2)
    chkbutton11.grid(column=5, row=2)
    chkbutton12.grid(column=6, row=2)
    chkbutton13.grid(column=1, row=3)
    chkbutton14.grid(column=2, row=3)
    chkbutton15.grid(column=3, row=3)
    chkbutton16.grid(column=4, row=3)
    chkbutton17.grid(column=5, row=3)
    chkbutton18.grid(column=6, row=3)
    chkbutton19.grid(column=1, row=4)
    chkbutton20.grid(column=2, row=4)
    chkbutton21.grid(column=3, row=4)
    chkbutton22.grid(column=4, row=4)
    chkbutton23.grid(column=5, row=4)
    chkbutton24.grid(column=6, row=4)
    chkbutton25.grid(column=1, row=5)
    chkbutton26.grid(column=2, row=5)
    chkbutton27.grid(column=3, row=5)
    chkbutton28.grid(column=4, row=5)
    chkbutton29.grid(column=5, row=5)
    chkbutton30.grid(column=6, row=5)
    chkbutton31.grid(column=1, row=6)
    chkbutton32.grid(column=2, row=6)
    chkbutton33.grid(column=3, row=6)
    chkbutton34.grid(column=4, row=6)
    chkbutton35.grid(column=5, row=6)
    chkbutton36.grid(column=6, row=6)

    root.mainloop()


# Print statement to create a loading screen while game loads
print(" LOADING GAME .")
t.sleep(0.5)
print(".")
t.sleep(0.2)
print(".")
t.sleep(0.2)
print(".")
t.sleep(0.2)
print(".")

Game()  # Calls upon the game funtion

# Creating a small Tkinter window to display the credits
root = tk.Tk()
root.wm_title("Credits")
root.configure(background="darkslategray")
root.iconbitmap("game.ico")


ListOfGods = tk.Label(root, bg="antiquewhite", fg="black",
                      text="Designed by Roy George")
ListOfGods.pack(side="top")

MommyItsOverrr = tk.Button(
    root, text="Click here to exit", bd=4, command=Continue)
MommyItsOverrr.pack(side="bottom")

root.mainloop()

print("Thank you for playing....")
t.sleep(1)
print("Play again sometime!")
t.sleep(2)

quit()  # Quits the application
