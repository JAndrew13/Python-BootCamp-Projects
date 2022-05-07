# TODO: Consider using `dataclasses` or `attrs`:
# import dataclasses
# import datetime
# from decimal import Decimal

# @dataclasses.dataclass
# class FlightData:
#     price: Decimal
#     origin_city: str
#     origin_airport: str
#     destination_city: str
#     destination_airport: str
#     out_date: datetime.date
#     return_date: datetime.date
#     stop_overs: int = 0
#     var_city: str = ""

class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = 0
        self.var_city = ""
