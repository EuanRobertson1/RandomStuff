import time
import random

PURPLE = '\033[1;35;48m'
CYAN = '\033[1;36;48m'
BOLD = '\033[1;37;48m'
BLUE = '\033[1;34;48m'
GREEN = '\033[1;32;48m'
YELLOW = '\033[1;33;48m'
RED = '\033[1;31;48m'
BLACK = '\033[1;30;48m'
UNDERLINE = '\033[4;37;48m'
END = '\033[1;37;0m'

i = 0
heh = "-"
while i < 100:
 x = random.randint(1,5)
 heh+= "-"
 if x == 1:
    print(PURPLE + heh + "\n" + END)
 elif x == 2:
    print(BLUE + heh + "\n" + END)
 elif x == 3:
    print(GREEN + heh + "\n" + END)
 elif x == 4:
    print(RED + heh + "\n" + END)   
 elif x == 5:
    print(YELLOW + heh + "\n" + END)   
 time.sleep(0.01)


  