import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors
import matplotlib.transforms as mtransforms
from matplotlib.patches import FancyBboxPatch


class DrawHeatmap(object):
    def __init__(self, data, title, path, x_labels, y_labels):
        self.data = data
        self.title = title
        self.path = path
        self.x_labels = x_labels
        self.y_labels = y_labels

    def add_fancy_patch_around(self, ax, bb, fc, **kwargs):
        fancy = FancyBboxPatch((bb.xmin, bb.ymin), bb.width, bb.height,
                               fc=fc, ec=fc,
                               **kwargs)
        ax.add_patch(fancy)
        return fancy

    def mk_pics(self):
        self.mk_pic(self.data, self.title, self.path, self.x_labels, self.y_labels)

    def mk_pic(self, data, title, path, x_labels, y_labels):
        sns.set()
        # sns.set(rc={'axes.facecolor': 'cornflowerblue', 'figure.facecolor': 'cornflowerblue'})
        # 添加每个热力块的具体数值,保留两位小数
        f, ax = plt.subplots(figsize=(10, 8))

        cmap_b = sns.diverging_palette(220, 20, l=100, n=51)
        norm = matplotlib.colors.TwoSlopeNorm(vcenter=0, vmin=-1, vmax=1)
        cmaps = plt.cm.get_cmap("RdBu")

        sns.heatmap(data, cmap=cmap_b, annot=False, fmt=".3f", ax=ax, vmin=-1.0, vmax=1.0, cbar=False,
                    mask=np.zeros_like(data, dtype=bool),
                    square=True, linewidths=0.3, linecolor="grey")

        for i in range(data.shape[0]):
            for j in range(0, data.shape[1]):
                if j >= i:
                    if i == j:
                        bb = mtransforms.Bbox([[j + 0.03, i + 0.03], [j + 0.96, i + 0.96]])
                        self.add_fancy_patch_around(ax=ax, bb=bb, fc=cmaps(norm(data.iloc[i, j])),
                                               boxstyle="square,pad=0.001")
                    else:
                        wl = abs(data.iloc[j, i]) / 2 * 0.93
                        bb = mtransforms.Bbox([[j + 0.5 - wl, i + 0.5 - wl], [j + wl + 0.5, i + wl + 0.5]])
                        self.add_fancy_patch_around(ax=ax, bb=bb, fc=cmaps(norm(data.iloc[j, i])),
                                               boxstyle="square,pad=0.001")
                    continue
                ax.text(j + 0.5, i + 0.5, '%.3f' % data.iloc[i, j].round(3), ha="center", va="center",
                        color=cmaps(norm(data.iloc[i, j])), fontsize=12,
                        fontname='Times New Roman')

        font1 = {'family': 'Times New Roman',
                 'weight': 'normal',
                 'size': 16,
                 }

        ax.set_xticklabels(x_labels)
        ax.set_yticklabels(y_labels)
        ax.xaxis.set_ticks_position('top')
        ax.yaxis.set_ticks_position('left')

        plt.tick_params(labelsize=14)

        im = ax.imshow(data, cmap=cmaps, vmin=-1, vmax=1)
        cb = f.colorbar(im, ax=ax)
        cb.ax.set_ylabel(title, rotation=-90, va="bottom", fontsize=24,
                         fontname='Times New Roman')

        plt.setp(ax.get_yticklabels(), rotation=360, horizontalalignment='right')
        plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='center')
        f.tight_layout()
        plt.savefig(path)
