import requests
import time
import os

logo = """

 ▄████████    ▄█    █▄       ▄████████    ▄████████    ▄████████ 
███    ███   ███    ███     ███    ███   ███    ███   ███    ███ 
███    █▀    ███    ███     ███    █▀    ███    █▀    ███    ███ 
███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    █▄    ███    ███     ███    █▄    ███    █▄  ▀███████████ 
███    ███   ███    ███     ███    ███   ███    ███   ███    ███ 
████████▀    ███    █▀      ██████████   ██████████   ███    ███ 
                                                      ███    ███ 
"""

def purple(text):
    os.system("")
    faded = ""
    down = False

    for line in text.splitlines():
        red = 40
        for character in line:
            if down:
                red -= 3
            else:
                red += 3
            if red > 254:
                red = 255
                down = True
            elif red < 1:
                red = 30
                down = False
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
    return faded

def red(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 250
        for character in line:
            green -= 5
            if green < 0:
                green = 0
            faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
        faded += "\n"
    return faded

def blue(text):
    os.system(""); faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 3
            if green > 255:
                green = 255
            faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        faded += "\n"
    return faded

def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded



def padToCenter(l:list,w:int)->str:
    """Manual centering"""
    padding =  ' '*(w//2) 
    parts = [ padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)


def padToCenter2(l:list,w:int)->str:
    return '\n'.join('-'+x.center(w)+'-' for x in l)

width = os.get_terminal_size().columns
print(water(padToCenter(logo.splitlines(),60)))
print(purple("> Ip Scraper by cheer#0001".center(width)))

print("\n")
choice = input(purple("     Input IP > "))


req = requests.get("http://ip-api.com/json/{}".format(choice)).json()

ipinfo = f"""
     IP > {req["query"]}
     Country > {req["country"]}
     City > {req["city"]}
     ZIP > {req["zip"]}
     Internet Provider > {req["isp"]}
"""

print("\n")
print(water(ipinfo))
input()
