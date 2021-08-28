def split_date(str_input):
    month = int(str_input[0:2])
    date = int(str_input[3:5])
    year = int(str_input[6:])
    return year, month, date


def get_earliest(*dates):
    earliest = dates[0]
    for date in dates:

        date_year, date_month, date_date = split_date(date)
        earliest_year, earliest_month, earliest_date = split_date(earliest)
        print(date_year, earliest_year)
        print(date_month, earliest_month)
        print(date_date, earliest_date)
        if date_year < earliest_year:
            earliest = date
            continue
        elif date_month < earliest_month and date_year == earliest_year:
            earliest = date
            continue
        elif date_date < earliest_date and date_month == earliest_month and date_year == earliest_year:
            earliest = date
            continue
    return earliest
