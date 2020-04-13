import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import numpy as np


def funnel_plot(df, y, x, pallete="Blues"):
    _df = df
    x_data = _df[x]
    y_data = _df[y]
    x_max = max(x_data)
    x_min = min(x_data)
    y_count = y_data.count()

    plt.xlim(0, x_max)
    plt.ylim(0, y_count)
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.set_frame_on(False)
    plt.tick_params(axis="y", which="both", left=False)
    plt.yticks((np.arange(y_count) + 0.5), tuple(y_data), fontsize="12", va="center")

    pallete = sns.color_palette(pallete, y_count)

    def _generate_rectangle(value, max_val, y_count, pos, color):
        x_cord = (x_max - value) / 2.0
        y_cord = y_count - pos
        ax.text(
            x_cord + value / 2.0,
            y_cord + 0.5,
            value,
            horizontalalignment="center",
            verticalalignment="center",
            size="x-large",
        )
        rectangle = patches.Rectangle(
            (x_cord, y_cord), value, 1, color=color, alpha=0.95
        )
        return rectangle

    bar_patches = [
        ax.add_patch(
            _generate_rectangle(
                value=row[x],
                max_val=x_max,
                y_count=y_count,
                pos=index + 1,
                color=pallete[index],
            )
        )
        for index, row in _df.iterrows()
    ]
    return fig
