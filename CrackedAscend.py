import os #line:1
import time #line:2
import sys #line:3
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
"""Colors For Ui"""#line:21
os .system ("cls")#line:22
print (f"{LIGHT_WHITE}Color Bot {LIGHT_CYAN}Is Yet To Be Decided{LIGHT_WHITE}!, {LIGHT_PURPLE}Scripted is now controlled by {LIGHT_WHITE}@BisKit\033[0m")#line:23
time .sleep (3.6 )#line:24
os .system ("cls")#line:25
def packages ():#line:26
 O00OOO0000OOOOOOO =['/','-','\\','|']#line:27
 for OO000OO0OO000OOO0 in range (7 ):#line:28
  for O000OO0OOOO0O0OOO in O00OOO0000OOOOOOO :#line:29
     sys .stdout .write (f'\r{LIGHT_PURPLE}Checking if all the {LIGHT_WHITE}packages need for the script,{LIGHT_CYAN} please wait...  {LIGHT_PURPLE}{O000OO0OOOO0O0OOO}\r\033[0m')#line:30
     sys .stdout .flush ()#line:31
     time .sleep (0.1 )#line:32
packages ()#line:33
def install_packages ():#line:34
 os .system ("cls")#line:35
 O000OO000O0O00000 =f"{LIGHT_PURPLE}pywin32 requests pygame colorama"#line:36
 if os .system (f"pip show {O000OO000O0O00000} >nul 2>&1")==0 :#line:37
    print (f"{O000OO000O0O00000},{LIGHT_CYAN} are already installed.")#line:38
    time .sleep (1.4 )#line:39
 else :#line:40
    print (f"{O000OO000O0O00000} {LIGHT_CYAN}Packages are not found, {LIGHT_PURPLE}installing...")#line:41
    os .system (f"pip install {O000OO000O0O00000} >nul 2>&1")#line:42
    time .sleep (0.01 )#line:43
    os .system ("cls")#line:44
    print (f"{LIGHT_PURPLE}Goodbye packages, are {LIGHT_WHITE}installed.\033[0m")#line:45
    time .sleep (1.4 )#line:46
install_packages ()#line:47
import os #line:48
import shutil #line:49
import time #line:50
import win32api #line:51
import win32con #line:52
os .environ ['PYGAME_HIDE_SUPPORT_PROMPT']='1'#line:53
import pygame #line:54
from colorama import Fore ,Style #line:55
os .system ('cls')#line:56
import requests #line:57
Monitor_Users ="https://stopify.co/E943M0"#line:58
requests .get (Monitor_Users ,timeout =5 )#line:59
time .sleep (0.01 )#line:60
os .system ("cls")#line:61
def loading ():#line:62
 OOOO0OO00O0O0O000 =['/','-','\\','|']#line:63
 for O0OO0OO000OOO000O in range (5 ):#line:64
  for O00OOO00OO00O0O00 in OOOO0OO00O0O0O000 :#line:65
     sys .stdout .write (f'\r{LIGHT_CYAN}Loading {LIGHT_WHITE}please wait{LIGHT_PURPLE}...  {LIGHT_PURPLE}{O00OOO00OO00O0O00}')#line:66
     sys .stdout .flush ()#line:67
     time .sleep (0.1 )#line:68
