attendee_names = set()

attendee_count = int(input("Attendee count: "))

for _ in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.add(attendee_name)

exempted = input("Exempted name: ")
attendee_names.discard(exempted)

late_attendee = attendee_names.pop()
print("Late: ", late_attendee)

print(attendee_names)
