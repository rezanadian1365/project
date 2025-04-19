# pickle & pickletools
import pickle

data = ["apple", "banana", "cherry"]
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

import pickletools

with open("data.pkl", "rb") as f:
    pickletools.dis(f)
