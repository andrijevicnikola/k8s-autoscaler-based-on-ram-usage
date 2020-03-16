from flask import Flask
from multiprocessing import Process
import time
app = Flask(__name__)
@app.route('/')
def hello():
    def proces():
        niz = list(range(1,1000000))
        time.sleep(10)
        del niz[:]
    p = Process(target=proces)
    p.start()
    p.join()
    return "OK!"
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)