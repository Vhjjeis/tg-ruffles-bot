import datetime
def get_format_day(value):
    words = ['день', 'дня', 'дней']
    if all((value % 10 == 1, value % 100 != 11)):
        return words[0]
    elif all((2 <= value % 10 <= 4,
            any((value % 100 < 10, value % 100 >= 20)))):
        return words[1]
    return words[2]


def date_to_str(date):
    new_date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M") - datetime.datetime.now()
    d = new_date.days
    h, rem = divmod(new_date.seconds, 3600)
    m, s = divmod(rem, 60)
    
    f = lambda x: str(x).rjust(2, "0")
    str_day = get_format_day(d)
    h, m, s = f(h), f(m), f(s)
    if d != 0:
        return f"{d} {str_day}, {h}:{m}:{s}"
    return f"{h}:{m}:{s}"