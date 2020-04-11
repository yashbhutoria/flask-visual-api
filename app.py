from flask import Flask, request
import seaborn as sns
import plotly.express as px
import json
import pandas as pd
import requests
import base64
import matplotlib.pyplot as plt
from waitress import serve

app = Flask(__name__)

PALLETE = "Set2"


@app.route("/graph", methods=["POST"])
def bar_graph():
    meta = request.json["metadata"]
    data = pd.DataFrame.from_records(request.json["data"])
    sns.set_style("darkgrid", {"axes.facecolor": "0.9"})
    plt.xticks(rotation=45)
    plot = sns.barplot(x=data.X, y=data.Y, palette=PALLETE)
    plt.xlabel(meta["X"])
    plt.ylabel(meta["Y"])
    plt.tight_layout()
    plot.figure.savefig("plot.png")
    plt.clf()
    with open("plot.png", "rb") as f:
        return base64.b64encode(f.read())


@app.route("/lineplot", methods=["POST"])
def line_plot():
    meta = request.json["metadata"]
    df = pd.DataFrame.from_records(request.json["data"])
    sns.set_style("darkgrid", {"axes.facecolor": "0.9"})
    plot = sns.lineplot(
        data=df, dashes=False, hue="event", style="event", markers=True, palette=PALLETE
    )
    plt.xticks(rotation=45)
    plt.xlabel(meta["X"])
    plt.ylabel(meta["Y"])
    plt.tight_layout()
    plot.figure.savefig("lineplot.png")
    plt.clf()
    with open("lineplot.png", "rb") as f:
        return base64.b64encode(f.read())


@app.route("/multibar", methods=["POST"])
def multi_bar():
    meta = request.json["metadata"]
    df = pd.DataFrame.from_records(request.json["data"])
    df.reset_index(inplace=True, level=0)
    df = df.melt(id_vars=["index"], var_name="line")
    sns.set_style("darkgrid", {"axes.facecolor": "0.9"})
    plot = sns.barplot(data=df, hue="line", x="index", y="value", palette=PALLETE)
    plt.xticks(rotation=45)
    plt.xlabel(meta["X"])
    plt.ylabel(meta["Y"])
    plt.tight_layout()
    plot.figure.savefig("multibar.png")
    plt.clf()
    with open("multibar.png", "rb") as f:
        return base64.b64encode(f.read())


@app.route("/scatter", methods=["POST"])
def scatter():
    meta = request.json["metadata"]
    df = pd.DataFrame.from_records(request.json["data"])
    df.reset_index(inplace=True, level=0)
    sns.set_style("darkgrid", {"axes.facecolor": "0.9"})
    plot = sns.scatterplot(data=df, x="x", y="y", palette=PALLETE)
    plt.xticks(rotation=45)
    plt.xlabel(meta["X"])
    plt.ylabel(meta["Y"])
    plt.tight_layout()
    plot.figure.savefig("scatter.png")
    plt.clf()
    with open("scatter.png", "rb") as f:
        return base64.b64encode(f.read())


@app.route("/funnel", methods=["POST"])
def funnel():
    data = dict(
        number=[39, 27.4, 20.6, 11, 2],
        stage=[
            "Website visit",
            "Downloads",
            "Potential customers",
            "Requested price",
            "invoice sent",
        ],
    )
    fig = px.funnel(data, x="number", y="stage")
    fig.write_image('funnel.png')
    with open("funnel.png", "rb") as f:
        return base64.b64encode(f.read())


@app.route("/")
def home():
    return "Working"


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80)
