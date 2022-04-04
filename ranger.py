"""
Summary:
    Filter a list of dates based on the date range
"""
from datetime import date, datetime, timedelta


def gen_dates():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 3, 30)
    delta = end_date - start_date
    dates = []
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        dates.append(day.strftime("%Y%m%d"))
    return dates


def date_in_range(date: str, from_date: str, to_date: str) -> bool:
    date_fmt = "%Y%m%d"
    date = datetime.strptime(date, date_fmt)
    from_date = datetime.strptime(from_date, date_fmt)
    to_date = datetime.strptime(to_date, date_fmt)
    if from_date <= date <= to_date:
        return True
    return False


def filter_dates_by_range(dates: list[str], from_date: str, to_date: str) -> list[str]:
    return list(filter(lambda x: date_in_range(x, "20220201", "20220317"), dates))


if __name__ == "__main__":
    dates = gen_dates()
    filtered_dates = filter_dates_by_range(dates, "20220201", "20220317")
    print(filtered_dates)
