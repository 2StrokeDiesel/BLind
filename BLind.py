import os
import time

def clear():
    try:
        os.system("clear")
    except:
        pass
    else:
        os.system("cls")
clear()
print("""
     ...     ..            ..    .                     ..
  .=*8888x <"?88h.   x .d88"    @88>                 dF
 X>  '8888H> '8888    5888R     %8P      u.    u.   '88bu.
'88h. `8888   8888    '888R      .     x@88k u@88c. '*88888bu
'8888 '8888    "88>    888R    .@88u  ^"8888""8888"   ^"*8888N
 `888 '8888.xH888x.    888R   ''888E`   8888  888R   beWE "888L
   X" :88*~  `*8888>   888R     888E    8888  888R   888E  888E
 ~"   !"`      "888>   888R     888E    8888  888R   888E  888E
  .H8888h.      ?88    888R     888E    8888  888R   888E  888F
 :"^"88888h.    '!    .888B .   888&   "*88*" 8888" .888N..888
 ^    "88888hx.+"     ^*888%    R888"    ""   'Y"    `"888*""
        ^"**""          "%       ""                     ""

""")

print("------------------------------------------------------------------------------------")
# shits fucked stand by
print("""
 _______ __     __ __               ___              __             __
|     __|  |--.|__|  |_.-----.    .'  _|.--.--.----.|  |--.-----.--|  |
|__     |     ||  |   _|__ --|    |   _||  |  |  __||    <|  -__|  _  |
|_______|__|__||__|____|_____|    |__|  |_____|____||__|__|_____|_____|

        __                  __      __
.-----.|  |_.---.-.-----.--|  |    |  |--.--.--.
|__ --||   _|  _  |     |  _  |    |  _  |  |  |
|_____||____|___._|__|__|_____|    |_____|___  |
                                         |_____|""")

kok = input("""Select Operating system (wont be used for all modules)
1) Windows
2) Mac
3) Linux(Highly Unlikely most of this works and what does will be on fedora)

Input OS:""")
print("""\n \n \n \n""")
koklist =("1", "2", "3" "windows", "Windows", "mac", "Mac", "fedora" "Fedora" "Linux" "linux" "arch" "Arch")
if kok in koklist:
    print("Horray it works")
else:
    clear()
    print("Looks like you entered a invalid input, you may have to restart the script, some issue may occur")
    time.sleep(3)
    clear()

a = input("""Modules:
1) Spamming

2) Cli Programs 

3) Clock

4) File Duplicator

5) Weather

6) Screensaver

98) Experimental

99) Credits

Select a number:""")
print("""\n \n \n \n""")
# Spamming tools
if a == "1" or a == "Spamming" or a == "spamming":
    import pyautogui

    x = input("Text to spam \n:")
    z = int(float(input("Delay, delay between each message being sent, 0.1 is tenth of a second 1 is a second \n:")))
    print("All of these have a 3 second delay before they start")
    y = input("""
1) Discord mode
2) General mode
3) Alarm mode
4) Kamari mode
5) Help \nMode selection:""")
    print("""\n \n \n \n""")
    dislist = ("1", "Discord", "discord", "Discord Mode", "Discord mode", "discord mode")
    if y in dislist:
        clear()
        print("Discord Mode Selected!")
        time.sleep(3)
        pyautogui.click(900, 1000)
        time.sleep(0.3)
        while True:
            pyautogui.typewrite(x)
            time.sleep(z)
            pyautogui.press("enter")
    genmodlist =("2", "General", "general", "General Mode", "general mode", "General mode")
    if y in genmodlist:
        clear()
        print("General Mode Selected!")
        time.sleep(3)
        while True:
            pyautogui.typewrite(x)
            time.sleep(z)
            pyautogui.press("enter")
    kamlist = ("4", "Kamari Mode", "Kamari", "kamari", "kamari mode", "Kamari Mode")
    if y in kamlist:
        time.sleep(3)
        pyautogui.click(900, 1000)
        time.sleep(0.3)
        while True:
            pyautogui.typewrite(x)
            time.sleep(z)
            pyautogui.press("enter")
            pyautogui.press("enter")
    alarmlist =("3", "alarm", "Alarm", "alarm mode", "Alarm mode", "Alarm Mode")
    if y in alarmlist:
        time.sleep(3)
        import datetime
        import time

        print("Hours in 24 hour format!")
        o = input("Hour of start \n:")
        u = input("Minute of start \n:")
        k = input("Number of minutes to spam once started \n:")
        u_int = int(u)
        o_int = int(o)
        k_int = int(k)
        today = datetime.datetime.now()
        sleep = (datetime.datetime(today.year, today.month, today.day, o_int, u_int) - today).seconds
        # This shits works now, I don't remember what I was doing
        print('time till start: ' + str(datetime.timedelta(seconds=sleep)))
        time.sleep(sleep)

        pyautogui.click(900, 1000)
        time.sleep(0.3)
        t_end = time.time() + 60 * k_int
        # things might work now, stfu I fixed it eventually
        while time.time() < t_end:
            pyautogui.typewrite(x)
            time.sleep(z)
            pyautogui.press("enter")

        if y == "5" or y == "Help" or y == "help" or y == "HELP":
            print("""\n \n \n \n""")
        print(
            '//Discord Mode \nThis version clicks on a specific area on the screen (900,1000 for those wondering) and allows for discord to easily be spammed without needing to be clicked on after, this is for 1080p monitors, and given thats what the majority have including me thats what I set it to be for by default though it can always be changed \n \n')
        print(
            "//General Mode \nVery simple module of this spammer, takes input and the time delay and starts repeating typing and enter 3 seconds after the input to start \n \n")
        print(
            "//Alarm Mode \nTakes the user input for a specific time (hours and minutes) of when to start, this is determined by the package datetime which is required for this to work, this time then has the current time subtracted this will give time time until the spam starts, the user is also asked how long to spam, this time is in minutes and is easily controlled by a simple integer entered \n \n")
        print("//Kamari Mode \nSpecial mode for a friend that presses enter twice for japanese keyboards on mac")

