import sys
import time
import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[32m'
    WARNING = '\033[33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEFAULT = '\033[39m'


def sleep_now(seconds):
    print(
        "Sleeping for " + str(seconds) + " seconds | " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    time.sleep(seconds)


def log_success(msg):
    print(bcolors.OKGREEN + msg + bcolors.DEFAULT)


def log_warning(msg):
    print(bcolors.WARNING + msg + bcolors.DEFAULT)


def log_error(msg):
    print(bcolors.FAIL + msg + bcolors.DEFAULT)


def log_fatal_error(msg):
    log_error(msg)
    sys.exit(-1)


def log_bold(msg):
    print(bcolors.BOLD + msg + '\033[0m')


def log_bold_underline(msg):
    print(bcolors.UNDERLINE + bcolors.BOLD + msg + '\033[0m')
