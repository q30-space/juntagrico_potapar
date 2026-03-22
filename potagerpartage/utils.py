import datetime


def next_wednesday():
    # get date of next wednesday
    today = datetime.date.today()
    days = 2 - today.weekday()
    if days <= 0:
        days += 7
    return today + datetime.timedelta(days=days)
