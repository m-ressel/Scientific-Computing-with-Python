def add_time(start, duration, day=None):
    # splitting start and duration into hour, minute and AM/PM
    [s_hour, s_minute, s_time] = start.replace(' ', ':').split(":")
    [d_hour, d_minute] = duration.replace(' ', ':').split(":")

    # changing previous strings into values
    [s_hour, s_minute] = [int(s_hour), int(s_minute)]
    [d_hour, d_minute] = [int(d_hour), int(d_minute)]

    # 12 AM/PM get separate cases
    if s_time == 'PM' and s_hour != 12:
        s_hour += 12
    if s_hour == 12 and s_time == 'AM':
        s_hour = 0

    # checking how many days and minutes will pass considering the duration
    [e_min, rest] = [(s_minute + d_minute)//60, (s_minute + d_minute) % 60]
    [e_hour, days] = [(s_hour + d_hour + e_min) % 24, (s_hour + d_hour + e_min)//24]

    # checking time of day
    if e_hour >= 12:
        if e_hour > 12:
            e_hour -= 12
        e_time = "PM"
    else:
        if e_hour == 0:
            e_hour = 12
        e_time = "AM"

    # making sure that all single digit minutes will start with 0
    if rest < 10:
        rest = "0"+str(rest)

    new_time = [e_hour, ":", rest, " ", e_time]

    # calculating a weekday based on below dictionary
    if day is not None:
        nr_to_weekday = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            0: "Sunday"
            }
        # reversing previous dictionary
        weekday_to_nr = dict(map(reversed, nr_to_weekday.items()))

        day = nr_to_weekday[(weekday_to_nr[day.capitalize()] + days) % 7]
        new_time = new_time + [", ", day]

    # reporting number of days that passed
    if days > 0:
        if days == 1:
            new_time.append(" (next day)")
        else:
            new_time = new_time + [" (", days, " days later)"]

    return ''.join(map(str, new_time))
