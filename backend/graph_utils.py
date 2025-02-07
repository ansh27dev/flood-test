# backend/graph_utils.py
import osmnx as ox
import networkx as nx

def create_graph(start_coords, end_coords):
    """Fetch OSM road network and create a graph"""
    bbox = ox.utils_geo.bbox_from_points([start_coords[1], end_coords[1]], [start_coords[0],end_coords[0]], dist=500)
    G = ox.graph_from_bbox(bbox[0],bbox[2],bbox[1],bbox[3],network_type="drive")
    return G

def find_shortest_path(graph, start_coords, end_coords):
    """Find shortest path using A* (initially Dijkstra via nx) and return coordinate list."""
    orig_node = ox.distance.nearest_nodes(graph, start_coords[0], start_coords[1])
    dest_node = ox.distance.nearest_nodes(graph, end_coords[0], end_coords[1])

    try:
        shortest_path = nx.shortest_path(graph, orig_node, dest_node, weight="length")
    except nx.NetworkXNoPath:
        return []

    route_coords = []
    for node_id in shortest_path:
        point = graph.nodes[node_id]
        route_coords.append([point["x"], point["y"]])
    return route_coords