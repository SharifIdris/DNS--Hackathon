import networkx as nx
import matplotlib.pyplot as plt

def visualize_trust_chain(domain, result):
    G = nx.DiGraph()
    G.add_edge("Root", "ug")
    G.add_edge("ug", domain)

    color_map = []
    for node in ["Root", "ug", domain]:
        if node == domain:
            if result["status"] == "Secure":
                color_map.append("green")
            elif result["status"] == "Broken":
                color_map.append("red")
            else:
                color_map.append("orange")
        else:
            color_map.append("lightblue")

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=2000, font_size=10)
    plt.title(f"Trust Chain Depth: {3 if result['ds_found'] else 2}")
    plt.show()
