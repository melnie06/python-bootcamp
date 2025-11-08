"""
Manual:

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

Complex:

class CustomError(Exception):
	def __init__(self, message, id):
    		message = f"Custom Error [{id}]: {message}"
    		super().__init__(message)

raise CustomError("yikes", 'a')
"""

class CustomError(Exception):
    pass

raise CustomError("yikes")
