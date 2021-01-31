import datetime

now = datetime.datetime.now()

Morning_Shift_Start = now.replace(hour = 7, minute = 0, second = 0)
Morning_Shift_End = now.replace(hour = 11, minute = 0, second = 0)

McD_Shift2_Start = now.replace(hour = 11, minute = 0, second = 1)
McD_Shift2_End = now.replace(hour = 23, minute = 59, second = 59)

Shift2_Start = now.replace(hour = 11, minute = 0, second = 1)
Shift2_End = now.replace(hour = 21, minute = 30, second = 0)

morn_start_str = Morning_Shift_Start.strftime("%H:%M")
morn_end_str = Morning_Shift_End.strftime("%H:%M")

mcd_shift2_start_str = McD_Shift2_Start.strftime("%H:%M")
mcd_shift2_end_str = McD_Shift2_End.strftime("%H:%M")

shift2_start_str = Shift2_Start.strftime("%H:%M")
shift2_end_str = Shift2_End.strftime("%H:%M")
