import tkinter as tk

window = tk.Tk()  # ساخت پنجره
window.title("برنامه من")  # عنوان پنجره
window.geometry("300x200")  # اندازه پنجره

label = tk.Label(window, text="سلام رضا!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(
    window, text="کلیک کن", command=lambda: label.config(text="کلیک شد!")
)
button.pack()

window.mainloop()  # اجرای برنامه
