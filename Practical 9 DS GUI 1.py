import sys
import time
import os
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from colorama import Fore, Style, init

init(autoreset=True)

class GraphCLI:
    def __init__(self):
        self.graph = {}
        self.history = []

    def add_vertex(self, u):
        if u not in self.graph:
            self.graph[u] = []
            message = f"Vertex added: {u}"
            self.history.append(message)
            self.display_message(message, Fore.GREEN)
        else:
            self.display_message(f"Vertex {u} already exists!", Fore.RED)

    def remove_vertex(self, u):
        if u in self.graph:
            connected_edges = self.graph[u]
            for v in connected_edges:
                self.graph[v].remove(u)
            del self.graph[u]
            message = f"Vertex {u} and its edges removed."
            self.history.append(message)
            self.display_message(message, Fore.RED)
        else:
            self.display_message(f"Vertex {u} not found!", Fore.RED)

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
        message = f"Edge added: {u} -- {v}"
        self.history.append(message)
        self.display_message(message, Fore.GREEN)

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
            self.graph[v].remove(u)
            message = f"Edge removed: {u} -- {v}"
            self.history.append(message)
            self.display_message(message, Fore.RED)
        else:
            self.display_message("Edge not found!", Fore.RED)

    def remove_node(self, u):
        if u in self.graph:
            for v in self.graph[u]:
                self.graph[v].remove(u)
            del self.graph[u]
            message = f"Node {u} and its edges removed."
            self.history.append(message)
            self.display_message(message, Fore.RED)
        else:
            self.display_message("Node not found!", Fore.RED)

    def bfs(self, start_vertex):
        if start_vertex not in self.graph:
            self.display_message(f"Vertex {start_vertex} not found!", Fore.RED)
            return

        visited = []
        queue = deque([start_vertex])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                self.display_message(f"Visited {vertex}", Fore.GREEN)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        message = f"BFS Traversal: {' -> '.join(visited)}"
        self.history.append(message)
        self.display_message(message, Fore.BLUE)

    def dfs(self, start_vertex, visited=None):
        if start_vertex not in self.graph:
            self.display_message(f"Vertex {start_vertex} not found!", Fore.RED)
            return

        if visited is None:
            visited = []
        
        visited.append(start_vertex)
        self.display_message(f"Visited {start_vertex}", Fore.GREEN)

        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

        if len(visited) == len(self.graph):
            message = f"DFS Traversal: {' -> '.join(visited)}"
            self.history.append(message)
            self.display_message(message, Fore.BLUE)

    def display_graph(self):
        G = nx.Graph(self.graph)
        nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=20, font_color='black')
        plt.show()

    def display_menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.MAGENTA + Style.BRIGHT + """
        ==============================
               Graph CLI Abin S103
        ==============================
        """)
        # Display the history of operations
        for record in self.history:
            print(Fore.YELLOW + record)
        print(Fore.MAGENTA + Style.BRIGHT + """
        ==============================
        1. Add Vertex
        2. Remove Vertex
        3. Add Edge
        4. Remove Edge
        5. Remove Node
        6. Display Graph
        7. BFS Traversal
        8. DFS Traversal
        9. Exit
        ==============================
        """)
        choice = input(Fore.CYAN + "Enter your choice: ")
        return choice

    def display_message(self, message, color=Fore.WHITE):
        print(color + message)
        time.sleep(1)

    def run(self):
        while True:
            choice = self.display_menu()
            if choice == '1':
                u = input("Enter vertex: ")
                self.add_vertex(u)
            elif choice == '2':
                u = input("Enter vertex to remove: ")
                self.remove_vertex(u)
            elif choice == '3':
                u = input("Enter first node: ")
                v = input("Enter second node: ")
                self.add_edge(u, v)
            elif choice == '4':
                u = input("Enter first node: ")
                v = input("Enter second node: ")
                self.remove_edge(u, v)
            elif choice == '5':
                u = input("Enter the node to remove: ")
                self.remove_node(u)
            elif choice == '6':
                self.display_graph()
            elif choice == '7':
                start = input("Enter starting vertex for BFS: ")
                self.bfs(start)
            elif choice == '8':
                start = input("Enter starting vertex for DFS: ")
                self.dfs(start)
            elif choice == '9':
                self.display_message("Exiting...", Fore.RED)
                break
            else:
                self.display_message("Invalid choice! Please try again.", Fore.RED)

if __name__ == "__main__":
    graph_cli = GraphCLI()
    graph_cli.run()
