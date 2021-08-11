class ExEndpoint:
    """
    The ExEndpoint class is used as a base class for all endpoints.
    Any additional logic that is desired to be present on all endpoints, but is
    outside of the scope of the session or client can be added here.
    """

    def __init__(self, session):
        self._api = session
