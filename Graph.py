import copy


class Graph:
    vertices = []
    edges = []

    def __init__(self):
        self.vertex_index = 0
        self.initialize_graph()
        self.routes = []
        self.get_all_routes('homepage')

    def initialize_graph(self):

        self.add_vertex_to_graph('homepage', 'page_1', 'page')

        self.add_vertex_to_graph('login_button', 'component_3', 'component')
        self.add_vertex_to_graph('login_page', 'page_2', 'page')
        self.add_vertex_to_graph('login_form', 'component_1', 'component')
        self.add_vertex_to_graph('login_link', 'component_8', 'component')

        self.add_vertex_to_graph('register_button', 'component_4', 'component')
        self.add_vertex_to_graph('register_page', 'page_3', 'page')
        self.add_vertex_to_graph('register_form', 'component_2', 'component')

        self.add_vertex_to_graph('homepage', 'page_1', 'page')

        self.add_vertex_to_graph('account_button', 'component_5', 'component')
        self.add_vertex_to_graph('account', 'page_4', 'page')
        self.add_vertex_to_graph('account_info', 'component_6', 'component')

        self.add_vertex_to_graph('logout_button', 'component_7', 'component')

        self.link_vertexes('homepage', 'register_button')
        self.link_vertexes('register_button', 'register_page')
        self.link_vertexes('register_page', 'register_form')
        self.link_vertexes('register_form', 'account_button')
        self.link_vertexes('account_button', 'account')
        self.link_vertexes('account', 'account_info')
        self.link_vertexes('account_info', 'logout_button')
        self.link_vertexes('logout_button', 'homepage')

        self.link_vertexes('homepage', 'login_button')
        self.link_vertexes('login_button', 'login_link')
        self.link_vertexes('login_link', 'register_page')



    def add_vertex_to_graph(self, friendly, node_id, type):
        self.vertices.append({})
        self.vertices[self.vertex_index]['friendly'] = friendly
        self.vertices[self.vertex_index]['node_id'] = node_id
        self.vertices[self.vertex_index]['type'] = type
        self.vertices[self.vertex_index]['id'] = self.vertex_index
        self.vertex_index += 1

    def link_vertexes(self, friendly_1, friendly_2):
        vertex_id_1 = self.get_vertex_id_from_friendly(friendly_1)
        vertex_id_2 = self.get_vertex_id_from_friendly(friendly_2)
        self.edges.append((vertex_id_1, vertex_id_2))

    def get_vertex_id_from_friendly(self, friendly):
        for vertex in self.vertices:
            if vertex['friendly'] == friendly:
                return vertex['id']

    def get_all_routes(self, start):
        start_id = self.get_vertex_id_from_friendly(start)
        current_route = [start_id]
        visited = [False for _ in range(len(self.edges))]
        self.get_route_from_point(current_route, visited)

    def get_route_from_point(self, current_route, visited):
        added_edge = False
        for index, edge in enumerate(self.edges):
            if edge[0] == current_route[-1] and visited[index] is False:
                route_copy = copy.deepcopy(current_route)
                route_copy.append(edge[1])
                visited_copy = copy.deepcopy(visited)
                visited_copy[index] = True
                added_edge = True
                self.get_route_from_point(route_copy, visited_copy)
        if not added_edge:
            self.routes.append(current_route)
