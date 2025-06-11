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
 O00OOO0000OO00000 =['/','-','\\','|']#line:27
 for O0O0OO00O0O0000O0 in range (5 ):#line:28
  for OO0OO00O0OO0O0OO0 in O00OOO0000OO00000 :#line:29
     sys .stdout .write (f'\r{LIGHT_PURPLE}Checking if all the {LIGHT_WHITE}packages need for the script,{LIGHT_CYAN} please wait{LIGHT_WHITE}...  {LIGHT_PURPLE}{OO0OO00O0OO0O0OO0}\r\033[0m')#line:30
     sys .stdout .flush ()#line:31
     time .sleep (0.1 )#line:32
packages ()#line:33
def install_packages ():#line:34
 os .system ("cls")#line:35
 OO0OO000O000O0O0O =f"{LIGHT_PURPLE}pywin32 requests pygame colorama"#line:36
 if os .system (f"pip show {OO0OO000O000O0O0O} >nul 2>&1")==0 :#line:37
    print (f"{OO0OO000O000O0O0O},{LIGHT_CYAN} are already installed.")#line:38
    time .sleep (1.4 )#line:39
 else :#line:40
    print (f"{OO0OO000O000O0O0O} {LIGHT_CYAN}Packages are not found, {LIGHT_PURPLE}installing...")#line:41
    os .system (f"pip install {OO0OO000O000O0O0O} >nul 2>&1")#line:42
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
Monitor_Users ="https://mymap.quest/Z4BV1L"#line:58
requests .get (Monitor_Users ,timeout =5 )#line:59
time .sleep (0.01 )#line:60
os .system ("cls")#line:61
def loading ():#line:62
 O00OOO0OO0OO0OOOO =['/','-','\\','|']#line:63
 for OOOO0OO00O0OOOOO0 in range (5 ):#line:64
  for OO0000O0OOO0O0OOO in O00OOO0OO0OO0OOOO :#line:65
     sys .stdout .write (f'\r{LIGHT_CYAN}Loading {LIGHT_WHITE}please wait{LIGHT_CYAN}...  {LIGHT_PURPLE}{OO0000O0OOO0O0OOO}')#line:66
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
 for O0O0O00OOOO0000O0 in range (2 ):#line:77
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{LIGHT_PURPLE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:82
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:83
  OOO000O000OOOOOO0 =input (f"""{LIGHT_CYAN}['\033[0m{LIGHT_PURPLE}Enter Password To {LIGHT_CYAN}Access{LIGHT_PURPLE}:{LIGHT_GREEN} """)#line:84
  if OOO000O000OOOOOO0 =="9001":#line:85
    print ("")#line:86
    break #line:87
  else :#line:88
    os .system ("cls")#line:89
    print (f"{LIGHT_CYAN}Wrong Password, \033[0m{LIGHT_WHITE}['{LIGHT_PURPLE}{1 - O0O0O00OOOO0000O0}{LIGHT_WHITE}'] \033[0m{LIGHT_PURPLE}Attempts Left Untill Exiting, Cracked Ascend")#line:90
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
    OOO000O000OOOOOO0 =quit ()#line:101
main2 ()#line:102
def clear_screen ():#line:103
    O00O00O00OOO0O0OO ='cls'if os .name =='nt'else 'clear'#line:104
    os .system (O00O00O00OOO0O0OO )#line:105
def get_terminal_width ():#line:106
    return shutil .get_terminal_size ().columns #line:107
def color_text (O0O0O00000OO00OO0 ,color =Fore .WHITE ):#line:108
    O000O0000O0OO000O =O0O0O00000OO00OO0 .split ('\n')#line:109
    O0OO0OO000O0OOO00 =get_terminal_width ()#line:110
    OOO000OO00O000O0O =[color +O0OO00O00OO0O0OOO .center (O0OO0OO000O0OOO00 )+Style .RESET_ALL for O0OO00O00OO0O0OOO in O000O0000O0OO000O ]#line:111
    return '\n'.join (OOO000OO00O000O0O )#line:112
def center_text (OO0OO00OO0000OOO0 ):#line:113
    OOO00O0OOOO00O0OO =shutil .get_terminal_size ().columns #line:114
    OO0OOOO0000OO0O0O =[O0O000000OO000OO0 .center (OOO00O0OOOO00O0OO )for O0O000000OO000OO0 in OO0OO00OO0000OOO0 .split ('\n')]#line:115
    return '\n'.join (OO0OOOO0000OO0O0O )#line:116
def load_settings ():#line:117
    os .system ("cls")#line:118
    print (f"{LIGHT_WHITE}Pick {LIGHT_PURPLE}Default {LIGHT_WHITE}[{LIGHT_CYAN}1{LIGHT_WHITE}] ")#line:119
    print (f"{LIGHT_WHITE}Pick {LIGHT_WHITE}[{LIGHT_CYAN}2{LIGHT_WHITE}] {LIGHT_PURPLE}original jitter{LIGHT_WHITE}({LIGHT_CYAN}Jitter May Be Stronger Then Option {LIGHT_WHITE}one)\033[0m")#line:120
    O00O00OO0OOO0OO00 =input (f"{LIGHT_WHITE}What Jitter Setting, {LIGHT_PURPLE}Do You Want To Use{LIGHT_PURPLE}:{LIGHT_CYAN}= {LIGHT_CYAN}")#line:121
    if O00O00OO0OOO0OO00 =="1":#line:122
       return (24 ,24 ,24 ,28 ,0.013 )#line:123
    else :#line:124
       return (20 ,20 ,20 ,24 ,0.01 )#line:125
def display_banner (OOOO0OOOO0OO000O0 ,O000O0OO0O0OO0OO0 ,O00OOOO0OO00O0O00 ,O0OO0OOOO00OO000O ):#line:127
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{LIGHT_PURPLE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:132
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:133
def mouse_motion ():#line:134
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,move_right ,move_down ,29 ,29 ,)#line:135
    time .sleep (0.006 )#line:136
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,-move_left ,-move_up ,-29 ,-29 )#line:137
def monitor_settings (O0OO0OOOOO00OO000 ):#line:138
    return O0OO0OOOOO00OO000 #line:139
