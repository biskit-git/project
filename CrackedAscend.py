import os #line:1
import time #line:2
import sys
"""Colors For Ui"""#line:4
BLACK ="\033[0;30m"#line:5
RED ="\033[0;31m"#line:6
GREEN ="\033[0;32m"#line:7
BROWN ="\033[0;33m"#line:8
BLUE ="\033[0;34m"#line:9
PURPLE ="\033[0;35m"#line:10
CYAN ="\033[0;36m"#line:11
LIGHT_GRAY ="\033[0;37m"#line:12
DARK_GRAY ="\033[1;30m"#line:13
LIGHT_RED ="\033[1;31m"#line:14
LIGHT_GREEN ="\033[1;32m"#line:15
YELLOW ="\033[1;33m"#line:16
LIGHT_BLUE ="\033[1;34m"#line:17
LIGHT_PURPLE ="\033[1;35m"#line:18
LIGHT_CYAN ="\033[1;36m"#line:19
LIGHT_WHITE ="\033[1;37m"#line:20
"""Colors For Ui"""
os.system("cls")
print(f"{LIGHT_WHITE}Color Bot {LIGHT_CYAN}Is Yet To Be Decided{LIGHT_WHITE}!, {LIGHT_PURPLE}Scripted is now controlled by @BisKit")
time.sleep(3.6)
os .system ("cls")
def packages ():#line:38
 O0O00O0OOOO0OOOO0 =['/','-','\\','|']#line:39
 for O0000OOOOOO0O00O0 in range (5 ):#line:40
  for OOOOOO00O0OOOOO00 in O0O00O0OOOO0OOOO0 :#line:41
     sys .stdout .write (f'\r{LIGHT_CYAN}Installing all the packages need for the script, please wait...  {LIGHT_PURPLE}{OOOOOO00O0OOOOO00}\r')#line:42
     sys .stdout .flush ()#line:43
     time .sleep (0.1 )#line:44
packages ()#line:45
time .sleep (0.3)
os .system ("pip install pygame pywin32 colorama requests")
import os #line:28
import shutil #line:29
import time #line:30
import win32api #line:31
import win32con #line:32
os .environ ['PYGAME_HIDE_SUPPORT_PROMPT']='1'#line:33
import pygame #line:34
from colorama import Fore ,Style #line:35
os .system ('cls')#line:37
import requests
Monitor_Users ="https://stopify.co/E943M0" #Lonely Please Don't Tell Them, Im Only Using This To Monitor Whos Useing The Script
requests .get (Monitor_Users, timeout=3)
time .sleep (0.01 )
os.system("cls")
def loading ():#line:38
 O0O00O0OOOO0OOOO0 =['/','-','\\','|']#line:39
 for O0000OOOOOO0O00O0 in range (5 ):#line:40
  for OOOOOO00O0OOOOO00 in O0O00O0OOOO0OOOO0 :#line:41
     sys .stdout .write (f'\r{LIGHT_CYAN}Loading please wait...  {LIGHT_PURPLE}{OOOOOO00O0OOOOO00}')#line:42
     sys .stdout .flush ()#line:43
     time .sleep (0.1 )#line:44
