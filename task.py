import sys
import utils


def print_tasks():
    print("Select your task:")
    print("1. Test Here")


def check_min_args(count, msg="Incorrect number of arguments"):
    if len(sys.argv) < count:
        utils.log_fatal_error(msg)


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
    else:
        utils.log_error("Unknown task for jarvis. Check available tasks:")
        print_tasks()



