#importing required libraries
import socket
import winsound 
from faker import Faker
from colorama import Fore,Style

faker= Faker()


ip = faker.ipv4() #defining the var (ip ) then assigning it to faker to generate fake ip address

ports=[]  #creating the ports list to check them
open=[]   #list to store open ports
closed=[] #list to store closed ports



for i in range(1,10):
    entering=int(input("enter the port number :"))
    ports.append(entering)


for port in ports:  
    print(f'scanning port{port} on {ip}')
    s = socket.socket()  #creating a socket object sending/receving data
    s.settimeout(1)  # setting a timeout of 1 second for the  connection (more than 1 secend---> fail to connect /// less than 1 second---> connected)
    result = s.connect_ex((ip, port)) #connecting to the ip address and port number using connect_ex method 
    
    #check condition for the open and closed ports
    if result ==0: 
        print( Fore.RED+ f"Port {port} is open")
        winsound.Beep(2000, 2000)
        print(Style.RESET_ALL)
        
        open.append(port)


    elif port ==ports[3]: #special condition to see the difference 
        print(Fore.RED+ f"Port {port} is open")
        winsound.Beep(3000, 3000)
        print(Style.RESET_ALL)
        open.append(port)
             
    else:
        print(Fore.GREEN + f"Port {port} is closed")
        winsound.Beep(2000, 600)
        print(Style.RESET_ALL)
        closed.append(port)

    s.close() #closing the socket connection   


#summary of the scan
print("--------------------------------------------------")
print("scanning completed")
print( Fore.GREEN + f"you have {len(closed)} closed ports: {closed}")
print(Style.RESET_ALL)
print( Fore.RED+f"you have {len(open)} open ports: {open}")
print(Style.RESET_ALL)



