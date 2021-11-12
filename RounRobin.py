#!/usr/bin/env python
# coding: utf-8

# In[18]:


import random
import heapq

class Process:
    pid = 0
    def __init__(self, priority, time):
        self.priority = priority
        self.time = time
        self.used = 0
        self.pid = Process.pid
        Process.pid += 1
    
    def __lt__(self, other):
        return self.priority < other.priority


def priority(p):
    heapq.heapify(p)
    current_process = heapq.heappop(p)
    counter = 0
    while current_process:
        counter += 1
        current_process.priority -= 3
        current_process.time -= 1
        print('\ n [{}]: proceso en ejecución {}, prioridad: {}, también se necesita: {}'.format(
            counter,
            current_process.pid,
            current_process.priority,
            current_process.time
        ))
        for item in p:
            print('Proceso {}, la prioridad es {}, necesita tiempo: {}'.format(
                item.pid,
                item.priority,
                item.time))
        if current_process.time != 0:
            heapq.heappush(p, current_process)
            heapq.heapify(p)
        if len(p) > 0:
            current_process = heapq.heappop(p)
        else:
            break
    return counter

def rotation(p):
    rotation_time_length = 5
    current_process = p.pop(0)
    counter = 0
    while current_process:
        counter += 1
        current_process.time -= 1
        current_process.used += 1
        print('\n [{}]: proceso en ejecución {}, ya ocupado: {}, todavía se necesita: {}'.format(counter,
            current_process.pid,
            current_process.used,
            current_process.time
        ))
        for item in p:
            print("El proceso {} aún necesita tiempo: {}".format(item.pid, item.time))
        if current_process.time == 0:
            if len(p):
                current_process = p.pop()
            else:
                return counter
        else:
            if current_process.used == rotation_time_length:
                current_process.used = 0
                p.append(current_process)
                current_process = p.pop()

def main():
    method = input("\n >>> Algoritmo de programación de procesos. \n A. Algoritmo de prioridad \t B. Algoritmo de round robin \n>")
    p = [Process(random.randrange(97,100), random.randrange(1, 21)) for i in range(random.randrange(4, 9))]
    
    if method == 'A':
        priority(p)
    elif method == 'B':
        rotation(p)
    else:
        print('\n [ERROR]: Error de entrada')
    print()

if __name__ == '__main__':
    main()


# In[42]:


import random
import heapq

class Process:
    pid = 0
    def __init__(self, priority, time):
        self.priority = priority
        self.time = time
        self.used = 0
        self.pid = Process.pid
        Process.pid += 1
    
    def __lt__(self, other):
        return self.priority < other.priority


def priority(p):
    heapq.heapify(p)
    current_process = heapq.heappop(p)
    counter = 0
    while current_process:
        counter += 1
        current_process.priority -= 3
        current_process.time -= 1
        print('\n [{}]: proceso en ejecución {}, prioridad: {}, también se necesita: {}'.format(
            counter,
            current_process.pid,
            current_process.priority,
            current_process.time
        ))
        for item in p:
            print('Proceso {}, la prioridad es {}, necesita tiempo: {}'.format(
                item.pid,
                item.priority,
                item.time))
        if current_process.time != 0:
            heapq.heappush(p, current_process)
            heapq.heapify(p)
        if len(p) > 0:
            current_process = heapq.heappop(p)
        else:
            break
    return counter

def rotation(p):
    rotation_time_length = 5
    current_process = p.pop(0)
    counter = 0
    while current_process:
        counter += 1
        current_process.time -= 1
        current_process.used += 1
        print('\n [{}]: proceso en ejecución {}, ya ocupado: {}, todavía se necesita: {}'.format(counter,
            current_process.pid,
            current_process.used,
            current_process.time
        ))
        for item in p:
            print("El proceso {} aún necesita tiempo: {}".format(item.pid, item.time))
        if current_process.time == 0:
            if len(p):
                current_process = p.pop()
            else:
                return counter
        else:
            if current_process.used == rotation_time_length:
                current_process.used = 0
                p.append(current_process)
                current_process = p.pop()

# Python program to convert a list
# to string using join() function
    
# Function to convert  
def listToString(s): 
    # initialize an empty string
    str1 = " " 
    # return string  
    return (str1.join(s))
        
        
# Driver code    
#s = ['Geeks', 'for', 'Geeks']
#print(listToString(s)) 

def main():
    method = input("\n >>> Algoritmo de programación de procesos. \nA. Algoritmo de prioridad \tB. Algoritmo de round robin \n>: ")
    
    # p = [Process(random.randrange(97,100), random.randrange(1, 21)) for i in range(random.randrange(4, 9))]
    p = [Process(random.randrange(97,100), random.randrange(1, 21)) for i in range(random.randrange(2, 3))]
    
    if method == 'A':
        priority(p)
    elif method == 'B':
        rotation(p)
    else:
        print('\ n [ERROR]: Error de entrada')
    print()

if __name__ == '__main__':
    main()


# In[23]:


with open("/Users/HP/Documents/Python/prueba.txt","r") as archivo:
    for linea in archivo:
        print(linea)


# In[24]:


f = open ('/Users/HP/Documents/Python/prueba2.txt','w')
f.write('hola mundo')
f.close()


# In[31]:


# Python program to convert a list
# to string using join() function
    
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
        
        
# Driver code    
s = ['Geeks', 'for', 'Geeks']
print(listToString(s)) 


# In[36]:


if __name__ == '__main__':
    # Python program for implementation of RR Scheduling
    print("Enter Total Process Number: ")
    total_p_no = int(input())
    total_time = 0 
    total_time_counted = 0
    # proc is process list
    proc = []
    wait_time = 0
    turnaround_time = 0
    for _ in range(total_p_no):
        # Getting the input for process
        print("Enter process arrival time and burst time") 
        input_info = list(map(int, input().split(" ")))
        arrival, burst, remaining_time = input_info[0], input_info[1], input_info[1]
        # processes are appended to the proc list in following format
        proc.append([arrival, burst, remaining_time, 0])
        # total_time gets incremented with burst time of each process
        total_time += burst
    print("Enter time quantum")
    time_quantum = int(input())
    # Keep traversing in round robin manner until the total_time == 0
    while total_time != 0:
        # traverse all the processes
        for i in range(len(proc)):
            # proc[i][2] here refers to remaining_time for each process i.e "i"
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                total_time_counted += proc[i][2]
                total_time -= proc[i][2]
                # the process has completely ended here thus setting it's remaining time to 0.
                proc[i][2] = 0 
            elif proc[i][2] > 0:
                # if process has not finished, decrementing it's remaining time by time_quantum
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
            if proc[i][2] == 0 and proc[i][3] != 1:
                # if remaining time of process is 0
                # and 
                # individual waiting time of process has not been calculated i.e flag
                wait_time += total_time_counted - proc[i][0] - proc[i][1]
                turnaround_time += total_time_counted - proc[i][0]
                # flag is set to 1 once wait time is calculated
                proc[i][3] = 1 
    print("\nAvg Waiting Time is ", (wait_time * 1) / total_p_no)
    print("Avg Turnaround Time is ", (turnaround_time * 1) / total_p_no)


# In[43]:


import os
print(os.path.abspath('.'))


# In[ ]:




