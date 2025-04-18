import pickle


def save_data(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)
        print("Data has been saved.")


def load_data(filename):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            print("Data has been loaded.")
            return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
