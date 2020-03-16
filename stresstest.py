from multiprocessing import Process
import requests

url = "http://localhost:30000"

def makeRequiests(id):
        for i in range(100):
            print("Proces sa ID " + str(id) + "; Zahtev broj " + str(i) + "; Vraceno je " + str(requests.get(url=url).content))

if __name__ == '__main__':
    p=[]
    n=50
    for i in range(n):
        p.append(Process(target=makeRequiests,args = (i,)))
        p[i].start()
    for i in range(n):
        p[i].join()
    print("Zavrseno")