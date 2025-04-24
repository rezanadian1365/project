class Storage:
    def __init__(self):
        """initialize storage class"""
        self.event = []

    def is_event_in_file(self, event):
        """check if event is in file"""
        with open(
            "c:/Users/rezaNadian/Desktop/hw6/HW10/my_ticket_system/events.txt",
            "r",
            encoding="utf-8",
        ) as f:
            for line in f:
                if event["event_name"] in line:
                    return True
        return False

    def is_event_in_memory(
        self, event_name, event_capacity, event_date, event_time, event_location
    ):
        """check if event is in memory"""
        for event in self.event:
            if (
                event["event_name"] == event_name
                and event["event_capacity"] == event_capacity
                and event["event_date"] == event_date
                and event["event_time"] == event_time
                and event["event_location"] == event_location
            ):
                return True
        return False

    def save_to_file(self):
        """save events to file"""
        with open(
            "c:/Users/rezaNadian/Desktop/hw6/HW10/my_ticket_system/events.txt",
            "a",
            encoding="utf-8",
        ) as f:
            for event in self.event:
                if not self.is_event_in_file(event):
                    f.write(
                        f"event name:{event['event_name']},event capacity:{event['event_capacity']},event date:{event['event_date']},event time : {event['event_time']},event location:{event['event_location']}"
                    )
                    f.write("\n")
                    print("event saved to file and updated successfully")

    def load_from_file(self):
        """load from file"""
        with open(
            "c:/Users/rezaNadian/Desktop/hw6/HW10/my_ticket_system/events.txt",
            "r",
            encoding="utf-8",
        ) as f:
            for line in f:
                event_name, event_capacity, event_date, event_time, event_location = (
                    line.strip().split(",")
                )
                if not self.is_event_in_memory(
                    event_name, event_capacity, event_date, event_time, event_location
                ):
                    self.event.append(
                        {
                            "event_name": event_name.split(":")[1],
                            "event_capacity": int(event_capacity.split(":")[1]),
                            "event_date": event_date.split(":")[1],
                            "event_time": event_time.split(":")[1],
                            "event_location": event_location.split(":")[1],
                        }
                    )
        print("event loaded from file successfully")
        return self.event

    def display_event_menu(self):
        """Display events as a menu and allow user to choose an event"""
        if not self.event:
            print("No events available.")
            return None

        print("Please select an event from the list below:")
        for i, event in enumerate(self.event, 1):
            print(
                f"{i}. {event['event_name']} - {event['event_date']} at {event['event_time']} (Capacity: {event['event_capacity']}, Location: {event['event_location']})"
            )

        try:
            event_choice = int(
                input("Enter the number of the event you want to select: ")
            )
            if 1 <= event_choice <= len(self.event):
                selected_event = self.event[event_choice - 1]
                print(f"You selected: {selected_event['event_name']}")
                return selected_event
            else:
                print("Invalid choice. Please select a valid event number.")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
