class ItemListModel:
    def __init__(self):
        self.items = []
        self.next = ""
        self.prev = ""

    def get_items(self):
        return self.items

    def add_item(self, name: str, url: str):
        self.items.append(dict(name=name, url=url))

    def set_next_page(self, page_url: str):
        self.next = page_url

    def set_prev_page(self, page_url: str):
        self.prev = page_url
