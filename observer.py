from abc import ABCMeta, abstractmethod

class Observable(metaclass=ABCMeta):
    def __init__(self):
        self.state = None
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def get_state(self):
        return self.state

    @abstractmethod
    def set_state(self, state):
        pass

class Observer(metaclass=ABCMeta):
    def __init__(self, observable):
        self.observable = observable

    @abstractmethod
    def update(self):
        pass


## An example of chat room
## User can enter into chat room or exit from chat room
## chat room will notify every user if any new event occur (new msg came, new call came)
## User can take action on that event

class Chatroom(Observable):
    allowed_states = [
        'idle',
        'msg',
        'call',
    ]
    def set_state(self, state):
        if state in self.allowed_states:
            self.state = state
            self.notify()

class User(Observer):
    def __init__(self, observable, name):
        super().__init__(observable)
        self.name = name

    def update(self):
        event = self.observable.get_state()
        self.act_on_event(event)

    def act_on_event(self, event):
        print("{} got {}".format(self.name, event))

    def send_message(self):
        self.observable.set_state('msg')

    def do_call(self):
        self.observable.set_state('call')

## Driver Code
if __name__ == '__main__':
    chat_room = Chatroom()
    sumit, ankur, sankalp = User(chat_room, 'sumit'), User(chat_room, 'ankur'), User(chat_room, 'sankalp')
    chat_room.subscribe(sumit)
    chat_room.subscribe(ankur)
    sumit.send_message()
