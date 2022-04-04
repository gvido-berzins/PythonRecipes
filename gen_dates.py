"""
Summary:
    Generate a list of dates between a certain range
"""
from datetime import date, timedelta


def gen_dates(start_date, end_date):
    delta = end_date - start_date  # returns timedelta
    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        print(day.strftime("%Y%m%d"))


def main():
    start_date = date(2022, 1, 1)
    end_date = date(2022, 3, 14)  # perhaps date.now()
    gen_dates(start_date, end_date)


if __name__ == "__main__":
    main()
