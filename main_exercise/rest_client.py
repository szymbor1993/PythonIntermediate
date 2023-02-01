import datetime

import requests

import constants
from utils import parse_date_str, previous_day

NBP_API_BASE_URL: str = "https://api.nbp.pl/api/exchangerates/rates/A"
PROXIES: dict = {
    "http": "http://proxy-mu.intel.com:911",
    "https": "https://proxy-mu.intel.com:912"
}


class RestError(requests.HTTPError):
    def __init__(self, response):
        self.status_code = response.status_code
        super().__init__(response=response)

    def __str__(self):
        return f"{type(self).__name__}: status code: {self.status_code}" \
               f"\nResponse: {self.response}"


class RestClient:
    def __init__(self, currency: str, output_format="json"):
        if output_format not in ("json", "xml"):
            raise ValueError("Output format can be either 'json' or 'xml'")
        self.currency = currency
        self.base_url = f"{NBP_API_BASE_URL}/{self.currency}"
        self.session = requests.Session()
        self.session.headers.update({"Accept": f"application/{output_format}"})
        # self.session.proxies = PROXIES

    def get_currency_rate_from_previous_working_day(self, date_str: str):
        date_obj = parse_date_str(date_str)
        found_working_day = False
        response = None

        while not found_working_day:
            date_obj = previous_day(date_obj)
            url = f"{self.base_url}/{date_obj.strftime(constants.DATE_FORMAT)}"
            response = self.session.get(url)
            match response.status_code:
                case 200:
                    found_working_day = True
                case 404:
                    continue
                case _:
                    raise RestError(response)

        try:
            rates_obj = response.json().get("rates", [])
            rate = rates_obj[0]["mid"]
            return float(rate)
        except (IndexError, KeyError, ValueError) as ex:
            raise RuntimeError(f"Could not get {self.currency} rate from {date_str}."
                               f"\nDetails: {ex}")
