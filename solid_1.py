# Association

class Manager:
    def __init__(self, name):
        self.name = name
        self.is_valid = None
    def get_name(self):
        return self.name
    def login(self, sc):
        sc.swipe(self)
        return self.is_valid

class SwipeCard:
    def __init__(self, card_no):
        self.card_no = card_no
    def get_card_no(self):
        return self.card_no
    def swipe(self, manager):
        manager.is_valid = True
        print(manager.name, manager.is_valid)

m1 = Manager("Sumit")
sc1 = SwipeCard(123)
m1.login(sc1)