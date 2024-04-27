import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def get_map_data(place_name):
    graph = ox.graph_from_place(place_name, network_type='drive')
    return graph

def plot_graph(graph, node_color='b', node_size=0.1, node_alpha=0.6, edge_color='k', edge_linewidth=0.5, figsize=(15, 15)):
    fig, ax = ox.plot_graph(graph, node_color=node_color, node_size=node_size, node_alpha=node_alpha, edge_color=edge_color, edge_linewidth=edge_linewidth, figsize=figsize, show=False, close=False)
    plt.tight_layout()
    plt.axis('off')
    plt.show()


def a_star_search(graph, source, target):
    path = nx.astar_path(graph, source, target, weight='length')
    return path


def plot_shortest_path(graph, shortest_path):
    fig, ax = ox.plot_graph_route(graph, shortest_path, route_color='g', route_linewidth=3, node_size=0, figsize=(15, 15), show=False, close=False)
    plt.tight_layout()
    plt.axis('off')
    plt.show()

def main():
    
    place_name = "Bejaia, Algeria"
    graph = get_map_data(place_name)
    #print(list(graph.nodes()))



    plot_graph(graph)
    targa_university_node = entry_source.get()
    center_city= entry_target.get()

    source = list(graph.nodes())[0]
    target = list(graph.nodes())[23]


    shortest_path = a_star_search(graph, 4129304918, 4129304920)


    plot_shortest_path(graph, shortest_path)



#if __name__ == "__main__":
#    main()

root = tk.Tk()
root.title("Shortest Path Finder")

label_source = tk.Label(root, text="Source Place:")
label_source.grid(row=0, column=0, padx=5, pady=5)
entry_source = tk.Entry(root)
entry_source.grid(row=0, column=1, padx=5, pady=5)

label_target = tk.Label(root, text="Destination Place:")
label_target.grid(row=1, column=0, padx=5, pady=5)
entry_target = tk.Entry(root)
entry_target.grid(row=1, column=1, padx=5, pady=5)

btn_find_path = tk.Button(root, text="Find Shortest Path", command=main)
btn_find_path.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
