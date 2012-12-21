from flask import Flask, request
from Queue import PriorityQueue
from datetime import datetime
import ujson as json

app = Flask(__name__)
app.heap = PriorityQueue()

@app.route('/push', methods=['GET'])
def push():
    if 'order_id' in request.args:
        order_id = request.args.get('order_id', '')
        item = (datetime.utcnow(), order_id)
        app.heap.put(item)
        return "OK", 200
    else:
        return "Missing order id", 500

@app.route('/pop')
def pop():
    try:
        item = app.heap.get_nowait()
    except:
        item = None
    return json.dumps(item)

@app.route('/queue')
def queue():
    return str(app.heap.qsize())

if __name__ == '__main__':
    app.debug = True
    app.run()
