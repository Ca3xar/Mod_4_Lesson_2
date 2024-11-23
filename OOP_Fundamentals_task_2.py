class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count
    
event = Event("Coding Temple Meeting", "09-27-2024")

event.add_participant()
event.add_participant()
event.add_participant()

print(f"Participant count for '{event.name}' on {event.date}: {event.get_participant_count()}")