import os, stat, subprocess
from pathlib import Path

class operating_system:
    name = ""
    ct = 0
    at = 0
    bt = 0
    
    
def my_os():
    
    print("    __Main menu__\n\n    1. User Management\n    2. Service Management\n    3. Process Management\n    4. Back-up\n    5. Exit:<")

    choice = int(input("Enter your Choice[1-5]: "))
    print()
    
    if(choice == 4):  #Back-up
        
        def back_up():
            goal = input("Enter 1 for creating file or folders\nEnter 2 for searching files: ")
            print()
            
            if(goal == '1'):
                def create_file_folder():
                    fileorfolder = int(input("Enter 1 if you want to create a file\nEnter 2 if you want to create a folder: "))
                    if(fileorfolder == 1):
                        print()
                        namefile = input("Enter the name of the file you want to create: ")
                        path = Path(namefile)
                        path.touch()
                        print(f"File {path} created!")
                    elif(fileorfolder == 2):
                        namefolder = input("Enter the name of the folder you want to create: ")
                        os.mkdir(namefolder)
                        print(f"The folder {namefolder} created")
                    else:
                        print("Invalid input. Please enter 1 or 2.")
                create_file_folder()
            elif(goal == '2'):
                def searching_file(filename, searchpath):
                    for root, dirs, files in os.walk(searchpath):
                        if filename in files:
                            return os.path.join(root, filename)
                    return None

                searchpath = input("Enter the path of the file: ")
                filename = input("Enter the name of the file: ")
                search = searching_file(filename, searchpath)
                if search:
                    print(f"The file {filename} exists")
                else:
                    print(f"The file {filename} does not exist")
            else:
                print("Invalid input. Please enter 1 or 2.")
        back_up()



    elif(choice == 1): #User Management
        
        def change_permissions():
            path = input("Enter the path of the file or folder: ")
            mode = input("Enter the mode (e.g., 755, 644): ")
            os.chmod(path, int(mode, 8))
            print(f"Changed permissions of {path} to {mode}")

        def add_permissions():
            path = input("Enter the path of the file or folder: ")
            current_mode = stat.S_IMODE(os.lstat(path).st_mode)
            print(f"Current permissions of {path}: {oct(current_mode)}")
            
            print()
            user_type = input("Enter the user type (u for user, g for group, o for others, a for all): ")
            permissions = input("Enter the permissions to add (e.g., r, w, x): ")
            
            permission_value = 0
            if 'r' in permissions:
                permission_value += 4
            if 'w' in permissions:
                permission_value += 2
            if 'x' in permissions:
                permission_value += 1
            
            if user_type == 'u':
                new_mode = (current_mode & 0o707) | (permission_value << 6)
            elif user_type == 'g':
                new_mode = (current_mode & 0o770) | (permission_value << 3)
            elif user_type == 'o':
                new_mode = (current_mode & 0o7770) | permission_value
            elif user_type == 'a':
                new_mode = (current_mode & 0o000) | (permission_value << 6) | (permission_value << 3) | permission_value
            else:
                print("Invalid user type.")
                return
            
            os.chmod(path, new_mode)
            print(f"Added permissions to {path}. New permissions: {oct(new_mode)}")

        # def change_ownership():
        #     path = input("Enter the path of the file or folder: ")
        #     owner = input("Enter the new owner (user ID): ")
        #     try:
        #         os.chown(path, int(owner), -1)
        #         print(f"Changed ownership of {path} to {owner}")
        #     except PermissionError:
        #         print("Permission denied. You need to run this script as root to change ownership.")
        #     except Exception as e:
        #         print(f"An error occurred: {e}")

        def user_managment():
            print()
            print("What do you want to do?")
            print("1. Change permissions")
            print("2. Add permissions")
            print()
            choice = int(input("Enter your choice [1-2]: "))

            if choice == 1:
                change_permissions()
            elif choice == 2:
                add_permissions()
            
            else:
                print("Invalid choice. Please enter 1 or 2.")
        user_managment()
        
        
    elif(choice == 2): #Service Management
        
        def service_managment():
            open_app = input("Enter the name of the application: ")
            try:
                result = subprocess.run(open_app, shell=True, check=True)
                
                if result.returncode == 0:
                    print(f"The app {open_app} opened succesfully.")
                else:
                    print('App DNE :(')
            except subprocess.CalledProcessError as e:
                print(f"failed to open {open_app}. error: {e}")
        service_managment()
        
    
    elif(choice == 3):  #Process Management
        
        def process_managment():
            
            print("    __Manage the process by the following algo's__\n\n    1. FCFS(Algo)\n    2. SJF(Algo)")
            process_algo = input("Enter your Choice[1-2]: ")
            
            if(process_algo == "1"):
                a = int(input("Enter the number of processes: "))
                processes = []
                for i in range(a):
                    p = operating_system()
                    p.name = input(f"enter the name of the process {i+1} : ")
                    p.at = int(input(f"enter the arival time of the process{i+1} : "))
                    p.bt = int(input(f"enter the burst time of process {i+1} : "))
                    processes.append(p)
                fcfs(processes)
                bubble_sort(processes)
                
                
            elif(process_algo == "2"):
                a = int(input("Enter the number of processes: "))
                
                processes = []
                for i in range(a):
                    p = operating_system()
                    p.name = input(f"Enter the name of the process {i+1}: ")
                    p.at = int(input(f"Enter the arrival time of process {i+1}: "))
                    p.bt = int(input(f"Enter the burst time of process {i+1}: "))
                    
                    processes.append(p)

                sortArrivalTime(processes)
                sortBurstTime(processes)
                SJF(processes)
                
            else:
                print("Enter btw 1-2")
                
        process_managment()
        
    elif(choice == 5):  #Exit the OS
        print("\n\nThe OS is shutting down.........")
    
    else:    
        print("Enter between 1 & 5")

            
