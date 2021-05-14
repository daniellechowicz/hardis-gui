from settings import *
import matplotlib.pyplot as plt
import numpy as np
import os


class Plotter(object):
    def plot(self, filename, data_original, data_corrected, start, stop):
        # Time and/or y-axis matrix
        t = np.linspace(0, len(data_corrected), len(data_corrected))

        textstr = "\n".join(
            (
                r"$\mathrm{mean}=%.2f$ N" % (np.mean(data_corrected[start:stop])),
                r"$\mathrm{median}=%.2f$ N" % (np.median(data_corrected[start:stop])),
                r"$\mathrm{std}=%.2f$ N" % (np.std(data_corrected[start:stop])),
                r"$\mathrm{max}=%.2f$ N" % (max(data_corrected[start:stop])),
            )
        )

        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)

        show_from = start - WINDOW
        show_to = stop + WINDOW

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(t, data_original, linewidth=0.5, color="dodgerblue", alpha=0.5)
        ax.plot(t, data_corrected, linewidth=0.5, color="red", alpha=1.0)
        ax.scatter(
            t[start:stop],
            data_corrected[start:stop],
            marker="*",
            color="dodgerblue",
            alpha=0.75,
        )
        ax.set_xlabel("Sample [-]")
        ax.set_ylabel("Cutting force [N]")
        ax.set_xlim(show_from, show_to)
        ax.legend(["Unfiltered", "Filtered", "Selected"], loc="upper right")
        ax.text(
            0.025,
            0.95,
            textstr,
            transform=ax.transAxes,
            fontsize=10,
            verticalalignment="top",
            bbox=props,
        )

        # Create a directory where data will be stored
        try:
            os.mkdir("../data")
        except:
            pass

        # Create a directory where figures will be stored
        try:
            os.mkdir(os.path.join("../data", "figures"))
        except:
            pass

        # Save figure
        plt.savefig(
            os.path.join("../data/figures", filename[:-4] + "_zoom.png"), dpi=200
        )

        # Close figure (figures created through the pyplot interface may consume too much memory
        plt.close()