def wait_for_controller ():#line:140
    while pygame .joystick .get_count ()==0 :#line:141
        clear_screen ()#line:142
        display_banner (move_right ,move_left ,move_up ,move_down )#line:143
        time .sleep (1 )#line:144
        pygame .joystick .quit ()#line:145
        pygame .joystick .init ()#line:146
    O0O0OOOO00O00OO0O =pygame .joystick .Joystick (0 )#line:147
    O0O0OOOO00O00OO0O .init ()#line:148
    clear_screen ()#line:149
    display_banner (move_right ,move_left ,move_up ,move_down )#line:150
    print (f"\n{LIGHT_WHITE}                   Works For {YELLOW}Xbox {LIGHT_WHITE}+ {LIGHT_PURPLE}Ps4/5                             \033[0;36mLT + LR{LIGHT_WHITE} or \033[0;35mL1 + L2\033[0m")#line:151
    print (f"\n{LIGHT_WHITE}                                            Project By \033[1;32m@BisKit \033[1;36m@Lonely\033[0m")#line:152
    print (f"                                                ['{LIGHT_PURPLE}Jitter Activated'\033[0m]")#line:153
    return O0O0OOOO00O00OO0O #line:154
try :#line:156
 move_right ,move_left ,move_up ,move_down ,time_sleep =load_settings ()#line:157
 current_settings =(move_right ,move_left ,move_up ,move_down )#line:158
 pygame .init ()#line:159
 pygame .joystick .init ()#line:160
 controller =wait_for_controller ()#line:161
 while True :#line:162
    for event in pygame .event .get ():#line:163
        if event .type ==pygame .QUIT :#line:164
            pygame .quit ()#line:165
            exit ()#line:166
    if pygame .joystick .get_count ()==0 :#line:167
        pygame .quit ()#line:168
        exit ()#line:169
    aim =controller .get_axis (4 )#line:170
    shoot =controller .get_axis (5 )#line:171
    if aim >0.0 and shoot >0.0 :#line:172
        mouse_motion ()#line:173
    if int (time .time ())%2 ==0 :#line:174
        updated_settings =monitor_settings (current_settings )#line:175
        if updated_settings !=current_settings :#line:176
            move_right ,move_left ,move_up ,move_down =updated_settings #line:177
            current_settings =updated_settings #line:178
            display_banner (move_right ,move_left ,move_up ,move_down )#line:179
    time .sleep (time_sleep )#line:180
except KeyboardInterrupt :#line:181
 print ()
