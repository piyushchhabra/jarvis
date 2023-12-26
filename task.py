import sys
from utils import utils
import json
import os
from jobs import run_jobs

full_path = os.path.realpath(__file__)
CURRENT_DIR = os.path.dirname(full_path)


def print_tasks():
    print("Select your task:")
    print("1. test")
    print("2. start_jobs")


def check_min_args(count, msg="Incorrect number of arguments"):
    if len(sys.argv) < count:
        utils.log_fatal_error(msg)


def get_json_file(path):
    with open(path) as f:
        return json.load(f)


def write_json_file(data, filename):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)


def test():
    print("Hello world")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_tasks()
        sys.exit(0)
    task = sys.argv[1]
    utils.log_bold_underline("Task to perform: " + task)

    if task == 'test':
        test()
    elif task == 'start_jobs':
        run_jobs.run()
    else:
        utils.log_error("Unknown task for jarvis. Check available tasks:")
        print_tasks()



