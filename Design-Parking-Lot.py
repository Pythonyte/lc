"""
Design a parking lot with the following interface:
1. GetNumberOfAvailableSlots()
2. GetSlotForCar(string carNumber)
3. GetCarInSlot(Slot x)
4. AddCar(string carNumber)
5. RemoveCar(string carNumber)
"""

class ParkingLot:
    def __init__(self, slots=5, level=5):
        self.slots = slots
        self.cars_in_slots = {}
        self.slots_for_cars = [[None] * slots for _ in  range(level)]
        # Slot numbers: Ex [4,3,2,1,0]
        # in reverse order, so that nearest slot 0..1..2 can be easily picked at 0(1) by pop
        self.available_slots = list(range(slots-1, -1, -1))

    def get_number_of_available_slots(self):
        count = len(self.available_slots)
        print("total available_slots {}".format(count))
        return count

    def __get_available_slots(self):
        return self.available_slots

    def get_slot_for_car(self, car):
        return self.cars_in_slots.get(car, "Wrong Car information")

    def get_car_in_slot(self, slot):
        if 0 < slot < self.slots:
            return self.slots_for_cars[slot]
        print("{} Wrong Slot information".format(slot))
        return

    def __remove_slot_from_available_slots(self):
        self.available_slots.pop()

    def __add_slot_in_available_slots(self, used_slot):
        self.available_slots.append(used_slot)
        # sorting in reverse oreder, so that nearest slot will get picked
        self.available_slots = sorted(self.available_slots, reverse=True)

    def add_car(self, car):
        if self.available_slots is None:
            print("No Slot Available for {}".format(car))
            return
        if car in self.cars_in_slots:
            print("{} Car Already Parked".format(car))
            return

        # get slot for parking
        slot = self.available_slots[-1]

        # fill info in mappings
        self.cars_in_slots[car] = slot
        self.slots_for_cars[slot] = car

        # remove slot from available_slots list
        self.__remove_slot_from_available_slots()
        print("{} parked at slot {}".format(car, slot))

    def remove_car(self, car):
        if car not in self.cars_in_slots:
            print("{} Car not available".format(car))
            return

        used_slot = self.cars_in_slots[car]
        del self.cars_in_slots[car]
        self.slots_for_cars[used_slot] = None
        self.__add_slot_in_available_slots(used_slot)
        print("{} exited from slot {}".format(car, used_slot))

    def get_details(self):
        print("*"*30)
        print("cars_in_slots {}".format(self.cars_in_slots))
        print("slots_for_cars {}".format(self.slots_for_cars))
        print("available_slots {}".format(self.available_slots))
        print("*" * 30)


### Driver Code ####
pl = ParkingLot()
pl.get_number_of_available_slots()
pl.add_car('UP01')
pl.add_car('DL01')
pl.add_car('DL04')
pl.add_car('DL04')
pl.get_details()
pl.get_number_of_available_slots()
pl.remove_car('HR55')
pl.remove_car('DL01')
pl.remove_car('DL04')
pl.add_car('HR55')
pl.add_car('HR57')
pl.get_details()



"""
###################OUTPUT############
total available_slots 5
UP01 parked at slot 0
DL01 parked at slot 1
DL04 parked at slot 2
DL04 Car Already Parked
******************************
cars_in_slots {'UP01': 0, 'DL01': 1, 'DL04': 2}
slots_for_cars ['UP01', 'DL01', 'DL04', None, None]
available_slots [4, 3]
******************************
total available_slots 2
HR55 Car not available
DL01 exited from slot 1
DL04 exited from slot 2
HR55 parked at slot 1
HR57 parked at slot 2
******************************
cars_in_slots {'UP01': 0, 'HR55': 1, 'HR57': 2}
slots_for_cars ['UP01', 'HR55', 'HR57', None, None]
available_slots [4, 3]
******************************
"""
