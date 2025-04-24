class Events:
    """class to handel events for ticket system
    define events for ticket system
    save events
    show events
    review capacity of events
    """

    def __init__(
        self,
        event_name=None,
        event_capacity=None,
        event_date=None,
        event_time=None,
        event_location=None,
        storage_instance=None,
    ):
        self.event_name = event_name
        self.event_capacity = event_capacity
        self.event_date = event_date
        self.event_time = event_time
        self.event_location = event_location
        self.storage = storage_instance
        self.event = []

    def create_event(self):
        """create event and save it to events list to file"""
        # load events from file
        self.storage.load_from_file()
        # get information  event from user
        self.event_name = input("Enter event name:")
        self.event_capacity = int(input("Enter event capacity:"))
        self.event_date = input("Enter event date:")
        self.event_time = input("Enter event time:")
        self.event_location = input("Enter event location:")

        new_event = {
            "event_name": self.event_name,
            "event_capacity": self.event_capacity,
            "event_date": self.event_date,
            "event_time": self.event_time,
            "event_location": self.event_location,
        }

        self.storage.event.append(new_event)

        # save
        self.storage.save_to_file()
        print("event created successfully")

    def list_events(self):
        """list events"""
        print("list of events:")
        for event in self.event:
            print(
                f"event name:{event['event_name']},event capacity:{event['event_capacity']},event date:{event['event_date']},event time : {event['event_time']},event location:{event['event_location']}"
            )

    def get_event_by_date(self):
        """get event by date"""
        event_date = input("Enter event date:")
        for event in self.event:
            if event["event_date"] == event_date:
                print(
                    f'event name:{event['event_name']},event capacity:{event['event_capacity']},event date:{event['event_date']},event time"{event ['event_time']},event location:{event['event_location']}'
                )

    def update_capacity(self):
        """update capacity of event after ticket sale"""
        found = False
        event_name = input("Enter event name:")
        for event in self.event:
            if event["event_name"] == event_name:
                event_capacity = int(input("Enter event cpacity:"))
                event["event_capacity"] = event_capacity
                print(f"event capacity updated to{ event['event_capacity']}")
                found = True
                break
        if not found:
            print("event not found")
