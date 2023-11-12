class NegativeValueError(Exception):
    def __init__(self):
        message = "max_length value must be non-negative"
        super().__init__(message)
