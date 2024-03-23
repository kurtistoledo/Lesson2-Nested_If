# 2. Quick Decisions: The Event Planner
# Task 3: Catering Choices
attendees_count = input("Enter number of attendees: ")
attendees = int(attendees_count)
venue = "large hall" if attendees > 50 else "conference room"
additional_facilities = ["audio system", "projector"] if attendees > 100 else ["audio system"] if attendees > 50 else []

print("Venue:", venue)
if additional_facilities:
    print("Additional Facilities Needed: audio system, projector")
else:
    print("No additional facilities needed.")

vegetarian = input("Do you want vegetarian food? (yes/no): ")
cater = "Veggie Delight Caterers" if vegetarian == "yes" else "Gourmet Meals Caterers"

print("Recommended Caterer:", cater)