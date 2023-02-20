class MessengerToken(dict):
    TOKEN = '_id'

    def __init__(
            self,
            token: str
    ):
        super().__init__(
            _id=token
        )
