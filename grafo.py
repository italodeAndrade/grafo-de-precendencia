import time
from multiprocessing import Process, Semaphore

def cont(n, t, nome, sem=None, sem_sai=None):
    print(f"Processo {nome} iniciado")
    
    if sem:
        sem.acquire()  

    for i in range(n):
        print(f"{nome} : {i+1}")
        time.sleep(t)

    if sem_sai:
        sem_sai.release()
        sem_sai.release()

    print(f"Processo {nome} encerrado")
        

def main():
    numero = int(input("Insira o número: "))
    tempo = float(input("Insira o tempo: "))

    sem_BC = Semaphore(0)
    sem_D = Semaphore(0)

    
    A = Process(target=cont, args=(numero, tempo, "A",None,sem_BC )) 
    B = Process(target=cont, args=(numero, tempo, " B",sem_BC,None))  
    C = Process(target=cont, args=(numero, tempo, "  C",sem_BC,sem_D))
    D = Process(target=cont, args=(numero, tempo, "   D",sem_D,None))  

    A.start()
    B.start()
    C.start()
    D.start()  

 
    A.join()  
    B.join()  
    C.join()
    D.join()  

if __name__ == '__main__':
    main()
