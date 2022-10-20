from abc import ABC, abstractmethod


class HandleEvent(ABC):

    @abstractmethod
    def handle(self):
        pass


def handle_event(service_impl: HandleEvent):
    service_impl.handle()
