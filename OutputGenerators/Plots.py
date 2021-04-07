import matplotlib.pyplot as plt


class Plot:
    @staticmethod
    def draw_save_plot(data, xname, yname, title, file_name):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(data)
        plt.xlabel(xname)
        plt.ylabel(yname)
        plt.title(title)
        plt.show()
        file_name = '../Plots/' + file_name
        plt.savefig(file_name)


if __name__ == '__main__':
    Plot.draw_save_plot([1, 2, 3, 4], 'X', 'Y', 'nazwa', 'test')
