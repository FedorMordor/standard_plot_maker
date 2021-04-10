
import numpy as np

from standard_plot_maker.plot_maker import PlotMaker

if __name__=="__main__":
    x_lattice = np.linspace(0, 1, 100)
    y_lattice = np.sin(x_lattice * 2 * np.pi)
    cont = np.array([x_lattice, y_lattice]).T
    plt_mkr = PlotMaker()
    plt_mkr.make_plot([cont], xlabel='xlabel', ylabel='ylabel')
