import os
import sys
from utils import utils

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.append(parentdir)


def run():
    while True:
        # invoke a function periodically
        utils.sleep_now(60 * 3)


if __name__ == '__main__':
    utils.sleep_now(60 * 3)