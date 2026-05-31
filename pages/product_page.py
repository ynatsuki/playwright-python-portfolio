class ProductPage:
    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.get_by_text("Product").is_visible()
