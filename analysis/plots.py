import matplotlib.pyplot as plt

def plot_results(results, goal):
    for r in results:
        y = [
            abs(c.row - goal.row) + abs(c.col - goal.col)
            for c in r.path
        ]
        x = range(len(y))
        plt.plot(x, y, label=r.name)

    plt.xlabel("Krok")
    plt.ylabel("Dystans Manhattan do mety")
    plt.title("Porównanie algorytmów")
    plt.legend()
    plt.grid(True)
    plt.show()
