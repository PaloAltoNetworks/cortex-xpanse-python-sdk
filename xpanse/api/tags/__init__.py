from xpanse.api.tags.v1.tags import TagsEndpoint


class TagsApi(TagsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v1"

    @property
    def v1(self):
        return TagsEndpoint(self._api)
