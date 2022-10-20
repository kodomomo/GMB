from app.core.github.service.handle_event import HandleEvent


class HandleEventImpl(HandleEvent):

    def handle(self):
        print("Hellow world")



handle_event_impl = HandleEventImpl()