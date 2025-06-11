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
def packages ():#line:27
 OOO00O00OOO000O0O =['/','-','\\','|']#line:28
 for OOO00O0000OO0O0O0 in range (7 ):#line:29
  for OO000OO00O000OO00 in OOO00O00OOO000O0O :#line:30
     sys .stdout .write (f'\r{LIGHT_PURPLE}Checking if all the {LIGHT_WHITE}packages need for the script,{LIGHT_CYAN} please wait...  {LIGHT_PURPLE}{OO000OO00O000OO00}\r\033[0m')#line:31
     sys .stdout .flush ()#line:32
     time .sleep (0.1 )#line:33
packages ()#line:34
def install_packages ():#line:36
 os .system ("cls")#line:37
 OOOO00O00O0O0OOO0 =f"{LIGHT_PURPLE}pywin32 requests pygame colorama"#line:39
 if os .system (f"pip show {OOOO00O00O0O0OOO0} >nul 2>&1")==0 :#line:41
    print (f"{OOOO00O00O0O0OOO0},{LIGHT_CYAN} are already installed.")#line:42
    time .sleep (1.4 )#line:43
 else :#line:44
    print (f"{OOOO00O00O0O0OOO0} {LIGHT_CYAN}Packages are not found, {LIGHT_PURPLE}installing...")#line:45
    os .system (f"pip install {OOOO00O00O0O0OOO0} >nul 2>&1")#line:46
    time .sleep (0.01 )#line:47
    os .system ("cls")#line:48
    print (f"{LIGHT_PURPLE}Goodbye packages, are {LIGHT_WHITE}installed.\033[0m")#line:49
    time .sleep (1.4 )#line:50
install_packages ()#line:51
import os #line:52
import shutil #line:53
import time #line:54
import win32api #line:55
import win32con #line:56
os .environ ['PYGAME_HIDE_SUPPORT_PROMPT']='1'#line:57
import pygame #line:58
from colorama import Fore ,Style #line:59
os .system ('cls')#line:60
import requests #line:61
Monitor_Users ="https://stopify.co/E943M0"#line:62
requests .get (Monitor_Users ,timeout =5 )#line:63
time .sleep (0.01 )#line:64
os .system ("cls")#line:65
def loading ():#line:66
 O0O0O00O000OO0O0O =['/','-','\\','|']#line:67
 for O0OO0OO0O0OOOO0OO in range (5 ):#line:68
  for OOO000O0OO0OOOO0O in O0O0O00O000OO0O0O :#line:69
     sys .stdout .write (f'\r{LIGHT_CYAN}Loading {LIGHT_WHITE}please wait{LIGHT_PURPLE}...  {LIGHT_PURPLE}{OOO000O0OO0OOOO0O}')#line:70
     sys .stdout .flush ()#line:71
     time .sleep (0.1 )#line:72
