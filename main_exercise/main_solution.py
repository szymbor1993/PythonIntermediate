import argparse

import constants
from input_manager import InputManager
from models import DividendOutput
from rest_client import RestClient


def calculate_dividend_tax(input_json_file: str) -> DividendOutput:
    input_data = InputManager.load_input(input_json_file)
    output_data = DividendOutput(foreign_currency=input_data.currency)
    difference_tax_rate: float = constants.POLISH_TAX_RATE - input_data.tax_rate
    if difference_tax_rate < 0.0:
        difference_tax_rate = 0.0

    client = RestClient(input_data.currency)
    for entry in input_data.dates:
        rate_to_pln = client.get_currency_rate_from_previous_working_day(entry.date)
        amount_pln = entry.amount * rate_to_pln

        output_data.total_amount += entry.amount
        output_data.total_amount_pln += amount_pln
        output_data.foreign_tax_pln += amount_pln * input_data.tax_rate
        output_data.tax_to_pay_pln += amount_pln * difference_tax_rate

    _round_results(output_data)
    return output_data


def _round_results(output_data: DividendOutput):
    output_data.total_amount = round(output_data.total_amount, 2)
    output_data.total_amount_pln = round(output_data.total_amount_pln, 2)
    output_data.foreign_tax_pln = round(output_data.foreign_tax_pln, 2)
    output_data.tax_to_pay_pln = round(output_data.tax_to_pay_pln, 2)


if __name__ == "__main__":
    parsed = argparse.ArgumentParser(description="Calculate polish tax from foreign "
                                                 "dividend")
    parsed.add_argument("input_file",
                        help="Input file in JSON format. See 'input_schema.json' "
                             "for reference",
                        type=str
                        )
    parsed.add_argument("-o", "--output_format", required=False, type=str,
                        help="Output format, by default console",
                        choices=["console", "json"], default="console")
    args = parsed.parse_args()

    output = calculate_dividend_tax(args.input_file)
    if args.output_format == "json":
        print(output.pretty_json())
    else:
        print(str(output))
