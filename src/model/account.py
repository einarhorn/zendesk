class Account(object):
    """A ZenDesk account object, which stores email and password

    Attributes:
        email (str): User's account email
        password (str): User's password
        base_url (str): Base url of Zendesk instance

    """

    def __init__(self, email, password, base_url):
        self.email = email
        self.password = password
        self.base_url = base_url
    