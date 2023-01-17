import tkinter as tk

import controller, languages



def on_button_click():
    input1 = input_1.get()
    input2 = input_2.get()
    output_text.config(state='normal')
    output_text.delete('1.0', tk.END)
    # clear the output text box
    output_text.config(state='normal')
    output_text.insert(tk.END, f"{languages.find_closest_match(input2)}:{controller.get_response(input1, input2)}")
    output_text.config(state='disabled')
    output_text.update()

# Timer for updating color of input areas based on if the input is valid
def timer():
    if input_1.get() != '':
        input_1.config(bg='green')
    else:
        input_1.config(bg='red')
    if input_2.get() != '' and len(input_2.get()) > 2:
        input_2.config(bg='green')
    else:
        input_2.config(bg='red')
    input_2.update()
    input_1.update()
    root.after(1000, timer)


root = tk.Tk()
root.title("GPT-3 Language Translator")
root.geometry("500x500")

label=tk.Label(root, text="Enter text to translate:")
label.pack()
input_1 = tk.Entry(root, width=45, justify='center', relief='solid', font=('Arial', 12))
input_1.pack()
label2 = tk.Label(root, text="Enter target language:")
label2.pack()
input_2 = tk.Entry(root, justify='center', relief='solid', font=('Arial', 12))
input_2.pack()

button = tk.Button(root, text="Submit", command=lambda: on_button_click())
button.pack()

output_text = tk.Text(root, height=3, width=30,
                      state='disabled', relief='solid', font=('Arial', 12))
output_text.pack()

timer()
