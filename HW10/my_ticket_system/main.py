from storage import Storage
from events import Events
from auth import Auth

admin = Auth()
print("welcome to my ticket system")
admin.login()

admin.validate_user()
store = Storage()
event_manager = Events(storage_instance=store)
event_manager.create_event()
store.save_to_file()
event_manager.list_events()
display = input("do you want to display events?(y/n)")
if display == "y":
    display_event = store.display_event_menu()
    if display_event:
        print(f"you selected {display_event['event_name']}")
    else:
        print("No event selected.")
