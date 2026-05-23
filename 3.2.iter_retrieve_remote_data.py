class RetrieveRemoteData:
    def __init__(self, per_page: int = 3):
        self.per_page = per_page


    def __iter__(self):
        page = request(Query(per_page=self.per_page, page=1))
        while True:
            for item in page.results:
                yield item
            if page.next is None:
                break
            page = request(Query(per_page=self.per_page, page=page.next))