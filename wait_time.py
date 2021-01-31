import math


def McD_time(num):
    try:
        num_ppl = int(num)
        queue_time = 2.4 * num_ppl
        wt = math.floor(queue_time)
        return str(wt) + " Minutes of Waiting \ntime."

    except ValueError:
        error_msg = "Incorrect Data Type!"
        return error_msg


def WS_time(num):
    try:
        num_ppl = int(num)
        queue_time = 1.3 * num_ppl
        wt = math.floor(queue_time)
        return str(wt) + " Minutes of Waiting \ntime."

    except ValueError:
        error_msg = "Incorrect Data Type!"
        return error_msg


def CR_time(num):
    try:
        num_ppl = int(num)
        queue_time = 1.5 * num_ppl
        wt = math.floor(queue_time)
        return str(wt) + " Minutes of Waiting \ntime."

    except ValueError:
        error_msg = "Incorrect Data Type!"
        return error_msg


def NS_time(num):
    try:
        num_ppl = int(num)
        queue_time = 1.9 * num_ppl
        wt = math.floor(queue_time)
        return str(wt) + " Minutes of Waiting \ntime."

    except ValueError:
        error_msg = "Incorrect Data Type!"
        return error_msg


def MS_time(num):
    try:
        num_ppl = int(num)
        queue_time = 0.9 * num_ppl
        wt = math.floor(queue_time)
        return str(wt) + " Minutes of Waiting \ntime."

    except ValueError:
        error_msg = "Incorrect Data Type!"
        return error_msg
