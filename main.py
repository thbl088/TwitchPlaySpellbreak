import socket
import threading
import time
from ahk import AHK
from ahk.window import Window

# Video where the source came from https://www.youtube.com/watch?v=uE_3RRBz3CQ&t=5s

# Ugly instructions : https://docs.google.com/document/d/1LGs13SgsaOYEQk_goI6dFfop_HU8w08j-32pwY7Ctps/edit?usp=sharing

# Download Autohotkey at https://www.autohotkey.com/ and provide the address to
# AutoHotkey.exe below!
ahk = AHK(executable_path='')

SERVER = "irc.twitch.tv"
PORT = 6667

# Your OAUTH Code Here https://twitchapps.com/tmi/
PASS = ""

# What you'd like to name your bot
BOT = ""

# The channel you want to monitor
CHANNEL = ""

# Your account
OWNER = ""

message = ""
user = ""
sub = ""
vip = ""
mod = ""
team = ""  # Red and Blue
streamer = ""  # You

irc = socket.socket()

irc.connect((SERVER, PORT))
irc.send(("PASS " + PASS + "\n" +
          "NICK " + BOT + "\n" +
          "JOIN #" + CHANNEL + "\n").encode())


def gamecontrol():
    global message
    global sub
    global vip
    global mod
    global team
    global streamer

    def setPerms():
        # perms for subs
        if sub:
            for perm in subPerms:
                perms[perm] = 1

        # perms for vip
        if vip:
            for perm in vipPerms:
                perms[perm] = 1

        # perms for mods
        if mod:
            for perm in modPerms:
                perms[perm] = 1

        if streamer:
            for perm in streamerPerms:
                perms[perm] = 1

        # perms for team blue of the prediction (choice 1)
        if team == "Blue":
            for perm in bluePerms:
                perms[perm] = 1

        # perms for team red of the prediction (choice 2)
        if team == "Red":
            for perm in redPerms:
                perms[perm] = 1

        # perms for peoples without teams during prediction
        if team == "None":
            for perm in nonePerms:
                perms[perm] = 1

        if user == "th_mrow":
            for perm in perms:
                perms[perm] = 1

    # All the key we're allowing to hold
    holdKeysList = ['w', 'a', 's', 'd', 'space']
    # The separator used after the hold for holding
    separator = "-"
    # The maximum time we're allowing someone to hold a key, in second (float). To hold you need to do hold-key-time
    maxTimeHold = 1.5


    perms = {
        'hold': 0,  # hold wasd space (holdKeysList
        'movement': 0,  # press wasd
        'sorcery': 0,
        'shot': 0,
        'loot': 0,  # press f
        'rune': 0,
        'dodge': 0,
        'levitate': 0,  # jump and levitate
        'inventory': 0,
        'drop': 0,  # change your keys in game or here, y->drop1, u->drop2, h->drop3, j->drop4
        'emote': 0,
        'mouse': 0,  # not finish
        'other': 0,  # nothing for now
        'abuse': 0,
        'picross': 0
    }

    # Choose what peoples are allowed to do
    normalUserPerms = ['loot', 'rune', 'dodge', 'levitate', 'inventory']
    subPerms = ['movement', 'shot', 'sorcery', 'drop']
    vipPerms = ['hold', 'movement',  'shot', 'sorcery', 'drop', 'emote', 'other']  # everything
    modPerms = ['hold', 'movement',  'shot', 'sorcery', 'drop', 'emote', 'other']  # everything
    streamerPerms = [
                     'loot', 'rune', 'dodge', 'levitate', 'inventory', 'hold',
                     'movement',  'shot', 'sorcery', 'drop', 'emote',
                     'mouse', 'other', 'abuse', 'picross'
                     ]  # absolutely everything
    bluePerms = []
    redPerms = []
    nonePerms = []

    while True:

        # perms for everyone
        for perm in normalUserPerms:
            perms[perm] = 1

        setPerms()
        # print(ahk.mouse_position)

        # movement
        if perms['movement']:
            if "w" == message.lower():  # message send
                ahk.key_press('w')  # key press, i'll not repeat those
                message = ""  # Without that we never stop until a new message.

            if "s" == message.lower():
                ahk.key_press('s')
                message = ""

            if "a" == message.lower():
                ahk.key_press('a')
                message = ""

            if "d" == message.lower():
                ahk.key_press('d')
                message = ""

        # sorcery
        if perms['sorcery']:
            if "q" == message.lower():
                ahk.key_press('q')
                message = ""

            if "e" == message.lower():
                ahk.key_press('e')
                message = ""

        # loot
        if perms['loot']:
            if "f" == message.lower():
                ahk.key_press('f')
                message = ""

        # shooting
        if perms['shot']:
            if "l" == message.lower():
                ahk.key_press('LButton')
                message = ""

            if "r" == message.lower():
                ahk.key_press('RButton')
                message = ""

        # jump and levitate
        if perms['levitate']:
            if "space" == message.lower():
                ahk.key_press('Space')
                message = ""

            if "levitate" == message.lower():
                ahk.key_down('Space', blocking=False)
                time.sleep(1.3)
                ahk.key_up('Space', blocking=False)
                message = ""

        # Dodge
        if perms['dodge']:
            if "ctrl" == message.lower():
                ahk.key_press('Ctrl')
                message = ""

        # Rune
        if perms['rune']:
            if "shift" == message.lower():
                ahk.key_press('Shift')
                message = ""

        # Drink potions
        if perms['inventory']:
            if "1" == message.lower():
                ahk.key_press('1')
                message = ""

            if "2" == message.lower():
                ahk.key_press('2')  # ascii code of é for the azerty version : 0233
                message = ""

            if "3" == message.lower():
                ahk.key_press('3')
                message = ""

            if "4" == message.lower():
                ahk.key_press('4')
                message = ""

        # Drop potions
        if perms['drop']:
            if "drop1" == message.lower():
                ahk.key_press('y')
                message = ""

            if "drop2" == message.lower():
                ahk.key_press('u')
                message = ""

            if "drop3" == message.lower():
                ahk.key_press('h')
                message = ""

            if "drop4" == message.lower():
                ahk.key_press('j')
                message = ""

        # Hold keys
        if message != "":
            arg = message.count(separator)
            if 0 <= arg < 3:
                messageArgs = message.split(separator, arg)
            else:
                messageArgs = message

            if perms['hold']:
                if "hold" == messageArgs[0]:
                    isIn = holdKeysList.count(messageArgs[1])
                    if isIn == 1:

                        # if messageArgs[1] == 'w':
                        #     input = 'z'
                        # elif messageArgs[1] == 'a':
                        #     input = 'q'
                        # else:
                        #     input = messageArgs[1]

                        ahk.key_down(input, blocking=False)
                        if arg == 2 and maxTimeHold >= float(messageArgs[2]) >= 0:
                            time.sleep(float(messageArgs[2]))
                        else:
                            time.sleep(1)
                        ahk.key_up(input, blocking=False)

                    message = ""
            if perms['picross']:
                if "lClick" == messageArgs[0]:
                    print(arg)
                    valsTable = {'x': 767, 'y': 360, 'spacingX': 60, 'spacingY': 60}
                    if arg == 2:
                        ahk.mouse_move(x=valsTable['x']+(int(messageArgs[1])*valsTable['spacingX']),
                                       y=valsTable['y']+(int(messageArgs[2])*valsTable['spacingY']), blocking=True
                                       )
                        ahk.key_press('LButton')
                    message = ""

                if "rClick" == messageArgs[0]:
                    print(arg)
                    valsTable = {'x': 767, 'y': 360, 'spacingX': 60, 'spacingY': 60}
                    if arg == 2:
                        ahk.mouse_move(x=valsTable['x']+(int(messageArgs[1])*valsTable['spacingX']),
                                       y=valsTable['y']+(int(messageArgs[2])*valsTable['spacingY']), blocking=True
                                       )
                        ahk.key_press('RButton')
                    message = ""

        # Use an emote
        if perms['emote']:
            if "emote" == message.lower():
                ahk.key_down('g', blocking=False)
                ahk.key_press('LButton')
                ahk.key_up('g', blocking=False)
                message = ""

        # Move your mouse
        if perms['mouse']:
            # print(ahk.mouse_position)
            def looseFocus():
                win = Window(ahk, ahk_id='0x20050')
                win.activate()
            def recenterMouse():
                #sb = ahk.active_window
                sb = ahk.win_get(title='Spellbreak')
                sb.disable()
                looseFocus()
                ahk.mouse_move(x=1920/2, y=1080/2, blocking=False)  # Blocks until mouse finishes moving (the default)
                sb.enable()
                sb.activate()


            if "test0" == message.lower():
                mousePos = ahk.mouse_position
                print(mousePos)
                recenterMouse()
                print(mousePos)
                message = ""

            if "test1" == message.lower():
                mousePos = ahk.mouse_position
                recenterMouse()
                print(mousePos)
                ahk.mouse_move(x=mousePos[0] + 300, y=mousePos[1], blocking=True)
                print(mousePos)
                recenterMouse()
                print(mousePos)
                ahk.mouse_move(x=mousePos[0] + 300, y=mousePos[1], blocking=True)
                recenterMouse()
                print(mousePos)
                message = ""

            if "pos" == message.lower():
                mousePos = ahk.mouse_position
                print(mousePos)
                message = ""

            if "right" == message.lower():
                mousePos = ahk.mouse_position
                print(mousePos)

                ahk.mouse_position[0] = 1920/2
                ahk.mouse_move(x=mousePos[0] + 1750, y=mousePos[1], blocking=True)  # Blocks until mouse finishes moving (the default)
                ahk.mouse_position[0] = 1920 / 2
                ahk.mouse_move(x=mousePos[0] + 1750, y=mousePos[1],
                               blocking=True)  # Blocks until mouse finishes moving (the default)
                ahk.mouse_position[0] = 1920 / 2
                ahk.mouse_move(x=mousePos[0] + 1750, y=mousePos[1],
                               blocking=True)  # Blocks until mouse finishes moving (the default)

                mousePos = ahk.mouse_position
                print(mousePos)
                message = ""

            if "left" == message.lower():
                mousePos = ahk.mouse_position
                print(mousePos)

                ahk.mouse_move(x=mousePos[0] - 1750, y=mousePos[1], blocking=True)  # Blocks until mouse finishes moving (the default)
                mousePos = ahk.mouse_position
                print(mousePos)
                message = ""

            if "up" == message.lower():
                mousePos = ahk.mouse_position
                print(mousePos)

                ahk.mouse_move(x=mousePos[0], y=mousePos[1] - 1080, blocking=True)  # Blocks until mouse finishes moving (the default)
                mousePos = ahk.mouse_position
                print(mousePos)
                message = ""

            if "down" == message.lower():
                mousePos = ahk.mouse_position
                print(mousePos)

                ahk.mouse_move(x=mousePos[0], y=mousePos[1] + 1080, blocking=True)  # Blocks until mouse finishes moving (the default)
                mousePos = ahk.mouse_position
                print(mousePos)
                message = ""

            if "back" == message.lower():
                mousePos = ahk.mouse_position
                print(mousePos)

                ahk.mouse_move(x=mousePos[0] + 1750, y=mousePos[1], blocking=True)  # Blocks until mouse finishes moving (the default)
                ahk.mouse_move(x=mousePos[0] + 1750, y=mousePos[1], blocking=True)
                mousePos = ahk.mouse_position
                print(mousePos)
                message = ""

            if "360" == message.lower():
                mousePos = ahk.mouse_position

                ahk.mouse_move(x=mousePos[0] + 1920, y=mousePos[1], blocking=True)  # Blocks until mouse finishes moving (the default)
                ahk.mouse_move(x=mousePos[0] + 1920, y=mousePos[1], blocking=True)
                mousePos = ahk.mouse_position
                print(mousePos)
                message = ""

            if "reset" == message.lower():
                mousePos = ahk.mouse_position
                print(mousePos)

                ahk.mouse_move(x=1920/2, y=1080/2, blocking=True)  # Blocks until mouse finishes moving (the default)
                mousePos = ahk.mouse_position
                print(mousePos)
                message = ""

        if perms['abuse']:
            if "double shot" == message.lower():
                ahk.key_press('LButton')
                ahk.key_down('RButton')
                ahk.key_down('Ctrl')
                ahk.key_press('LButton')
                ahk.key_up('RButton')
                ahk.key_up('Ctrl')

                message = ""

            if "self explosion" == message.lower():
                ahk.key_down('LButton')
                time.sleep(0.2)
                ahk.key_down('RButton')
                time.sleep(0.3)
                ahk.key_down('d')
                time.sleep(0.1)
                ahk.key_down('Ctrl')
                time.sleep(0.0)
                ahk.key_up('Ctrl')
                time.sleep(0.0)
                ahk.key_press('LButton')
                time.sleep(0.0)
                ahk.key_up('RButton')
                ahk.key_up('d')
                message = ""






