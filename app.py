from flask import Flask, request
import seaborn as sns
import json
import pandas as pd
import requests
import base64
import matplotlib.pyplot as plt
app = Flask(__name__)


@app.route('/graph', methods=["POST"])
def bar_graph():
    print(type(request.json))
    data = pd.DataFrame.from_records(request.json)
    svm = sns.barplot(x=data.X,
                      y=data.Y).get_figure().savefig('plot.png')
    plt.clf()
    return base64.b64encode(open('plot.png', 'rb').read())

@app.route('/lineplot', methods=["POST"])
def line_plot():
    df = pd.DataFrame.from_records(request.json)
    plot = sns.lineplot(data=df,dashes=False,hue="event", style="event",markers=True)
    plt.xticks(rotation=45)
    plot.figure.savefig('lineplot.png')
    plt.clf()
    return base64.b64encode(open('lineplot.png', 'rb').read())

@app.route('/')
def home():
    return "Working"


if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=5000)
