import heapq

class Proceso:
    pid = 0
    def __init__(self, prioridad, tiempo):
        self.prioridad = prioridad
        self.tiempo = tiempo
        self.used = 0
        self.pid = Proceso.pid
        Proceso.pid += 1
    
    def __Comparacion__(self, otro):
        return self.prioridad < otro.priority

def roundRobin(p):
    quantun = 5
    current_process = p.pop(0)
    contador = 0
    while current_process:
        contador += 1
        current_process.tiempo -= 1
        current_process.used += 1
        print('\n [{}]: proceso en ejecución {}, ya ocupado: {}, todavía se necesita: {}'.format(contador,
            current_process.pid,
            current_process.used,
            current_process.tiempo
        ))
        for item in p:
            print("El proceso {} aún necesita tiempo: {}".format(item.pid, item.time))
        if current_process.tiempo == 0:
            if len(p):
                current_process = p.pop()
            else:
                return contador
        else:
            if current_process.used == quantun:
                current_process.used = 0
                p.append(current_process)
                current_process = p.pop()

def leerData():
    data = []
    with open("data.txt","r") as archivo:
        for linea in archivo:
            dt = linea.split(" ")
            data.append(Proceso(int(dt[0]), int(dt[1])))
    return data

def main():
    input("Leyendo Datos...")
    p = leerData()
    roundRobin(p)
    print()

if __name__ == '__main__':
    main()
