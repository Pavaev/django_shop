class AuthModel:

    def __init__(self, username, password):
        self.username = username
        self.password = password


class CommentModel:

    def __init__(self, text):
        self.text = text


class OrderModel:

    def __init__(self, username, phone):
        self.username = username
        self.phone = phone
