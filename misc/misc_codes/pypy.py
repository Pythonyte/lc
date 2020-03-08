class custom_str:
    def __init__(self, val):
        self.val = val

    def lower(self):
        return 'Lower' + self.val.lower()

for item in [custom_str('Sumit'), 'Singhal']:
    print(item.lower())

val1 = 3
val2 = custom_str

