import tkinter
from tkinter.filedialog import askopenfile
import socket

window = tkinter.Tk() # root window - parent window for everything
# everything'll place inside this box

window.title("File Sender")

# this frame is inside the root window
frame = tkinter.Frame(window) # parent of this frame is root window
frame.pack() # layout manager to place the frame in responsive manner automatically

# parent of data_frame is frame
data_frame = tkinter.LabelFrame(frame, text="Destination IP/Port") # creating a frame with a lable and border
data_frame.grid(row=0, column=0, padx=20, pady=5, sticky="ew") # layout manager to place the frame custom manar

ip = tkinter.Label(data_frame, text="IP") # creating a lable
ip.grid(row=0, column=0) # placing the label
port = tkinter.Label(data_frame, text="Port")
port.grid(row=0, column=1)

ip_entry = tkinter.Entry(data_frame)
ip_entry.grid(row=1, column=0)
port_entry = tkinter.Entry(data_frame)
port_entry.grid(row=1, column=1)

for widget in data_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

select_button_frame = tkinter.LabelFrame(frame, text="Select a file")
select_button_frame.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

selectet_file_name = tkinter.Label(select_button_frame, text="")
selectet_file_name.grid(row=0, column=1)

def Open():
    file = askopenfile()
    global file_dir
    file_dir = file.name
    selectet_file_name.config(text=file_dir)

B_select = tkinter.Button(select_button_frame, text ="Select", command = Open)
B_select.grid(row=0, column=0)

for widget in select_button_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


send_button_frame = tkinter.LabelFrame(frame, text="Send selected file")
send_button_frame.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

def Send():
    # print(ip_entry.get())
    # print(port_entry.get())
    # print(file_dir)


    file_name = ""
    for c in file_dir[::-1]:
        if c == "/":
            break
        file_name = c+file_name
    print(file_name) # retrieved file name from the full directory

    # sending the file via UDP connection
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a new socket
    client.connect((ip_entry.get(), int(port_entry.get()))) # connect with another known socket
    client.send(file_name.encode()) # send file name before sending the file to save the file in receiver's pc as the exact same name of the file in sender's pc
    file = open(file_dir, "rb") # open the file in sender's pc
    file_to_send = file.read() # read the file
    client.sendall(file_to_send) # send the file
    client.send("<end>".encode()) # to identify the end

B_send = tkinter.Button(send_button_frame, text="Send", command=Send)
B_send.grid(row=0, column=0)

for widget in send_button_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop() # run the program until i close the window