# Command line tools / programs
if a == "2" or a == "Cli program" or a == "cli programs" or a == "cli" or a == "Cli":
    import pyautogui
    import os

    pos = input("""
1)spotdl-scripts
2)ping-test
3)yt-dlp-scripts

Select Module:""")
    poslist= ("3", "alarm", "Alarm", "alarm mode", "Alarm mode", "Alarm Mode")
    if pos in poslist:
        pop = input("""File Type:
1) mp3
2) m4a
3) flac
4) Help
Select Format """)
        if pop == "4" or pop == "help" or pop == "Help":
            print("""//Mp3 
Small File size, but lesser quality

//m4a 
Medium file size, better quality

//flac,
compressed lossless, large file size""")

        fax = input("Spotify Link:")
        if pop == "1" or pop == "mp3":
            oop = "spotdl --audio youtube-music --format mp3 download "

        if pop == "2" or pop == "m4a":
            oop = "spotdl --audio youtube-music --format m4a download "

        if pop == "3" or pop == "flac":
            oop = "spotdl --audio youtube-music --format flac download "

        clear()

        pyautogui.press("winleft")
        time.sleep(0.5)
        pyautogui.typewrite("terminal")
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.typewrite(oop + fax)

    if pos == "2" or pos == "Ping-Test" or pos == "ping-test" or pos == "Ping-test" or pos == "Ping" or pos == "ping":
        if kok == "1" or kok == "windows" or kok == "Windows":
            os.system("cls")
            os.system("ping 1.1.1.1 -t")

        if kok == "2" or kok == "3" or kok == "mac" or kok == "Mac" or kok == "Linux" or kok == "linux" or kok == "Ubuntu" or kok == "ubuntu" or kok == "fedora" or kok == "Fedora" or kok == "arch":
            if kok == "arch":
                print("why they fuck are you using this if your on arch?, anyway continue")
                time.sleep(float(0.3))
            os.system("clear")
            os.system("ping 1.1.1.1")

    if pos == "3" or pos == "yt-dlp" or pos == "Yt-dlp":
        clear()
        tot = input("""File type:
1) mp3
2) m4a
3) flac
4) mp4
Select Number:""")
        xof = input("Input link:")
        if tot == "1" or tot == "mp3" or tot == "Mp3":
            fox = " -x --audio-format mp3 "

        if tot == "2" or tot == "m4a" or tot == "M4a":
            fox = " -x --audio-format m4a "

        if tot == "3" or tot == "flac" or tot == "Flac":
            fox = " -x --audio-format flac "

        if tot == "4" or tot == "mp4" or tot == "Mp4":
            fox = " --remux-video mp4"

        clear()

        os.system('yt-dlp' + fox + xof)

# patwang

# This a fuking clock
if a == "3" or a == "Clock" or a == "clock":
    import pyautogui
    import datetime
    import time
    from pyfiglet import Figlet

    if kok == "1" or kok == "Windows" or kok == "windows":
        os.system("cls")
    if kok == "2" or kok == "3" or kok == "mac" or kok == "Mac" or kok == "Linux" or kok == "linux" or kok == "Ubuntu" or kok == "ubuntu" or kok == "fedora" or kok == "Fedora" or kok == "arch":
        os.system("clear")
    while True:
        p = datetime.datetime.now()
        f = (datetime.datetime.strftime(p, '%H : %M : %S'))
        o_u = f
        i = Figlet(font='letters')
        print(i.renderText(o_u), end="")
        print('\033[6A\033[2K', end='')
        time.sleep(1)
        # The \033[5A\033[2K allows for refresh with pyfiglet in without clearing, each font needs a different amount of room for clear so, changing the number 5a will change how many lines
        # it clears, this is something that will be needed to be edited by the eu,but it's not a big deal, maybe figure out a way to fix in future?

        # File Duper
