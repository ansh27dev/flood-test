# backend/routing.py
from graph_utils import create_graph, find_shortest_path

def calculate_route(start_coords, end_coords, flood_zones=None): # Flood zones are optional for now
    """Main function to get route."""
    graph = create_graph(start_coords, end_coords)
    route = find_shortest_path(graph, start_coords, end_coords)
    return route