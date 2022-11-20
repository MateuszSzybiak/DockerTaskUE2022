import io
from flask import Flask, Response, request
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np

app = Flask(__name__)


plt.rcParams["figure.autolayout"] = True


@app.route("/")
def start_page():
    return "<p> Hello, to see quadratic plot use /plot</p>"


@app.route('/plot')
def plot():
    a = float(request.args.get('a', 1))
    b = float(request.args.get('b', 0))
    c = float(request.args.get('c', 0))

    xmin = int(request.args.get('xmin', -5))
    xmax = int(request.args.get('xmax', 5))
    ymin = int(request.args.get('ymin', -5))
    ymax = int(request.args.get('ymax', 25))

    fig, ax = plt.subplots()

    x = np.linspace(xmin, xmax, (xmax-xmin)*10)
    y = a*x**2 + b*x + c
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.xlim([xmin, xmax])
    plt.ylim([ymin, ymax])
    plt.plot(x, y, 'r')
    plt.title("Quadratic function")

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
