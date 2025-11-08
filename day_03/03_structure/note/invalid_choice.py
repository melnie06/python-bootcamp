class InvalidChoiceError(ValueError):
	pass

options = ("rock","paper", "scissors")
user_choice = input("Pick move (rock/paper/scissors): ")

if user_choice not in options:
	raise InvalidChoiceError()