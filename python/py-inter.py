"""
Python Intervalometer
"""

__author__ = "Zach Hannum"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import serial
import time
import sys

BULB_ON_COMMAND = b'\xff'
BULB_OFF_COMMAND = b'\x64'

def main(args):
    srl = serial.Serial(args.port)
    time.sleep(args.delay)
    print("Starting shots...")
    shot_num = 1
    while(shot_num != args.num + 1):
        try:
            print("Shot " + str(shot_num) + "...")
            srl.write(BULB_ON_COMMAND)
            time.sleep(args.long)
            srl.write(BULB_OFF_COMMAND)
            time.sleep(args.interval)
            shot_num += 1
        except KeyboardInterrupt:
            srl.write(BULB_OFF_COMMAND)
            break
    sys.exit()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--delay", help="Delay before starting in seconds, defaults to 0", default=0, type=int)
    parser.add_argument("-l", "--long", help="Length of shots in seconds, defaults to 0", default=0, type=int)
    parser.add_argument("-i", "--interval", help="Interval between shots in seconds, defaults to 0", default=0, type=int)
    parser.add_argument("-n", "--num", help="Number of shots, defaults to infinity", default=-1, type=int)
    parser.add_argument("-p", "--port", help="Serial port the device is on")

    args = parser.parse_args()
    main(args)