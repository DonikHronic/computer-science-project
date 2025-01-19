from typing import Any

import networkx
from matplotlib import pyplot as plt

from config import COLOR_MAPPING


async def visualize_business_process(architecture: dict[str, Any]) -> None:
    print("Visualizing the business process...")
    # Visualization code goes here
    graph = networkx.DiGraph()
    plt.figure(figsize=(15, 10))
    for obj in architecture["objects"]:
        graph.add_node(obj["id"], label=obj["name"], description=obj["description"], status=obj["status"])

    for interaction in architecture["interactions"]:
        from_id = interaction["from"]
        for to in interaction["to"]:
            graph.add_edge(from_id, to["id"], status=to["status"])

    # Get node colors based on the status attribute
    node_colors = [COLOR_MAPPING[graph.nodes[node]["status"]] for node in graph.nodes]

    # Get edge colors based on the status attribute
    edge_colors = [COLOR_MAPPING[graph.edges[edge]["status"]] for edge in graph.edges]

    pos = networkx.spring_layout(graph, k=2.5)
    networkx.draw_networkx_nodes(graph, pos, node_size=2000, node_color=node_colors)
    networkx.draw_networkx_labels(graph, pos, labels=networkx.get_node_attributes(graph, "label"), font_size=8)

    # Drawing edges
    networkx.draw_networkx_edges(graph, pos, arrowstyle="->", arrowsize=20, edge_color=edge_colors)
    edge_labels = {(u, v): d["status"] for u, v, d in graph.edges(data=True)}
    networkx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color="red", font_size=8)

    # Display plot
    plt.title("JSON Data Visualization")
    plt.show()

    print("Business process visualization is completed.")