if a == "4" or a == "Duplicator" or a == "file Duplicator" or a == "File Duplicator" or a == "File duplicator" or a == "duper" or a == "file duplicator":
    print("If for some god forsaken reason you need this hats off, here you go \n \n")
    print("File has to be in BLind folder, otherwise idk how its going to work!")
    zyc = input("File Name (NOT EXTENSION!)\n Input Filename:")
    print("\n")
    xyc = input("File extension (Type as .txt or .mp4) *ADD A SPACE ON END \n Input Extension:")
    print("\n")
    xyz = int(input("""How Many Copies?
Input Number:"""))
    print("\n")
    iou = 0
    for iou in range(xyz):
        if kok == "1" or kok == "windows" or kok == "Windows":
            os.system('copy ' + zyc + xyc + zyc + str(iou) + xyc)
        if kok == "linux" or kok == "Linux" or kok == "Ubuntu" or kok == "ubuntu" or kok == "fedora" or kok == "Fedora" or kok == "arch" or kok == "3" or kok == "2" or kok == "Mac" or kok == "mac":
            os.system('cp ' + zyc + xyc + zyc + str(iou) + xyc)
        iou += 1

# Weather
if a == "5" or a == "Weather" or a == "weather":
    import requests

    print("\t\tWelcome to the Weather Forecaster!\n\n")
    print("This uses wttr.in, credit goes to them for this amazing service\n\n")

    city_name = input("Enter the name of the City : ")
    print("\n\n")

# Function to Generate Report
    def Gen_report(C):
        url = 'https://wttr.in/{}'.format(C)
        try:
            data = requests.get(url)
            T = data.text
        except:
            T = "Error Occurred"
        print(T)


    Gen_report(city_name)

if a == "6" or a == "screensaver" or a == "Screensaver":
    import os.path

    iop = os.path.isfile("rain.sh")
    if iop:

        if kok == "1" or kok == "windows" or kok == "Windows":
            os.system("bash rain.sh")

        if kok == "2" or kok == "mac" or kok == "Mac":
            print(
                "currently i have not seen mac with this module working im not sure if its wget/curl or if its the actual .sh script")
            print(
                "https://raw.githubusercontent.com/lbgists/rain.sh/master/rain.sh this is the script that I use for the screensaver, if you get the file in the same folder then you can goahead and try to get this working and uncomment the previous")
            # os.system("sh rain.sh")

        if kok == "linux" or kok == "Linux" or kok == "Ubuntu" or kok == "ubuntu" or kok == "fedora" or kok == "Fedora" or kok == "arch" or kok == "3":
            os.system("chmod +x ./rain.sh")
            os.system("./rain.sh")

    else:
        if kok == "2" or kok == "mac" or kok == "Mac":
            print(
                "currently i have not seen mac with this module working im not sure if its wget/curl or if its the actual .sh script")
            print(
                "https://raw.githubusercontent.com/lbgists/rain.sh/master/rain.sh this is the script that I use for the screensaver, if you get the file in the same folder then you can goahead and try to get this working and uncomment the previous")
            # os.system("sh rain.sh")
        if kok == "1" or kok == "windows" or kok == "Windows":
            os.system("wget https://raw.githubusercontent.com/lbgists/rain.sh/master/rain.sh")
            os.system("bash rain.sh")

        if kok == "linux" or kok == "Linux" or kok == "Ubuntu" or kok == "ubuntu" or kok == "fedora" or kok == "Fedora" or kok == "arch" or kok == "3":
            os.system("wget https://raw.githubusercontent.com/lbgists/rain.sh/master/rain.sh")
            os.system("chmod +x ./rain.sh")
            os.system("./rain.sh")