def twitch():
    global user
    global message
    global sub
    global vip
    global mod
    global team
    global streamer

    def joinchat():
        Loading = True
        while Loading:
            readbuffer_join = irc.recv(1024)
            readbuffer_join = readbuffer_join.decode()
            print(readbuffer_join)
            for line in readbuffer_join.split("\n")[0:-1]:
                Loading = loadingComplete(line)

    def loadingComplete(line):
        if ("End of /NAMES list" in line):
            print("TwitchBot has joined " + CHANNEL + "'s Channel!")
            sendMessage(irc, "Mrow!")
            return False
        else:
            return True

    def sendMessage(irc, message):
        messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
        irc.send((messageTemp + "\n").encode())

    def getUser(line):
        # global user

        colons = line.count(":")
        colonless = colons - 1
        separate = line.split(":", colons)
        user = separate[colonless].split("!", 1)[0]
        return user

    def getMessage(line):
        # global message
        try:
            colons = line.count(":")
            message = (line.split(":", colons))[colons]
        except:
            message = ""
        return message

    def getSub(line):
        # global sub
        colons = line.count(";")
        separate = line.split(";", colons)
        sub = separate[10].split("=", 1)[1]
        return sub

    def getVip(line):
        # global sub
        colons = line.count(";")
        separate = line.split(";", colons)
        vip = separate[1].split("=", 1)[1].count("vip")
        return vip

    def getMod(line):
        # global sub
        colons = line.count(";")
        separate = line.split(";", colons)
        mod = separate[1].split("=", 1)[1].count("moderator")
        return mod

    def getStreamer(line):
        # global streamer
        colons = line.count(";")
        separate = line.split(";", colons)
        streamer = separate[1].split("=", 1)[1].count("broadcaster")
        return streamer

    def getPredictTeam(line):
        # global team
        colons = line.count(";")
        separate = line.split(";", colons)
        if separate[1].split("=", 1)[1].count("blue-1"):
            team = "Blue"
        elif separate[1].split("=", 1)[1].count("pink-2"):
            team = "Red"
        else:
            team = "None"
        return team

    def console(line):
        if "PRIVMSG" in line:
            return False
        else:
            return True

    joinchat()
    irc.send("CAP REQ :twitch.tv/tags\r\n".encode())
    while True:
        try:
            readbuffer = irc.recv(1024).decode()
        except:
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            if "PING :tmi.twitch.tv" in line:
                msgg = "PONG :tmi.twitch.tv\r\n".encode()
                irc.send(msgg)
                print(msgg)
                continue
            else:
                try:
                    user = getUser(line)
                    message = getMessage(line)

                    sub = getSub(line)
                    vip = getVip(line)
                    mod = getMod(line)
                    team = getPredictTeam(line)
                    streamer = getStreamer(line)
                    print(user + " : " + message)
                except Exception:
                    pass


def main():
    if __name__ == '__main__':
        t1 = threading.Thread(target=twitch)
        t1.start()
        t2 = threading.Thread(target=gamecontrol)
        t2.start()


main()
