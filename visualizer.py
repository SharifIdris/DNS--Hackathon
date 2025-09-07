import networkx as nx
import matplotlib.pyplot as plt

def visualize_trust_chain(domain, result):
    G = nx.DiGraph()
    tld = domain.split('.')[-1]

    G.add_edge("Root", tld)
    G.add_edge(tld, domain)

    color_map = []
    for node in G:
        if node == domain:
            if "Secure" in result["status"]:
                color_map.append("green")
            elif "Insecure" in result["status"]:
                color_map.append("orange")
            else:
                color_map.append("red")
        else:
            color_map.append("lightblue")

    nx.draw(G, with_labels=True, node_color=color_map, node_size=2000, font_size=12)
    plt.title(f"DNSSEC Trust Chain for {domain}")
    plt.show()
