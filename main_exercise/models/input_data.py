from typing import List

from pydantic import BaseModel, validator

from utils import parse_date_str


# noinspection PyMethodParameters
class DividendEntry(BaseModel):
    date: str
    amount: float

    @validator("date")
    def date_should_be_datetime(cls, input_str):
        parse_date_str(input_str)
        return input_str


# noinspection PyMethodParameters
class DividendInput(BaseModel):
    currency: str
    tax_rate: float
    dates: List[DividendEntry]

    @validator("currency")
    def currency_three_letter_string(cls, input_str):
        if len(input_str) != 3:
            raise ValueError("Currency need to be in 3-letter ISO-4217 format")
        return input_str
