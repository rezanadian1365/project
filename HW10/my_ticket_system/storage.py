from prettytable import PrettyTable


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
        """overwrite events to file"""
        with open(
            "c:/Users/rezaNadian/Desktop/hw6/HW10/my_ticket_system/events.txt",
            "w",  # حالت "w" برای بازنویسی کل فایل
            encoding="utf-8",
        ) as f:
            for event in self.event:
                f.write(
                    f"event name:{event['event_name']},event capacity:{event['event_capacity']},event date:{event['event_date']},event time:{event['event_time']},event location:{event['event_location']}\n"
                )
        print("All events saved to file (updated)")

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
        """Display events as a table and allow user to choose an event"""
        if not self.event:
            print("No events available.")
            return None

        # Create a table object
        table = PrettyTable()

        # Define table headers
        table.field_names = [
            "Event #",
            "Event Name",
            "Date",
            "Time",
            "Remaining Capacity",
            "Location",
        ]

        # Add events to the table
        for i, event in enumerate(self.event, 1):
            table.add_row(
                [
                    i,
                    event["event_name"],
                    event["event_date"],
                    event["event_time"],
                    event["event_capacity"],
                    event["event_location"],
                ]
            )

        # Print the table
        print(table)

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

    def reserve_ticket(self, selected_event, user_email):
        """Reserve a ticket for the selected event"""
        for event in self.event:
            if event == selected_event:
                if event["event_capacity"] > 0:
                    event["event_capacity"] -= 1
                    print(
                        f"Ticket reserved for {user_email} for event: {event['event_name']}"
                    )
                    self.save_to_file()
                    self.save_reservation(user_email, event)
                    return True
                else:
                    print("Sorry, this event is fully booked.")
                    return False
        print("Event not found.")
        return False

    def save_reservation(self, user_email, event):
        """Save reservation info to a separate file"""
        with open(
            "c:/Users/rezaNadian/Desktop/hw6/HW10/my_ticket_system/reservations.txt",
            "a",
            encoding="utf-8",
        ) as f:
            f.write(
                f"{user_email},{event['event_name']},{event['event_date']},{event['event_time']}\n"
            )
            print("Reservation saved.")
