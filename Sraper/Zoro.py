from Target import Target


class Zoro(Target):
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.zoro.com/"
        self.params = f"search?q="
        self.search_terms = []

        self.pageSearch = "&page="

        self.cardTags = ("div", {"class": "product-card"})
        self.productIDTag = "gtm-data-productid"

        # self.fullUrl = self.base_url + self.params + "%20".join(self.search_terms) + self.pageSearch


        self.API_url = "https://www.zoro.com/product/?products="
        self.IMG_url = "https://www.zoro.com/static/cms/product/full/"

    def getFullURL(self):
        return self.base_url + self.params + "%20".join(self.search_terms) + self.pageSearch




