from datetime import datetime, date

def birthday_msg(username, date):
    date = "2021-08-01"
    user_dob = datetime.strptime(date, '%Y-%m-%d')

    today = datetime.today().strftime('%Y-%m-%d')
    today_date = datetime.strptime(today, '%Y-%m-%d')

    if today_date == user_dob:
        msg = f"Hello, {username}! Happy birthday!"
    else:
        ndays = countdiff(user_dob, today_date)
        msg = f"Hello, {username}! Your birthday is in {ndays} day(s)"

    json_msg = { "message": msg}
    return json_msg


def countdiff(user_dob, today_date):
    birthday = date(user_dob.year, user_dob.month, user_dob.day)
    today = date(today_date.year, today_date.month, today_date.day)
    delta = today - birthday
    return delta.days