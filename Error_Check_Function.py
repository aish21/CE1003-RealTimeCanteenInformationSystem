def error_check_day(val):
    days = ('Monday', 'monday', 'Tuesday', 'tuesday', 'Wednesday', 'wednesday',
            'Thursday', 'thursday', 'Friday', 'friday', 'Saturday', 'saturday', 'Sunday', 'sunday')
    if val != days:
        error_msg = "Incorrect input!"
        return error_msg


def error_check_hrs(val):
    hours_list = ["%.2d" % x for x in range(25)]
    if val != hours_list:
        error_msg = "Incorrect input!"
        return error_msg


def error_check_mins(val):
    minutes_list = ["%.2d" % x for x in range(61)]
    if val != minutes_list:
        error_msg = "Incorrect input!"
        return error_msg


