import tkinter as tk

import controller, languages


# Function called after submit button is pressed
def on_button_click():
    input1 = input_1.get()
    input2 = input_2.get()
    output_text.config(state='normal')
    
     # clear the output text box
    output_text.delete('1.0', tk.END)
    output_text.config(state='normal')
    
    # get translated text and match found for the language to output in gui
    output_text.insert(tk.END, f"{languages.find_closest_match(input2)}:{controller.get_response(input1, input2)}")
    output_text.config(state='disabled')
    output_text.update()

    '''This does not ensure a proper input all of the time 
    but makes sure the function used for finding the language 
    has enough input and the translation input isnt a blank space'''
    
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

# Root Tkinter window
root = tk.Tk()
root.title("GPT-3 Language Translator")
root.geometry("500x500")

# Label and input for text to be translated
label=tk.Label(root, text="Enter text to translate:")
label.pack()
input_1 = tk.Entry(root, width=45, justify='center', relief='solid', font=('Arial', 12))
input_1.pack()

# Label and input for target language
label2 = tk.Label(root, text="Enter target language:")
label2.pack()
input_2 = tk.Entry(root, justify='center', relief='solid', font=('Arial', 12))
input_2.pack()

#submit button
button = tk.Button(root, text="Submit", command=lambda: on_button_click())
button.pack()


# Output window for translated text
output_text = tk.Text(root, height=3, width=30,
                      state='disabled', relief='solid', font=('Arial', 12))
output_text.pack()

timer()
