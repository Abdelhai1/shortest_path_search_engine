import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
# initialization
graph = None

def get_map_data(city_name):
    place_name = city_name + ", Algeria"  # Assuming Algeria for all cities
    global graph
    graph = ox.graph_from_place(place_name, network_type='drive')
    return graph

def update_nodes(event=None):
    selected_city = combobox_city.get()
    graph = get_map_data(selected_city)
    listbox_source.delete(0, tk.END)
    listbox_target.delete(0, tk.END)
    for node in get_node_names(graph):
        listbox_source.insert(tk.END, node)
        listbox_target.insert(tk.END, node)

def get_node_names(graph):
    node_names = {}
    for node in graph.nodes():
        node_names[node] = graph.nodes[node].get('name', f"Unnamed Node {node}")
    return node_names

def a_star_search(graph, source, target):
    path = nx.astar_path(graph, source, target, weight='length')
    return path

def plot_shortest_path(graph, shortest_path):
    fig, ax = ox.plot_graph_route(graph, shortest_path, route_color='g', route_linewidth=3, node_size=0, figsize=(15, 15), show=False, close=False)
    plt.tight_layout()
    plt.axis('off')
    plt.show(block=False)

def main():
    
    selected_source = listbox_source.get(tk.ACTIVE)
    selected_target = listbox_target.get(tk.ACTIVE)
    
    if selected_source and selected_target:
        shortest_path = a_star_search(graph, selected_source, selected_target)
        plot_shortest_path(graph, shortest_path)
    else:
        messagebox.showwarning("Warning", "Please select both source and target nodes.")

# Initialize Tkinter
root = tk.Tk()
root.title("Shortest Path Finder")
root.geometry("400x400")

# Create frames for better organization
frame_input = ttk.Frame(root, padding="10")
frame_input.pack(fill='both', expand=True)

frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.pack(fill='x')

# Create and place the widgets
label_city = ttk.Label(frame_input, text="Select City:")
label_city.pack(side='left', padx=5, pady=5)

"wilayas"
cities = [
    "Adrar", "Ain Defla", "Ain Temouchent", "Alger", "Annaba", "Batna",
    "Bechar", "Bejaia", "Biskra", "Blida", "Bordj Bou Arreridj", "Bouira",
    "Boumerdes", "Chlef", "Constantine", "Djelfa", "El Bayadh", "El Oued",
    "El Tarf", "Ghardaia", "Guelma", "Illizi", "Jijel", "Khenchela",
    "Laghouat", "Muaskar", "Medea", "Mila", "Mostaganem", "Msila", "Naama",
    "Oran", "Ouargla", "Oum el Bouaghi", "Relizane", "Saida", "Setif", "Sidi Bel Abbes",
    "Skikda", "Souk Ahras", "Tamanrasset", "Tebessa", "Tiaret", "Tindouf",
    "Tipaza", "Tissemsilt", "Tizi Ouzou", "Tlemcen", "Adrar", "Ain Defla",
    "Ain Temouchent", "Alger", "Annaba", "Batna", "Bechar", "Bejaia", "Biskra",
    "Blida", "Bordj Bou Arreridj", "Bouira", "Boumerdes", "Chlef", "Constantine",
    "Djelfa", "El Bayadh", "El Oued", "El Tarf", "Ghardaia", "Guelma", "Illizi",
    "Jijel", "Khenchela", "Laghouat", "Muaskar", "Medea", "Mila", "Mostaganem",
    "Msila", "Naama", "Oran", "Ouargla", "Oum el Bouaghi", "Relizane", "Saida",
    "Setif", "Sidi Bel Abbes", "Skikda", "Souk Ahras", "Tamanrasset", "Tebessa",
    "Tiaret", "Tindouf", "Tipaza", "Tissemsilt", "Tizi Ouzou", "Tlemcen"
]

combobox_city = ttk.Combobox(frame_input, values=cities)
combobox_city.pack(side='left', padx=5, pady=5)
combobox_city.bind("<<ComboboxSelected>>", update_nodes)

label_source = ttk.Label(frame_input, text="Source Place:")
label_source.pack(side='left', padx=5, pady=5)

listbox_source = tk.Listbox(frame_input, selectmode="browse")
listbox_source.pack(side='left', fill='both', expand=True, padx=5, pady=5)

label_target = ttk.Label(frame_input, text="Destination Place:")
label_target.pack(side='left', padx=5, pady=5)

listbox_target = tk.Listbox(frame_input, selectmode="browse")
listbox_target.pack(side='left', fill='both', expand=True, padx=5, pady=5)

btn_find_path = ttk.Button(frame_buttons, text="Find Shortest Path", command=main)
btn_find_path.pack(fill='x', padx=5, pady=5)

# Run the main loop
root.mainloop()
