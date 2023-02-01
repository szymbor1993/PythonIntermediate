import json

from pydantic import BaseModel, validator


# noinspection PyMethodParameters
class DividendOutput(BaseModel):
    foreign_currency: str
    total_amount: float = 0.0
    total_amount_pln: float = 0.0
    foreign_tax_pln: float = 0.0
    tax_to_pay_pln: float = 0.0

    @validator("foreign_currency")
    def currency_three_letter_string(cls, input_str):
        if len(input_str) != 3:
            raise ValueError("Currency need to be in 3-letter ISO-4217 format")
        return input_str

    def pretty_json(self):
        return json.dumps(self.dict(), indent=4)

    def __str__(self):
        return f"Foreign currency: {self.foreign_currency}," \
               f"\nTotal dividend (in {self.foreign_currency}): {self.total_amount}," \
               f"\nTotal dividend (in PLN): {self.total_amount_pln}," \
               f"\nForeign tax payed (in PLN): {self.foreign_tax_pln}," \
               f"\nTax to pay in Poland (in PLN): {self.tax_to_pay_pln}"
