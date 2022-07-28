"""
this graph is sectioned into three main portions (A, B, and C)
this will hopefully make it easier to see which functions relate to which print statements
"""

class Graph:
    
    # A ————————————————————————————————
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        
        # converting (start, end) into graph_dict = {'start1': ['end1', 'end2'], ...}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(f'self.graph_dict: {self.graph_dict}')
    
    
    # B ————————————————————————————————
    # find path from start to end
    def get_paths(self, start, end, path=[]):
        path = path + [start]
        
        # if start and end are the same point
        if start == end:
            return [path]
        
        # if there are no paths leaving start
        if start not in self.graph_dict:
            return []
        
        # all possible paths will be contained in this list
        paths = []
        
        # if start isn't directly linked to end, but has other connections to consider
        for node in self.graph_dict[start]:
            if node not in path:
                recursive_paths = self.get_paths(node, end, path)
                for p in recursive_paths:
                    paths.append(p)
                    
        return paths
    
    
    # C ————————————————————————————————
    # find the shortest path from start to end (fewest stops)
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        
        # if start and end are the same point
        if start == end:
            return path
        
        # if there are no paths leaving start
        if start not in self.graph_dict:
            return None
        
        # variable to store the shortest path
        shortest_path = None
        
        # if start isn't directly linked to end, but has other connections to consider
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        
        return shortest_path


if __name__ == '__main__':
    
    # A ————————————————————————————————
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto')
    ]
    
    route_graph = Graph(routes)

    # outcome:
    # self.graph_dict: {
    #     'Mumbai': ['Paris', 'Dubai'],
    #     'Paris': ['Dubai', 'New York'],
    #     'Dubai': ['New York'],
    #     'New York': ['Toronto']
    #     }


    # B ————————————————————————————————
    start = 'Mumbai'
    end = 'New York'
    
    print(f'\n\nthe paths between {start} and {end}: {route_graph.get_paths(start, end)}')


    # C ————————————————————————————————
    start = 'Paris'
    end = 'New York'
    
    print(f'\n\nthe shortest path between {start} and {end}: {route_graph.get_shortest_path(start, end)}')
