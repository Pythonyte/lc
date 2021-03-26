# from threading import Lock
#
# class Singleton:
#     _instances = {}
#     def __new__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             with Lock():
#                 if cls not in cls._instances:
#                     cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instances[cls]
#
# def testThread(num):
#     print("Object value", Singleton())
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         import threading
#         t = threading.Thread(target=testThread, args=[i])
#         t.start()
#
# print(Singleton())
# print(Singleton())
# print(Singleton())

# class C(object):
#     def __init__(self):
#         self._x = None
#
#     @property
#     def x(self):
#         """I'm the 'x' property."""
#         print("getter of x called")
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         print("setter of x called")
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         print("deleter of x called")
#         del self._x
#
#
# c = C()
# print(c.x)
# c.x = 'foo'  # setter called
# foo = c.x    # getter called
# print(c.x)
# del c.x      # deleter called
# print(c.x)


class CustomList:
    def __init__(self,elements=1):
        self._clist = [0]*elements
    def __getitem__(self, index):
        print("Get item called")
        return self._clist[index]
    def __setitem__(self, index, value):
        print("Set item called")
        self._clist[index] = value
    def __str__(self):
        return "111"
obj1 = CustomList(10)
print(repr(obj1))
print(str(obj1))