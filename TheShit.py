try:
    import pygame
except:
    import pip
    pip.main(["install", "pygame"])
    import pygame
try:
    from pyfirmata import Arduino, util, SERVO
except:
    import pip
    pip.main(["install", "pyfirmata"])
    from pyfirmata import Arduino, util, SERVO
import sys
import time
from tkinter import messagebox
import tkinter as tk
#import tkinter.font as tkFont
#import subprocess
from pygame.locals import *

# ----------config----------- #
height = 700                  #
width = 600                   #
degree = 180                  #
arduinoBoard = "COM3"         #
# -----------cons------------ #
BLACK = (0, 0, 0)             #
GREEN = (0, 255, 0)           #
BLUE = (0, 0, 255)            #
RED = (255, 0, 0)             #
WHITE = (255, 255, 255)       #
GREY = (20, 20, 20)           #
GREY1 = (26, 26, 26)          #
initialPos = 0                #
finalPos = degree             #
# -----------fps------------- #
FRAME_RATE = 60               #
# --------------------------- #
degreeMiddle = degree/2


class Shit:

    def __init__(self, mainsurface, board):
        self.main_surface = mainsurface
        pygame.init()
        self.percentToAngleX = 0
        self.percentToAngleY = 0
        self.board = board


    """def selected(serialSelection, root):
        arduinoBoard = serialSelection.get(ANCHOR)
        root.destroy()
        print("\narduino bord linked to port ", arduinoBoard, "...\n")
        return"""


    def hardware(self):
        self.board.digital[9].write(self.percentToAngleX)
        time.sleep(0.01)
        self.board.digital[10].write(self.percentToAngleY)
        time.sleep(0.01)


    def print_mouse_coordinates(self, mainFont, mainClock):
        # ---------background---------- #
        self.main_surface.fill(GREY)

        # ------get mouse position----- #
        #       position_z = "493"
        position_x, position_y = pygame.mouse.get_pos()
        #       posImport = [positionX, positionY, positionZ]    #export data

        # -----percentage of pos----- #
        percentageMX = (position_x / height) * 100
        percentageMY = (position_y / width) * 100

        self.percentToAngleX = (percentageMX / 100) * degree
        self.percentToAngleY = (percentageMY / 100) * degree

        self.percentToAngleX = round(int(self.percentToAngleX), 0)
        self.percentToAngleY = round(int(self.percentToAngleY), 0)

        percentageMX = round(percentageMX, 2)
        percentageMY = round(percentageMY, 2)
        # --------------------------- #
        percentToAngleMX = mainFont.render(str(self.percentToAngleX), 1, WHITE)
        percentToAngleMY = mainFont.render(str(self.percentToAngleY), 1, WHITE)

        self.main_surface.blit(percentToAngleMX, (140, 20))
        self.main_surface.blit(percentToAngleMY, (140, 40))
        # --------------------------- #
        porcentageX = mainFont.render(str(percentageMX), 1, WHITE)
        porcentageY = mainFont.render(str(percentageMY), 1, WHITE)

        self.main_surface.blit(porcentageX, (80, 20))
        self.main_surface.blit(porcentageY, (80, 40))
        # --------------------------- #

        # ---print mouse position---- #
        mouse_label_x = mainFont.render(str(position_x), 1, WHITE)
        mouse_label_y = mainFont.render(str(position_y), 1, WHITE)
        #       mouse_label_z = mainFont.render(str(position_z), 1, WHITE)
        mouse_x = mainFont.render("X:", 1, WHITE)
        mouse_y = mainFont.render("Y:", 1, WHITE)
        #       mouse_z = mainFont.render("Z:", 1, WHITE)
        hm = mainFont.render("nightmare", 1, GREY1)
        self.main_surface.blit(mouse_label_x, (30, 20))
        self.main_surface.blit(mouse_label_y, (30, 40))
        #       self.main_surface.blit(mouse_label_z, (30, 60))
        self.main_surface.blit(mouse_x, (10, 20))
        self.main_surface.blit(mouse_y, (10, 40))
        #       self.main_surface.blit(mouse_z, (10, 60))
        self.main_surface.blit(hm, (601, 576))
        # --------------------------- #
        pygame.draw.line(self.main_surface, RED,(0, position_y), (height, position_y), 2)
        pygame.draw.line(self.main_surface, GREEN, (position_x, 0), (position_x, width), 2)
        pygame.draw.circle(self.main_surface, BLUE, (position_x + 1, position_y + 1), 4, 0)
        # --------------------------- #
        # x, y = pygame.mouse.get_pos()
        # x -= width # // 2
        # y -= height # // 2
        # self.main_surface.blit(rc, (x, y))
        # --------------------------- #
        mainClock.tick(FRAME_RATE)
        pygame.display.update()
        # --------------------------- #


    def exitHardware(self):
        pygame.quit()
        """self.board.digital[11].write(0)"""
        self.board.digital[9].write(degreeMiddle)
        #for count in range(FRAME_RATE/2):
        verticalAngle = round(self.percentToAngleY)
        if self.percentToAngleY > 30:
            while verticalAngle != 30:
                verticalAngle -= 1
                self.board.digital[10].write(verticalAngle)
                time.sleep(0.015)
        else:
            while verticalAngle != 30:
                verticalAngle += 1
                self.board.digital[10].write(verticalAngle)
                time.sleep(0.015)
        time.sleep(0.15)


    def exitApplication():
        #root.destroy()
        pygame.quit()
        sys.exit()

    
    """def fire(self, firecheck):
        self.board.digital[11].write(40)
            

    def ceasefire(self, firecheck):
        self.board.digital[11].write(0)"""


