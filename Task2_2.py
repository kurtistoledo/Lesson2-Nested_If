# 2. Quick Decisions: The Event Planner
# Task 2: Venue Selection
attendees_count = input("Enter number of attendees: ")
attendees = int(attendees_count)
venue = "large hall" if attendees > 50 else "conference room"
additional_facilities = ["audio system", "projector"] if attendees > 100 else ["audio system"] if attendees > 50 else []

print("Venue:", venue)
if additional_facilities:
    print("Additional Facilities Needed: audio system, projector")
else:
    print("No additional facilities needed.")
