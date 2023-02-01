import datetime

import constants


def parse_date_str(date_str: str):
    try:
        return datetime.datetime.strptime(date_str, constants.DATE_FORMAT)
    except ValueError:
        raise ValueError(f"Date should be in format "
                         f"'{constants.DATE_FORMAT_HUMAN_READABLE}'")


def previous_day(date_obj: datetime.datetime):
    return date_obj - datetime.timedelta(days=1)
