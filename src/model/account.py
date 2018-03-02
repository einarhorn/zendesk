class Account(object):
    """A ZenDesk account object, which stores email and password

    Attributes:
        email (str): User's account email
        password (str): User's password

    """

    def __init__(self, email, password):
        self.email = email
        self.password = password
    