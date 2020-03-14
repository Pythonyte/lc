from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Publisher(ABC):
    """
    The Publisher interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, Subscriber) -> None:
        """
        Attach an Subscriber to the Publisher.
        """
        pass

    @abstractmethod
    def detach(self, Subscriber) -> None:
        """
        Detach an Subscriber from the Publisher.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all Subscribers about an event.
        """
        pass


class ConcretePublisher(Publisher):
    """
    The Publisher owns some important state and notifies Subscribers when the state
    changes.
    """

    _state = None
    _Subscribers = []

    def attach(self, Subscriber) -> None:
        print("Publisher: Attached an Subscriber.")
        self._Subscribers.append(Subscriber)

    def detach(self, Subscriber) -> None:
        self._Subscribers.remove(Subscriber)

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Publisher: Notifying Subscribers...")
        for Subscriber in self._Subscribers:
            Subscriber.update(Publisher)

    def some_business_logic(self):
        """
        Usually, the subscription logic is only a fraction of what a Publisher can
        really do. Publishers commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nPublisher: I'm doing something important.")
        self._state = randrange(0, 10)

        print("Publisher: My state has just changed to: {self._state}")
        self.notify()


class Subscriber(ABC):
    """
    The Subscriber interface declares the update method, used by Publishers.
    """
    @abstractmethod
    def update(self, Publisher) -> None:
        """
        Receive update from Publisher.
        """
        pass


"""
Concrete Subscribers react to the updates issued by the Publisher they had been
attached to.
"""


class ConcreteSubscriberA(Subscriber):
    def update(self, Publisher) -> None:
        if Publisher._state < 3:
            print("ConcreteSubscriberA: Reacted to the event")


class ConcreteSubscriberB(Subscriber):
    def update(self, Publisher) -> None:
        if Publisher._state == 0 or Publisher._state >= 2:
            print("ConcreteSubscriberB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    Publisher = ConcretePublisher()

    Subscriber_a = ConcreteSubscriberA()
    Publisher.attach(Subscriber_a)

    Subscriber_b = ConcreteSubscriberB()
    Publisher.attach(Subscriber_b)

    Publisher.some_business_logic()
    Publisher.some_business_logic()

    Publisher.detach(Subscriber_a)

    Publisher.some_business_logic()