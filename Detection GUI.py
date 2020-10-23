import tkinter
import DetectionTool

#we use this fuction to launch the server with thedetection system
def Detection(): 
    NetScan = NetScan_var.get()
    HostIP = HostIP_var.get()
    devices_dict={} 
    devices_dict=DetectionTool.DeviceScan(NetScan)      
    DetectionTool.ServerCode(HostIP, 80, devices_dict)
# I learned GUI programming from different sites but mainly https://www.geeksforgeeks.org/python-gui-tkinter/ and questions answered in https://stackoverflow.com
screen = tkinter.Tk()
#img = ImageTk.PhotoImage(Image.open("dos.png"))
screen.title("Detection tool") #title of the GUI
screen.geometry("900x720") #size of the window of the GUI
screen.configure(bg="#eaebec") #the color of the background
# we take create a window with the above specifications
window = tkinter.Frame(screen)
# we need 2 variable to store the the IP that we want to attack and the spoofed ip that would be inplemented in the GUI
NetScan_var = tkinter.StringVar()
HostIP_var = tkinter.StringVar()
 
# we create 2 small boxes where the user should put his inputs in
entryA = tkinter.Entry(screen, textvariable = NetScan_var)
entryA.place(relx = 0.44, rely=0.4)

label = tkinter.Label(screen, text = "Input the Network scan IP adress:", fg="black", bg="#eaebec", font=20)
label.place(relx = 0.169, rely = 0.4)                    

entryB = tkinter.Entry(screen, textvariable = HostIP_var)
entryB.place(relx = 0.439, rely=0.45)

label = tkinter.Label(screen, text = "Input the Host IP adress:", fg="black", bg="#eaebec", font=20)
label.place(relx = 0.239, rely = 0.45)

begin = tkinter.Button(screen, text = "Launch detection", padx = 10,  fg = "black", bg = "#0e6b0e", command = Detection)
begin.pack(side="bottom")
screen.mainloop() # a loop so the GUI stays displayed 