def main():
    pygame.init()
    mainFont = pygame.font.SysFont("Consolas", 18)
    mainClock = pygame.time.Clock()
    main__surface = pygame.display.set_mode((height + 1, width + 1), 0, 32)
    pygame.display.set_caption("NIGHTMARE   NIGHTMARE   NIGHTMARE   NIGHTMARE   NIGHTMARE   NIGHTMARE   NIGHTMARE")

    """# ------Board selection------ #
    data = subprocess.check_output(['chgport']).decode('utf-8').split('\n')
    results=[line.split("''")[0][3:4] for line in data if "COM" in line]
    #cPorts = int(results[0])

    root = tk.Tk()
    root.title("Ports")
    def_font = tk.font.nametofont("TkDefaultFont")
    def_font.config(size=12)
    root.geometry("300x200")

    comLabel = Label(root, text = "SELECT ARDUINO SERIAL PORT:")
    comLabel.pack(pady = 5)

    comScroll = Scrollbar(root)
    comScroll.pack(side = RIGHT, fill = Y)

    serialSelection = Listbox()
    for lines in results:
        serialSelection.insert(lines, "COM" + str(results[0]))
    serialSelection.pack(padx = 5, pady = 10, side = LEFT, fill = BOTH)

    #selection = Shit.selected(serialSelection, root)
    Button(root, text='Select', command=Shit.selected(serialSelection, root)).pack(pady = 20)

    comScroll.config(command = serialSelection.yview)
    root.resizable(False, False)
    root.mainloop()"""
    # --------------------------- #

    board = Arduino(arduinoBoard)
    myShit = Shit(main__surface, board)
    # --------board load--------- #
    board.digital[9].mode = SERVO
    board.digital[10].mode = SERVO
    """board.digital[11].mode = SERVO"""
    iterator = util.Iterator(board)
    iterator.start()
    pin9 = board.get_pin("d:9:o")
    print("\nServo X attached to: ", pin9)
    pin10 = board.get_pin("d:10:o")
    print("\nServo Y attached to: ", pin10)
    board.digital[9].write(degree/2)
    board.digital[10].write(degree/2)
    """ try:
        pin11 = board.get_pin("d:11:o")
        print("\nServo Fire attached to: ", pin11, "\n")
        board.digital[11].write(0)
    except:
        firecheck = True"""
    time.sleep(8)
    """except:
        root = tk.Tk()
        root.withdraw()
        MsgBox = tk.messagebox.askquestion ('Run anyways','Board not found. Run anyways?',icon = 'warning')
        firecheck = True
        if MsgBox == 'no':
            Shit.exitApplication(root, MsgBox)"""
    # -------action loop--------- #
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                myShit.exitHardware()
                Shit.exitApplication()
            if event.type == MOUSEMOTION:
                myShit.print_mouse_coordinates(mainFont, mainClock)
                #if MsgBox == True:
                myShit.hardware()

main()
