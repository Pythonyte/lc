class Foo:
    class_attr = "I'm a class attribute!"

    def __init__(self):
        self.dict_attr = "I'm in a dict!"

    @property
    def property_attr(self):
        return "I'm a read-only property!"

    def __getattr__(self, item):
        return "I'm dynamically returned!"

    def my_getattribute(self, item):
        if item in self.__class__.__dict__:
            print('Retrieving from self.__class__.__dict__')
            v = self.__class__.__dict__[item]
        elif item in self.__dict__:
            print('Retrieving from self.__dict__')
            v = self.__dict__[item]
        else:
            print('Retrieving from self.__getattr__')
            v = self.__getattr__(item)
        if hasattr(v, '__get__'):
            import pdb;pdb.set_trace()
            print("Invoking descriptor's __get__")
            v = v.__get__(self, type(self))
        return v

# if __name__ == '__main__':
#     # https://amir.rachum.com/blog/2019/10/16/descriptors/
#
#     foo = Foo()
#     # print(foo.class_attr)
#     # print()
#     # print(foo.dict_attr)
#     # print()
#     # print(foo.property_attr)
#     # print()
#     # print(foo.dynamic_attr)
#     # print()
#     # print(foo.my_getattribute('class_attr'))
#     # print()
#     # print(foo.my_getattribute('dict_attr'))
#     print()
#     print(foo.my_getattribute('property_attr'))
#     print()
#     print(foo.my_getattribute('dynamic_attr'))

"""
def __getattribute__(self, item):
  if item in self.__class__.__dict__:
    v = self.__class__.__dict__[item]
  elif item in self.__dict__:
    v = self.__dict__[item]
  else:
    v = self.__getattr__(item)
  if hasattr(v, '__get__'):
    v = v.__get__(self, type(self))
  return v
"""

class Descriptor:
    def __init__(self):
        self.__fuel_cap = 0
    def __get__(self, instance, owner):
        return self.__fuel_cap
    def __set__(self, instance, value):
        print("Setter called", instance, value)
        self.__fuel_cap = value
    def __delete__(self, instance):
        del self.__fuel_cap

class Car:
    fuel_cap = Descriptor()
    def __init__(self,make,model,fuel_cap):
        self.make = make
        self.model = model
        self.fuel_cap = fuel_cap

car = Car("BMW","X7",40)
print(car)