# some credits likely that these will get slowly updated, something that isn't that important other than something fun to do when I get tired of other stuff
if a == "99" or a == "Credits" or a == "credits":
    import os
    import sys
    import random
    import time

    print("""
  d8b
  ?88
   88b
   888888b ?88   d8P      .d888b, d8888b  88bd88b d888b8b  ?88,.d88b,
   88P `?8bd88   88       ?8b,   d8P' `P  88P'  `d8P' ?88  `?88'  ?88
  d88,  d88?8(  d88         `?8b 88b     d88     88b  ,88b   88b  d8P
 d88'`?88P'`?88P'?8b     `?888P' `?888P'd88'     `?88P'`88b  888888P'
                 )88                                        88P'
                ,d8P                                       d88
             `?888P'                                       ?8P""")
    print("\n")
    words = """Plan for the future
  Live in the present
   Embrace the past"""
    for char in words:
        foo = [0.2, 0.25, 0.1, 0.275, 0.3, 0.5]
        time.sleep(random.choice(foo))
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    # Experimental

if a == "98" or a == "experimental" or a == "Experimental":
    cup = input("""
1) Link scraper
2) I Heart Radio active streaming link scraper
3) Radio
4) beatstars ripper
Input:""")
    if cup == "1" or cup == "Link scraper" or cup == " link scraper":
        import urllib.request
        from bs4 import BeautifulSoup

        com = input("Website url:")
        parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
        resp = urllib.request.urlopen(com)
        soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

        for link in soup.find_all('a', href=True):
            print(link['href'])
    if cup == "2" or cup == "Ihr" or cup == "I heart radio" or cup == "i heart radio" or cup == "I Heart Radio active streaming link scraper":
        print("personal use but can be modified by end user, in experimental as i heart radio scraper")
        i = 0
        import os

        kjo = int(input("How many possibilities? :"))
        okj = input("Output file name : ")
        while i <= kjo:
            os.system('wget --spider --save-headers -nv --append-output ' + str(okj) + '.txt' + ' https://ample.revma.ihrhls.com/zc' + str(i))
            i += 1
    if cup == "3" or cup == "radio" or cup == "Radio":
        import vlc
        import time

        url = "https://ample.revma.ihrhls.com/zc4289"

    # define VLC instance
        instance = vlc.Instance('--fullscreen')

    # Define VLC player
        player = instance.media_player_new()

    # Define VLC media
        media = instance.media_new(url)

    # Set player media
        player.set_media(media)

    # Play the media
        player.play()
        while True:
            pass

    if cup == "4" or cup == "beatstars ripper" or cup == "Beatstars ripper" or cup== "Beatstars Ripper":
        fuckface = input("""beatstars stream link, take (prefix after id)_000.ts OFF!
        input: """)
        bighead = input("prefix: ")
        dickbag = int(input('approximately how many .ts files? (varys per song, each .ts is 10 seconds) : '))
        i = 0
        while i <= dickbag:
            if i < 10:
                os.system('wget -nv ' + str(fuckface) + str(bighead) + "_00" + str(i) + ".ts")
                i += 1
            if i > 9:
                os.system('wget -nv ' + str(fuckface) + str(bighead) + "_0" + str(i) + ".ts")
                i += 1
            if i > 99:
                os.system('wget -nv ' + str(fuckface) + str(bighead) + "_" + str(i) + ".ts")
                i += 1
            if i == dickbag + 1:
                import pyautogui

                pyautogui.confirm("REMOVE ALL .TS FILES (beside song downloaded) FROM BLIND FOLDER, once done press confirm/ ok")
                killmenow = int(input("How many .ts files are there downloaded"))
                Ihatethisgodforsakenwebsite = input("song name")
                ihatethis = input("BLind.py File location")
                twoAM= input("What shell Do you want to use? : ")
                # very obviously can be changed to a single command but i wanted the user to have the option for what shell to use
                itwo = 0
                pyautogui.press("winleft")
                time.sleep(1)
                pyautogui.typewrite(twoAM)
                time.sleep(0.5)
                pyautogui.press("enter")
                time.sleep(2)
                pyautogui.typewrite("cd " + ihatethis)
                pyautogui.press("enter")
                pyautogui.typewrite('ffmpeg -i "concat:')
                while itwo < killmenow:
                    if itwo < 10:
                        pyautogui.typewrite(bighead + "_00" + str(itwo) + ".ts|")
                        itwo += 1

                    if itwo > 9:
                        pyautogui.typewrite(bighead + "_0" + str(itwo) + ".ts|")
                        itwo += 1
                    if itwo == killmenow:
                        pyautogui.typewrite(bighead + '_0' + str(itwo) + '.ts" ')
                        pyautogui.typewrite(Ihatethisgodforsakenwebsite + '.m4a')
                        time.sleep(0.3)
                        pyautogui.press("enter")
                        time.sleep(10)
                        pyautogui.alert("once ffmpeg is done press ok")
                        pyautogui.typewrite('del ' + '*.ts')
                        pyautogui.press('enter')

# https://tinyurl.com/bdfvbf8t
# #peace tea, good shit
# 0150150
# 2297575
# deez nutz signed getz159 1:38am 6/27/23
# I always come back