def bubble_sort(lst):  #for fcfs arival time sorting
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if(lst[j].at > lst[j+1].at):
                lst[j],lst[j+1] = lst[j+1],lst[j]
                    
def fcfs(processes):
    
    ct = []
    tat = []
    wt = []
    
    flag = True
    for i in range(len(processes)):
        if(flag == True):
            ct.append(processes[i].bt)
            flag = False
        else:
            ct.append(ct[i-1]+processes[i].bt)
    
    for i in range(len(processes)):
        tat.append(ct[i] - processes[i].at)
        wt.append(tat[i] - processes[i].bt)
            
    avgwt = 0
    avgtat = 0
        
    for i in range(len(processes)):
        avgwt+= wt[i]
        avgtat+= tat[i]

    print("Average waiting time is: ",(avgwt/len(processes)))
    print("Everage turn around time is: ",(avgtat/len(processes)))             


def sortArrivalTime(lst):   #for sjf arival time sorting
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j].at < lst[min_idx].at:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

def sortBurstTime(lst):   #for sjf burst time sorting
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j].bt < lst[min_idx].bt:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def SJF(processes):
    sortArrivalTime(processes)

    BT = [bt.bt for bt in processes]

    currentTime = 0
    totalProcesses = len(processes)
    completedProcesses = 0
    
    contextSwitching = []
    first = True
    print("Execution State: < ", end="")
    while completedProcesses < totalProcesses:
        arrivedProcess = []
        for process in processes:
            if process.at <= currentTime and process.bt > 0:
                arrivedProcess.append(process)
        if len(arrivedProcess) != 0:
            sortBurstTime(arrivedProcess)

        if len(arrivedProcess) == 0 and completedProcesses < totalProcesses:
            contextSwitching.append("Idle State")
            currentTime += 1
            contextSwitching.append(currentTime)
        else:
            if first:
                contextSwitching.append(arrivedProcess[0].name)
                first = False
            elif runningProcess.name != arrivedProcess[0].name:
                contextSwitching.append(currentTime)
                contextSwitching.append(arrivedProcess[0].name)
        if len(arrivedProcess) != 0:
            runningProcess = arrivedProcess[0] 
            arrivedProcess[0].bt -= 1
            currentTime += 1
            if arrivedProcess[0].bt == 0:
                print(arrivedProcess[0].name + ", ", end="")
                arrivedProcess[0].ct = currentTime
                completedProcesses += 1

    print(">")
    contextSwitching.append(currentTime)

    CT = []
    for p in processes:
        CT.append(p.ct)
    
    TT = []
    WT = []

    for i in range(len(processes)):
        TT.append(CT[i] - processes[i].at)
        WT.append(TT[i] - BT[i])
    
    avgWT = sum(WT) / len(processes)
    avgTT = sum(TT) / len(processes)
   
    print("Average Turn Around Time:", avgTT)
    print("Average Waiting Time:", avgWT) 
        
        
#Main Code
my_os()


print()
restart = input("enter Y for run again, N for terminating the the program: ").upper()
if(restart == "Y"):
    my_os()
    print()
else:
    print("\n\nThe program has been terminated.........")



