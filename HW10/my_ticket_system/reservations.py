# class reservation:
#     def reserve_ticket(self, selected_event, user_email):
#         """Reserve a ticket for the selected event"""
#         for event in self.event:
#             if event == selected_event:
#                 if event["event_capacity"] > 0:
#                     event["event_capacity"] -= 1
#                     print(
#                         f"Ticket reserved for {user_email} for event: {event['event_name']}"
#                     )
#                     self.save_to_file()
#                     self.save_reservation(user_email, event)
#                     return True
#                 else:
#                     print("Sorry, this event is fully booked.")
#                     return False
#         print("Event not found.")
#         return False

#     def save_reservation(self, user_email, event):
#         """Save reservation info to a separate file"""
#         with open(
#             "c:/Users/rezaNadian/Desktop/hw6/HW10/my_ticket_system/reservations.txt",
#             "a",
#             encoding="utf-8",
#         ) as f:
#             f.write(
#                 f"{user_email},{event['event_name']},{event['event_date']},{event['event_time']}\n"
#             )
#             print("Reservation saved.")
