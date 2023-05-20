import pyautogui
import time

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
#shits fucked stand by

print("Same shit, use this as you will \n \n")
a = input ( "Modules: Spamming, Cli Programs  \n" )
if a==("Spamming"):
  x = input("Text to spam \n:")
  z = input("Delay, delay between each message being sent, 0.1 is tenth of a second 1 is a second \n:")
  y = input(" General mode,  Discord mode,  Alarm mode,  Kamari mode \nMode selection:")
  
  if y ==("Discord"):
    pyautogui.click(900,1000)
    time.sleep(0.3)
    while True:
        pyautogui.typewrite((x))
        time.sleep((z))
        pyautogui.press("enter")

  if y ==("general"): 
    while True:
        pyautogui.typewrite((x))
        time.sleep((z))
        pyautogui.press("enter")

  if y == ("Kamari mode"):
    pyautogui.click(900,1000)
    time.sleep(0.3)
    while True:
        pyautogui.typewrite((x))
        time.sleep((z))
        pyautogui.press("enter")
        pyautogui.press("enter")        

  if y ==("Alarm"):
    import datetime, time
    print("Hours in 24 hour format!")
    o = input("Hour of start \n:")
    u = input("Minute of start \n:")
    k = input("Number of minutes to spam once started \n:")
    u_int = int(u)
    o_int = int(o)
    k_int = int(k)
    today = datetime.datetime.now()
    sleep = (datetime.datetime(today.year, today.month, today.day, (o_int),(u_int)) - today).seconds
    #This shits works now, i feel bad for people that might eventually work on this, may god be on your side, even i dont remember what I was doing 
    print('time till start: ' + str(datetime.timedelta(seconds=sleep)))
    time.sleep(sleep)
    
    pyautogui.click(900,1000)
    time.sleep(0.3)
    t_end = time.time() + 60*(k_int)
    #things might work now, stfu i fixed it eventually 
    while time.time() < t_end:
      pyautogui.typewrite((x))
      time.sleep((z))
      pyautogui.press("enter")
#your mother likes this program
if a ==("Cli Programs") or ("cli programs"):
  pyautogui.click(150,1060)
  time.sleep(0.5)
  pyautogui.typewrite (" command prompt ")
  pyautogui.press("enter")
  time.sleep(1)
  pyautogui.typewrite ('spotdl --audio youtube-music --format flac download ')

