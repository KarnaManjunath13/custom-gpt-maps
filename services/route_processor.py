# route_processor.py

class RouteProcessor:
    def __init__(self, routes):
        """
        Initializes the RouteProcessor with a list of routes.
        :param routes: List of routes, where each route is a dictionary containing 'distance' and 'road_type'.
        """
        self.routes = routes

    def filter_by_distance(self, max_distance):
        """
        Filters out routes that exceed the specified maximum distance.
        :param max_distance: Maximum distance allowed.
        :return: List of filtered routes.
        """
        return [route for route in self.routes if route['distance'] <= max_distance]

    def filter_by_road_type(self, preferred_road_types):
        """
        Filters out routes that do not match the preferred road types.
        :param preferred_road_types: List of preferred road types.
        :return: List of filtered routes.
        """
        return [route for route in self.routes if route['road_type'] in preferred_road_types]

    def process_routes(self, max_distance, preferred_road_types):
        """
        Filters routes by both distance and preferred road types.
        :param max_distance: Maximum distance allowed.
        :param preferred_road_types: List of preferred road types.
        :return: List of routes that match both criteria.
        """
        filtered_by_distance = self.filter_by_distance(max_distance)
        filtered_by_road_type = self.filter_by_road_type(preferred_road_types)
        return [route for route in filtered_by_distance if route in filtered_by_road_type]
