import base64
import json
import matplotlib as mpl
mpl.use('Agg')
import markdown.extensions.fenced_code
import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from flask import Flask, request
from pygments.formatters import HtmlFormatter
from custom_visuals import funnel_plot
from waitress import serve

app = Flask(__name__)

PALLETE = "Set2"

def sort_by_month(df: pd.DataFrame) -> pd.DataFrame:
    rank = {"JAN": 10, "FEB": 11, "MAR": 12, "APR": 1, "MAY": 2, "JUN": 3,
            "JUL": 4, "AUG": 5, "SEP": 6, "OCT": 7, "NOV": 8, "DEC": 9}
    df.reset_index(inplace=True, drop=False)
    df.index = df['index'].apply(lambda x: rank[x.upper()]).rename('index')
    df.sort_index(inplace=True)
    df.set_index('index', inplace=True)
    return df

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
    plot = sns.barplot(data=df, hue="line", x="index",
                       y="value", palette=PALLETE)
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

@app.route('/lineplotmonth', methods=["POST"])
def line_plot_month():
    meta = request.json['metadata']
    df = pd.DataFrame.from_records(request.json['data'])
    df = sort_by_month(df)
    sns.set_style("darkgrid", {"axes.facecolor": "0.9"})
    plot = sns.lineplot(data=df, dashes=False, hue="event",
                        style="event", markers=True, palette=PALLETE)
    plt.xticks(rotation=45)
    plt.xlabel(meta['X'])
    plt.ylabel(meta['Y'])
    plt.tight_layout()
    plot.figure.savefig('lineplot.png')
    plt.clf()
    with open('lineplot.png', 'rb') as f:
        return base64.b64encode(f.read())

@app.route('/barplotmonth', methods=["POST"])
def bar_plot_month():
    meta = request.json['metadata']
    data = pd.DataFrame.from_records(request.json['data'])
    data = sort_by_month(data)
    sns.set_style("darkgrid", {"axes.facecolor": "0.9"})
    plt.xticks(rotation=45)
    plot = sns.barplot(x=data.X, y=data.Y, palette=PALLETE)
    plt.xlabel(meta['X'])
    plt.ylabel(meta['Y'])
    plt.tight_layout()
    plot.figure.savefig('plot.png')
    plt.clf()
    with open('plot.png', 'rb') as f:
        return base64.b64encode(f.read())

@app.route("/funnel", methods=["POST"])
def ordered_funnel():
    df = pd.DataFrame.from_records(request.json["data"])
    fig = funnel_plot(df,x='value',y='segment')
    plt.tight_layout()
    fig.savefig('funnel.png')
    plt.clf()
    with open("funnel.png", "rb") as f:
        return base64.b64encode(f.read())


@app.route("/docs")
def docs():
    readme_file = open("API_Docs.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )
    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return md_template

@app.route("/")
def index():
    return "working"


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80)