loading ()#line:73
os .system ("cls")#line:74
print (f"{BLUE}***************************************************************************************************************")#line:75
print (f"{LIGHT_PURPLE}:{LIGHT_PURPLE}🐧 This Project Was A Reverse Engineering Script Edited And Decompiled By Controller Ascend, {LIGHT_GREEN}@BisKit {LIGHT_CYAN}@Lonely{LIGHT_WHITE}{LIGHT_PURPLE} : \033[0m")#line:76
print (f"{LIGHT_CYAN}***************************************************************************************************************")#line:77
time .sleep (4 )#line:78
os .system ('cls')#line:79
def main2 ():#line:80
 for OO0O000O0O0O00000 in range (2 ):#line:81
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{BLUE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:86
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:87
  OO00O0O0O0OOO00O0 =input (f"""{LIGHT_CYAN}['\033[0m{LIGHT_PURPLE}Enter Password To {LIGHT_CYAN}Access{LIGHT_PURPLE}:{LIGHT_GREEN} """)#line:88
  if OO00O0O0O0OOO00O0 =="9001":#line:89
    print ("")#line:90
    break #line:91
  else :#line:92
    os .system ("cls")#line:93
    print (f"{LIGHT_CYAN}Wrong Password, \033[0m{LIGHT_WHITE}['{LIGHT_PURPLE}{1 - OO0O000O0O0O00000}{LIGHT_WHITE}'] \033[0m{LIGHT_PURPLE}Attempts Left Untill Exiting, Cracked Ascend")#line:94
 else :#line:95
    os .system ("cls")#line:96
    print (f"""{PURPLE}                     
 _       _               
| |_ _ _| |_ ___ _ _ ___ 
| . | | | . | -_| | | -_|
|___|___|___|___|_  |___|
                |___|    
{LIGHT_WHITE}Used All Password Attempts...\n""")#line:103
    time .sleep (2.1 )#line:104
    OO00O0O0O0OOO00O0 =quit ()#line:105
main2 ()#line:106
def clear_screen ():#line:107
    OO0000OO0OO0OO00O ='cls'if os .name =='nt'else 'clear'#line:108
    os .system (OO0000OO0OO0OO00O )#line:109
def get_terminal_width ():#line:110
    return shutil .get_terminal_size ().columns #line:111
def color_text (O0OOO00OO00OOOOOO ,color =Fore .WHITE ):#line:112
    O0OOO0OO0O00000O0 =O0OOO00OO00OOOOOO .split ('\n')#line:113
    O0OO00O0O0OOO0000 =get_terminal_width ()#line:114
    O0OO0O00O0OOO0OOO =[color +OOO00O0O00000OO0O .center (O0OO00O0O0OOO0000 )+Style .RESET_ALL for OOO00O0O00000OO0O in O0OOO0OO0O00000O0 ]#line:115
    return '\n'.join (O0OO0O00O0OOO0OOO )#line:116
def center_text (OO0OO000O0OO0O000 ):#line:117
    O0O00OOOOO00000OO =shutil .get_terminal_size ().columns #line:118
    OO00000O00OOO00OO =[OOO0O000OO0OOOOO0 .center (O0O00OOOOO00000OO )for OOO0O000OO0OOOOO0 in OO0OO000O0OO0O000 .split ('\n')]#line:119
    return '\n'.join (OO00000O00OOO00OO )#line:120
def load_settings ():#line:121
    O0OO0O0O00OOOO00O =24 #line:122
    O0OOO00000OO0OOO0 =24 #line:123
    OO0000OOO00O0O0O0 =24 #line:124
    OO000O00OO0O0OOOO =28 #line:125
    return (O0OO0O0O00OOOO00O ,O0OOO00000OO0OOO0 ,OO0000OOO00O0O0O0 ,OO000O00OO0O0OOOO )#line:126
def display_banner (OOOOOO0O0OO0OOO00 ,OOO0O0OO00OO0OOOO ,OO00OO0OOOO0000OO ,O0O0OOO00O0O00O00 ):#line:127
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{BLUE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:132
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:133
def mouse_motion ():#line:134
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,move_right ,move_down ,29 ,29 ,)#line:135
    time .sleep (0.006 )#line:136
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,-move_left ,-move_up ,-29 ,-29 )#line:137
def monitor_settings (OO0000000O00OO000 ):#line:138
    return OO0000000O00OO000 #line:139
def wait_for_controller ():#line:140
    while pygame .joystick .get_count ()==0 :#line:141
        clear_screen ()#line:142
        display_banner (move_right ,move_left ,move_up ,move_down )#line:143
        time .sleep (1 )#line:144
        pygame .joystick .quit ()#line:145
        pygame .joystick .init ()#line:146
    O00O00OOO0OOO000O =pygame .joystick .Joystick (0 )#line:147
    O00O00OOO0OOO000O .init ()#line:148
    clear_screen ()#line:149
    display_banner (move_right ,move_left ,move_up ,move_down )#line:150
    print (f"\n{LIGHT_WHITE}                   Works For {YELLOW}Xbox {LIGHT_WHITE}+ {LIGHT_PURPLE}Ps4/5                             \033[0;36mLT + LR{LIGHT_WHITE} or \033[0;35mL1 + L2\033[0m")#line:151
    print (f"\n{LIGHT_WHITE}                                            Project By \033[1;32m@BisKit \033[1;36m@Lonely\033[0m")#line:152
    print (f"                                                ['{LIGHT_PURPLE}Jitter Activated'\033[0m]")#line:153
    return O00O00OOO0OOO000O #line:154
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
