from xpanse.base_api import ExApi
from xpanse.api.annotations.v3.tags import TagsEndpoint


class TagsApi(ExApi, TagsEndpoint):
    def __init__(self, session):
        super().__init__(session)

    @property
    def current_version(self):
        return "v3"

    @property
    def v3(self):
        return TagsEndpoint(self._api)


class AnnotationsApi(ExApi):
    @property
    def tags(self):
        return TagsApi(self._api)