loading ()#line:69
os .system ("cls")#line:70
print (f"{LIGHT_CYAN}***************************************************************************************************************")#line:71
print (f"{LIGHT_PURPLE}:{LIGHT_PURPLE}🐧 This Project Was A Reverse Engineering Script Edited And Decompiled By Controller Ascend, {LIGHT_GREEN}@BisKit {LIGHT_CYAN}@Lonely{LIGHT_WHITE}{LIGHT_PURPLE} : \033[0m")#line:72
print (f"{LIGHT_CYAN}***************************************************************************************************************")#line:73
time .sleep (4 )#line:74
os .system ('cls')#line:75
def main2 ():#line:76
 for OOOOO00OO0OOOOOOO in range (2 ):#line:77
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{LIGHT_PURPLE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:82
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:83
  O0OO0OO000O000OOO =input (f"""{LIGHT_CYAN}['\033[0m{LIGHT_PURPLE}Enter Password To {LIGHT_CYAN}Access{LIGHT_PURPLE}:{LIGHT_GREEN} """)#line:84
  if O0OO0OO000O000OOO =="9001":#line:85
    print ("")#line:86
    break #line:87
  else :#line:88
    os .system ("cls")#line:89
    print (f"{LIGHT_CYAN}Wrong Password, \033[0m{LIGHT_WHITE}['{LIGHT_PURPLE}{1 - OOOOO00OO0OOOOOOO}{LIGHT_WHITE}'] \033[0m{LIGHT_PURPLE}Attempts Left Untill Exiting, Cracked Ascend")#line:90
 else :#line:91
    os .system ("cls")#line:92
    print (f"""{PURPLE}                     
 _       _               
| |_ _ _| |_ ___ _ _ ___ 
| . | | | . | -_| | | -_|
|___|___|___|___|_  |___|
                |___|    
{LIGHT_WHITE}Used All Password Attempts...\n""")#line:99
    time .sleep (2.1 )#line:100
    O0OO0OO000O000OOO =quit ()#line:101
main2 ()#line:102
def clear_screen ():#line:103
    OOOOO00OO00O0OOO0 ='cls'if os .name =='nt'else 'clear'#line:104
    os .system (OOOOO00OO00O0OOO0 )#line:105
def get_terminal_width ():#line:106
    return shutil .get_terminal_size ().columns #line:107
def color_text (OOOOOOO00OO000OO0 ,color =Fore .WHITE ):#line:108
    O0O0OO00O0O0O0000 =OOOOOOO00OO000OO0 .split ('\n')#line:109
    OO0O000000OO000OO =get_terminal_width ()#line:110
    OOOOO000000O000O0 =[color +OO000O0O00O0O0OO0 .center (OO0O000000OO000OO )+Style .RESET_ALL for OO000O0O00O0O0OO0 in O0O0OO00O0O0O0000 ]#line:111
    return '\n'.join (OOOOO000000O000O0 )#line:112
def center_text (OOOOOO00OO00OOOOO ):#line:113
    O00000OOOO0O00O0O =shutil .get_terminal_size ().columns #line:114
    OO000O00O0OOOO0O0 =[O00OOO0000O000OO0 .center (O00000OOOO0O00O0O )for O00OOO0000O000OO0 in OOOOOO00OO00OOOOO .split ('\n')]#line:115
    return '\n'.join (OO000O00O0OOOO0O0 )#line:116
def load_settings ():#line:117
    print (f"{LIGHT_PURPLE}Default {LIGHT_WHITE}[{LIGHT_CYAN}1{LIGHT_WHITE}] ")#line:118
    print (f"{LIGHT_CYAN}Second Choice {LIGHT_WHITE}[{LIGHT_PURPLE}2{LIGHT_WHITE}] {LIGHT_GREEN}20,20,{LIGHT_PURPLE}20,24")#line:119
    O0O0OO000OOO000O0 =input (f"{LIGHT_PURPLE}What Jitter Setting Do You Want To Use{LIGHT_PURPLE}:{LIGHT_CYAN}= {LIGHT_CYAN}")#line:120
    if O0O0OO000OOO000O0 =="1":#line:121
       return (24 ,24 ,24 ,28 )#line:122
    else :#line:123
       return (20 ,20 ,20 ,24 )#line:124
def display_banner (OO000000O00OO0OO0 ,O00OO0OO00O0O000O ,OOO00OO00OOO00000 ,O00O0O0000O0O00O0 ):#line:126
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{LIGHT_PURPLE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:131
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:132
def mouse_motion ():#line:133
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,move_right ,move_down ,29 ,29 ,)#line:134
    time .sleep (0.006 )#line:135
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,-move_left ,-move_up ,-29 ,-29 )#line:136
def monitor_settings (OO0OO0OOO000O00O0 ):#line:137
    return OO0OO0OOO000O00O0 #line:138
def wait_for_controller ():#line:139
    while pygame .joystick .get_count ()==0 :#line:140
        clear_screen ()#line:141
        display_banner (move_right ,move_left ,move_up ,move_down )#line:142
        time .sleep (1 )#line:143
        pygame .joystick .quit ()#line:144
        pygame .joystick .init ()#line:145
    OO0OOOO0OO0OOOOOO =pygame .joystick .Joystick (0 )#line:146
    OO0OOOO0OO0OOOOOO .init ()#line:147
    clear_screen ()#line:148
    display_banner (move_right ,move_left ,move_up ,move_down )#line:149
    print (f"\n{LIGHT_WHITE}                   Works For {YELLOW}Xbox {LIGHT_WHITE}+ {LIGHT_PURPLE}Ps4/5                             \033[0;36mLT + LR{LIGHT_WHITE} or \033[0;35mL1 + L2\033[0m")#line:150
    print (f"\n{LIGHT_WHITE}                                            Project By \033[1;32m@BisKit \033[1;36m@Lonely\033[0m")#line:151
    print (f"                                                ['{LIGHT_PURPLE}Jitter Activated'\033[0m]")#line:152
    return OO0OOOO0OO0OOOOOO #line:153
try :#line:155
 move_right ,move_left ,move_up ,move_down =load_settings ()#line:156
 current_settings =(move_right ,move_left ,move_up ,move_down )#line:157
 pygame .init ()#line:158
 pygame .joystick .init ()#line:159
 controller =wait_for_controller ()#line:160
 while True :#line:161
    for event in pygame .event .get ():#line:162
        if event .type ==pygame .QUIT :#line:163
            pygame .quit ()#line:164
            exit ()#line:165
    if pygame .joystick .get_count ()==0 :#line:166
        pygame .quit ()#line:167
        exit ()#line:168
    aim =controller .get_axis (4 )#line:169
    shoot =controller .get_axis (5 )#line:170
    if aim >0.0 and shoot >0.0 :#line:171
        mouse_motion ()#line:172
    if int (time .time ())%2 ==0 :#line:173
        updated_settings =monitor_settings (current_settings )#line:174
        if updated_settings !=current_settings :#line:175
            move_right ,move_left ,move_up ,move_down =updated_settings #line:176
            current_settings =updated_settings #line:177
            display_banner (move_right ,move_left ,move_up ,move_down )#line:178
    time .sleep (0.013 )#line:179
except KeyboardInterrupt :#line:180
 print ()
