import socket

import tkinter

window = tkinter.Tk()
window.title("File Receiver")

frame = tkinter.Frame(window)
frame.pack()

label_receive = tkinter.LabelFrame(frame, text="Receive Button")
label_receive.grid(row=0, column=0, padx=20, pady=20)

notification = tkinter.Label(label_receive, text="")
notification.grid(row=1, column=0)

def Receive():
    notification.config(text="receiving...")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket

    server.bind(("localhost",9999)) # give the IP and Port for new socket
    server.listen() # listning in port 9999

    client, addr = server.accept() # accepting any file comming through that socket
    # print(client, addr)

    filename = client.recv(1024) # receive the file name
    print("receiving ", filename)

    file = open(filename, "wb") # creating a new file

    done = False

    file_bytes = b""

    while done == False:
        data = client.recv(1024) # read 1024 chunks of data repeatly
        if file_bytes[-5:] == b"<end>":
            done = True # end of receiving
        file_bytes += data # appending the received chunks of data

    file.write(file_bytes) # save received data into newly created file

    print("received...")
    notification.config(text="received " + str(filename)[2:-1])

    file.close() # close the file
    client.close() # close the client connection
    server.close() # close the server connection

button_receive = tkinter.Button(label_receive, text="Receive", command=Receive)
button_receive.grid(row=0, column=0)

for widget in label_receive.winfo_children():
    widget.grid_configure(padx=90, pady=10)

window.mainloop()