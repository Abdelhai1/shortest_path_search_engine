import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox


def get_map_data(place_name):
    graph = ox.graph_from_place(place_name, network_type='drive')
    #print("First 100 node IDs in the graph:", list(graph.nodes())[:100])
    return graph

def plot_graph(graph, node_color='b', node_size=0.1, node_alpha=0.6, edge_color='k', edge_linewidth=0.5, figsize=(15, 15)):
    fig, ax = ox.plot_graph(graph, node_color=node_color, node_size=node_size, node_alpha=node_alpha, edge_color=edge_color, edge_linewidth=edge_linewidth, figsize=figsize, show=False, close=False)
    plt.tight_layout()
    plt.axis('off')
    plt.show(block=False)


def a_star_search(graph, source, target):
    path = nx.astar_path(graph, source, target, weight='length')
    return path


def plot_shortest_path(graph, shortest_path):
    fig, ax = ox.plot_graph_route(graph, shortest_path, route_color='g', route_linewidth=3, node_size=0, figsize=(15, 15), show=False, close=False)
    plt.tight_layout()
    plt.axis('off')
    plt.show(block=False)

def main():
    
    place_name = "Bejaia, Algeria"
    graph = get_map_data(place_name)
    #print(list(graph.nodes()))


    # source_place = entry_source.get()
    # target_place = entry_target.get()

    # Geocode the place names to get the coordinates
    # source_location = ox.geocode(source_place)
    # target_location = ox.geocode(target_place)
    # plot_graph(graph)
    source = int(entry_source.get())
    target = int(entry_target.get())

    shortest_path = a_star_search(graph, source, target)


    plot_shortest_path(graph, shortest_path)



#if __name__ == "__main__":
#    main()

root = tk.Tk()
root.title("Shortest Path Finder")
root.geometry("300x150")  # Set the size of the window

# Create a style
style = ttk.Style(root)
style.theme_use("clam")  # Use a modern theme

# Create frames for better organization
frame_input = ttk.Frame(root, padding="10")
frame_input.pack(fill='x')

frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.pack(fill='x')

# Create and place the widgets
label_source = ttk.Label(frame_input, text="Source Place:")
label_source.pack(side='left', padx=5, pady=5)

entry_source = ttk.Entry(frame_input)
entry_source.pack(side='left', fill='x', expand=True, padx=5, pady=5)

label_target = ttk.Label(frame_input, text="Destination Place:")
label_target.pack(side='left', padx=5, pady=5)

entry_target = ttk.Entry(frame_input)
entry_target.pack(side='left', fill='x', expand=True, padx=5, pady=5)

btn_find_path = ttk.Button(frame_buttons, text="Find Shortest Path", command=main)
btn_find_path.pack(fill='x', padx=5, pady=5)

# Run the main loop
root.mainloop()