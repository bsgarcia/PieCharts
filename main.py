import matplotlib.pyplot as plt
import numpy as np


def save_fig(vals, positive, filename):

    # ------------------------------------------------------------------------------- # 
    my_dpi = 96

    figsize = (620/my_dpi, ) * 2
    subsize = (7.5, 7.5)
    left = 0.5 * (1. - subsize[0] / figsize[0])
    right = 1. - left
    bottom = 0.5 * (1. - subsize[1] / figsize[1])
    top = 1. - bottom
    fig = plt.figure(figsize=figsize, dpi=my_dpi)
    fig.subplots_adjust(left=left, right=right, bottom=bottom, top=top)
    ax = fig.add_subplot()

    size = 0.5

    cmap = plt.get_cmap("tab20c")
    # outer_colors = cmap(np.arange(3) * 4)
    # inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))
    explode = [.01, .01][:len(vals)]
    outer_colors = ['seagreen', 'indianred']

    if positive is None:
        if filename[0] == "0" and filename[2] == "0":
            labeldistance = 1.18
        else:
            labeldistance = 1.09

        _, labels, autotexts = ax.pie(
            vals, labeldistance=labeldistance, radius=0.65, colors=outer_colors, pctdistance=0.725,
            labels=['+1', '-1'], autopct='%.0f%%',
            wedgeprops=dict(width=size, edgecolor='w'), explode=explode)
    else:

        _, labels, autotexts = ax.pie(
            vals, labeldistance=1, radius=0.65, colors=[outer_colors[not positive]],
            labels=[['+1', '-1'][not positive]], autopct='%.0f%%',
            wedgeprops=dict(width=size, edgecolor='w'))

    rec = plt.Rectangle(
        (-1.068, -1.063), width=2.13, height=2.129, fill=False, lw=5)

    rec = ax.add_patch(rec)
    rec.set_clip_on(False)

    for label, color, autotext in zip(
            labels, outer_colors, autotexts):

        autotext.set_color('white')
        autotext.set_size(35)
        label.set_size(55)
        label.set_color(color)

    plt.savefig(filename)

    # ------------------------------------------------------------------------------- # 


def main():

    # Define probs and rewards for each cond
    # ------------------------------------------------------------------------------- # 
    reward = [[] for _ in range(6)]
    prob = [[] for _ in range(6)]

    reward[0] = [[-1, 1], [-1, 1]]
    prob[0] = [[0.2, 0.8], [0.8, 0.2]]

    reward[1] = [[-1, 1], [-1, 1]]
    prob[1] = [[0.3, 0.7], [0.7, 0.3]]

    reward[2] = [[-1, 1], [-1, 1]]
    prob[2] = [[0.4, 0.6], [0.6, 0.4]]

    reward[3] = [[-1, 1], [-1, 1]]
    prob[3] = [[0.5, 0.5], [0.5, 0.5]]

    reward[4] = [[-1, 1], [-1, 1]]
    prob[4] = [[0.1, 0.9], [0.9, 0.1]]

    reward[5] = [[-1, 1], [-1, 1]]
    prob[5] = [[1, 0], [0, 1]]

    for r, p in zip(reward, prob):

        for i, j in zip(r, p):

            pwin = j[1]
            rwin = i[1]
            plose = j[0]
            rlose = i[0]
            ev = '%.1f' % (sum([pwin*rwin, plose*rlose]))

            if pwin != 0 and plose != 0:
                val, positive = \
                    ([int(j[1] * 100) / 100, int(j[0] * 100) / 100], None)
            else:
                val, positive = \
                    ([[int(j[1] * 100), int(j[0] * 100)][plose != 0] / 100], pwin != 0)

            save_fig(val, positive, filename=f'{ev}_0.png')
    # ------------------------------------------------------------------------------- # 


if __name__ == '__main__':
   main()