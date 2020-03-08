# Given a ratio of values like dollar/inr = 70, inr/euro = 50 and euro/yen = 40….and a new input like (dollar,yen)…
# find the value of dollar/yen if it exists.
#

class ConversionRatio:
    def __init__(self):
        self.mapping = {}

    def set_mapping(self, currency_from, currency_to, value):
        if currency_from not in self.mapping:
            self.mapping[currency_from] = {}
        self.mapping[currency_from].update(
            {
                currency_to: value
            },
        )

    def get_conversion(self, currency_from, currency_to):
        total_amount = None

        def helper(currency, amount):
            if currency == currency_to:
                nonlocal total_amount
                total_amount = amount
                return
            if currency in self.mapping:
                for curr, val in self.mapping[currency].items():
                    helper(curr, amount*val)

        helper(currency_from, 1)
        print(self.mapping)
        print(currency_from, currency_to, total_amount)
        return total_amount

cr = ConversionRatio()
cr.set_mapping('dollar', 'inr', 70)
cr.set_mapping('dollar', 'aed', 3)
cr.set_mapping('inr', 'euro', 50)
cr.set_mapping('euro', 'yen', 40)
cr.get_conversion('dollar','dgdf')
cr.get_conversion('dollar','yen')
cr.get_conversion('dollar','euro')
cr.get_conversion('euro','yen')
cr.get_conversion('inr','yen')
# {'dollar': {'aed': 3, 'inr': 70}, 'euro': {'yen': 40}, 'inr': {'euro': 50}}

