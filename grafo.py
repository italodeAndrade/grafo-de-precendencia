import time
import sys
from multiprocessing import Process, semaphore

def cont(n, t, nome):
    print(f"processo: {nome} iniciado")
    for i in range(n):
        print(f"{nome} : {i+1} ")
        time.sleep(t)
    print(f"processo {nome} encerrado")

def main():
    numero= int(input("insira o numero: "))
    tempo= float(input("insira o tempo: "))

    A = Process(target=cont, args=(numero, tempo, "A"))
    B = Process(target=cont, args=(numero, tempo, " B"))
    C = Process(target=cont, args=(numero, tempo, "  C"))
    D = Process(target=cont, args=(numero, tempo, "   D"))
    
    A.start()
    B.start()
    C.start()
    D.start()

    print("Aguardando fim dos processos")
    A.join()
    B.join()
    C.join()
    D.join()


if __name__ == '__main__':
    main()
