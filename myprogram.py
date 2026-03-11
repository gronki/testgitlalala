import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    n_points = 200
    x = np.random.random(n_points)
    y = np.random.random(n_points)

    plt.figure(figsize=(6, 4))
    plt.scatter(x, y, alpha=0.7)
    plt.title("Random Scatter Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig("/work/out.png", dpi=150)


if __name__ == "__main__":
    main()
