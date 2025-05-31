import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font="Arial 20", borderwidth=2, relief="solid")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(buttons_frame)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(row_frame, text=btn_text, font="Arial 18", relief="ridge", height=2, width=5)
        button.pack(side="left", expand=True, fill="both", padx=1, pady=1)
        button.bind("<Button-1>", click)

root.mainloop()
