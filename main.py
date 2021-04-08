import numpy as np

import plot_maker

if __name__ == '__main__':
    x_lattice = np.linspace(0, 1, 100)
    y_lattice = x_lattice**2
    plot_maker_obj = plot_maker.PlotMaker()
    xlabel = 'xlabel'
    ylabel = 'ylabel'
    plot_maker_obj.set_params(**plot_maker.big_plot_params)
    plot_maker_obj.make_plot(
            [np.array([x_lattice, y_lattice]).T],
            xlabel=xlabel,
            ylabel=ylabel,
            legend=[1, 2])

