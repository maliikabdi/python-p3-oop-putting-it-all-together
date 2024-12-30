#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        # Initialize the brand and size attributes
        self.brand = brand
        self.size = size  # This will use the setter for validation

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Ensure the size is an integer
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        # Output when shoe is cobbled and set condition to "New"
        print("Your shoe is as good as new!")
        self.condition = "New"
