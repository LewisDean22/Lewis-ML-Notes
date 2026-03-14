import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    # return [0 for i in x if i<0 else x]
    return [0 if i < 0 else i for i in x]


def generate_plot(x, y, filename, y_label):
    plt.rcParams.update({"font.size": 14})
    plt.plot(x, y(x), c="teal", linewidth=2)
    plt.xlabel(r"$x$")
    plt.ylabel(y_label)
    plt.tight_layout()
    plt.savefig(f"docs/figures/{filename}.svg", format="svg")
    plt.close()


sigmoid_x = np.linspace(-10, 10, 1000)
generate_plot(sigmoid_x, sigmoid, "sigmoid", r"$\text{Sigmoid}(x)$")
relu_x = np.linspace(-10, 10, 1000)
generate_plot(relu_x, relu, "relu", r"$\text{ReLU}(x)$")
