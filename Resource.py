class Resource:
    def __init__(self, resourceId, resourceContent):
        self._resourceId = resourceId
        self._resourceContent = resourceContent
    def get_resourceId(self):
        return self._resourceId
    def set_resourceId(self, resourceId):
        self._resourceId = resourceId
    def get_resourceContent(self):
        return self._resourceContent
    def set_resourceContent(self, resourceContent):
        self._resourceContent = resourceContent