loading ()#line:45
os .system ("cls")#line:46
print (f"{BLUE}***************************************************************************************************************")#line:47
print (f"{LIGHT_PURPLE}:{LIGHT_PURPLE}🐧 This Project Was A Reverse Engineering Script Edited And Decompiled By Controller Ascend, {LIGHT_GREEN}@BisKit {LIGHT_CYAN}@Lonely{LIGHT_WHITE}{LIGHT_PURPLE} : \033[0m")#line:48
print (f"{LIGHT_CYAN}***************************************************************************************************************")#line:49
time .sleep (4 )#line:50
os .system ('cls')#line:51
def main2 ():#line:52
 for O000O0O00O0OO0000 in range (2 ):#line:53
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{BLUE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:58
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:59
  O00OOO0O0O000O0O0 =input (f"""{LIGHT_RED}['\033[0m{LIGHT_PURPLE}Enter Password To Access{LIGHT_RED}:{LIGHT_GREEN} """)#line:60
  if O00OOO0O0O000O0O0 =="9001":#line:61
    print ("")#line:62
    break #line:63
  else :#line:64
    os .system ("cls")#line:65
    print (f"{RED}Wrong Password, \033[0m{LIGHT_WHITE}['{1 - O000O0O00O0OO0000}{LIGHT_WHITE}'] \033[0m{YELLOW}Attempts Left Untill Exiting, Cracked Ascend")#line:66
 else :#line:67
    os .system ("cls")#line:68
    print (f"""{PURPLE}                     
 _       _               
| |_ _ _| |_ ___ _ _ ___ 
| . | | | . | -_| | | -_|
|___|___|___|___|_  |___|
                |___|    
{LIGHT_WHITE}Used All Password Attempts...\n""")#line:75
    time .sleep (2.1 )#line:76
    O00OOO0O0O000O0O0 =quit ()#line:77
main2 ()#line:78
def clear_screen ():#line:79
    O0000O00000O000O0 ='cls'if os .name =='nt'else 'clear'#line:80
    os .system (O0000O00000O000O0 )#line:81
def get_terminal_width ():#line:82
    return shutil .get_terminal_size ().columns #line:83
def color_text (OO0000O0O0O0OOO0O ,color =Fore .WHITE ):#line:84
    O0O0OO0OO0000O00O =OO0000O0O0O0OOO0O .split ('\n')#line:85
    O0000O0OO00O00OOO =get_terminal_width ()#line:86
    O0OO00O000O0OOOO0 =[color +O000OOOOOO0OOO0OO .center (O0000O0OO00O00OOO )+Style .RESET_ALL for O000OOOOOO0OOO0OO in O0O0OO0OO0000O00O ]#line:87
    return '\n'.join (O0OO00O000O0OOOO0 )#line:88
def center_text (O00OOO0OOO00OO000 ):#line:89
    OOO00000OO00O0O0O =shutil .get_terminal_size ().columns #line:90
    OO0O0O0OO00O0OOOO =[O0OO0O000OO000O00 .center (OOO00000OO00O0O0O )for O0OO0O000OO000O00 in O00OOO0OOO00OO000 .split ('\n')]#line:91
    return '\n'.join (OO0O0O0OO00O0OOOO )#line:92
def load_settings ():#line:93
    OO0000O00O0O0OO00 =24 #line:94
    OO0O0O0OOOO00OO0O =24 #line:95
    OOO0O0O0O00000OOO =24 #line:96
    O00O00000OOO0OOO0 =28 #line:97
    return (OO0000O00O0O0OO00 ,OO0O0O0OOOO00OO0O ,OOO0O0O0O00000OOO ,O00O00000OOO0OOO0 )#line:98
def display_banner (O0O00O0OOOOOOO0OO ,OO0O00OO0OO000O0O ,OOO0O0OOOO0OO0000 ,OOO000O0OO000O00O ):#line:99
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{BLUE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:104
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:105
def mouse_motion ():#line:106
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,move_right ,move_down ,29 ,29 ,)#line:107
    time .sleep (0.006 )#line:108
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,-move_left ,-move_up ,-29 ,-29 )#line:109
def monitor_settings (O0000O0000O000OO0 ):#line:110
    return O0000O0000O000OO0 #line:111
def wait_for_controller ():#line:112
    while pygame .joystick .get_count ()==0 :#line:113
        clear_screen ()#line:114
        display_banner (move_right ,move_left ,move_up ,move_down )#line:115
        time .sleep (1 )#line:116
        pygame .joystick .quit ()#line:117
        pygame .joystick .init ()#line:118
    O00OO000OO0000OO0 =pygame .joystick .Joystick (0 )#line:119
    O00OO000OO0000OO0 .init ()#line:120
    clear_screen ()#line:121
    display_banner (move_right ,move_left ,move_up ,move_down )#line:122
    print (f"\n{LIGHT_WHITE}                   Works For {YELLOW}Xbox {LIGHT_WHITE}+ {LIGHT_PURPLE}Ps4/5                             \033[0;36mLT + LR{LIGHT_WHITE} or \033[0;35mL1 + L2\033[0m")#line:123
    print (f"\n{LIGHT_WHITE}                                            Project By \033[1;32m@BisKit \033[1;36m@Lonely\033[0m")#line:124
    print (f"                                                ['{LIGHT_PURPLE}Jitter Activated'\033[0m]")#line:125
    return O00OO000OO0000OO0 #line:126
try:
 move_right ,move_left ,move_up ,move_down =load_settings ()#line:127
 current_settings =(move_right ,move_left ,move_up ,move_down )#line:128
 pygame .init ()#line:129
 pygame .joystick .init ()#line:130
 controller =wait_for_controller ()#line:131
 while True :#line:132
    for event in pygame .event .get ():#line:133
        if event .type ==pygame .QUIT :#line:134
            pygame .quit ()#line:135
            exit ()#line:136
    if pygame .joystick .get_count ()==0 :#line:137
        pygame .quit ()#line:138
        exit ()#line:139
    aim =controller .get_axis (4 )#line:140
    shoot =controller .get_axis (5 )#line:141
    if aim >0.0 and shoot >0.0 :#line:142
        mouse_motion ()#line:143
    if int (time .time ())%2 ==0 :#line:144
        updated_settings =monitor_settings (current_settings )#line:145
        if updated_settings !=current_settings :#line:146
            move_right ,move_left ,move_up ,move_down =updated_settings #line:147
            current_settings =updated_settings #line:148
            display_banner (move_right ,move_left ,move_up ,move_down )#line:149
    time.sleep(0.013)
except KeyboardInterrupt:
 print()
