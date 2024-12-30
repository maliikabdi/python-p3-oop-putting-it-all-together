#!/usr/bin/env python3

class Book:

    def __init__(self, title, page_count):
        # Initialize the title and page_count attributes
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Ensure the page_count is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Output when turning the page
        print("Flipping the page...wow, you read fast!")


