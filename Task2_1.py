# 2. Quick Decisions: The Event Planner
# Task 1: Code Correction
attendees_count = input("Enter number of attendees: ")
attendees = int(attendees_count)
venue = "large hall" if attendees > 100 else "conference room"
print(venue)