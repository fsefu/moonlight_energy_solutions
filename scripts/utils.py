from matplotlib import pyplot as plt


class Utils:
    @staticmethod
    def save_plot(filename):
        plt.savefig(filename)
        print(f"Plot saved as {filename}")

    # Any additional utility functions
