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

def leerData():
    data = []
    with open("data.txt","r") as archivo:
        for linea in archivo:
            dt = linea.split(" ")
            data.append(Process(int(dt[0]), int(dt[1])))
    return data

def main():
    method = input("\n >>> Algoritmo de programación de procesos. \nA. Algoritmo de prioridad \tB. Algoritmo de round robin \n>: ")
    #p = [Process(random.randrange(97,100), random.randrange(1, 21)) for i in range(random.randrange(4, 9))]
    p = leerData()
    if method == 'A':
        priority(p)
    elif method == 'B':
        rotation(p)
    else:
        print('\n [ERROR]: Error de entrada')
    print()

if __name__ == '__main__':
    main()
