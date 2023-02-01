from typing import Dict, List, TypeAlias

from pydantic import BaseModel, validator

from models import DividendInput, DividendOutput


# noinspection PyMethodParameters
class TestData(BaseModel):
    input: DividendInput
    rates: List[float]
    expected_output: DividendOutput

    @validator("rates")
    def rates_len_should_equal_to_input_rates_len(cls, value: List[float], values) \
            -> List[float]:
        if len(value) != len(values["input"].dates):
            raise ValueError("'Rates' needs to have the same number of elements as "
                             "'dates' in input data")
        return value


TestCaseData: TypeAlias = Dict[str, TestData]


def strip_test_prefix(module_name: str) -> str:
    return module_name.replace("test_", "")
