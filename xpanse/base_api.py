class ExApi:
    """
    The ExApi class is used as a base class for all APIs.
    """

    def __init__(self, session):
        self._api = session
