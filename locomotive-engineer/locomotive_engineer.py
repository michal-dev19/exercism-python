"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    forgotten_id_1, forgotten_id_2, id_1, *every_other_id = each_wagons_id
    *combined_ids, = *missing_wagons, *every_other_id, *[forgotten_id_1, forgotten_id_2]
    combined_ids.insert(0, id_1)
    return combined_ids

def add_missing_stops(main_route, **remaining_stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    
    stop_values = list(remaining_stops.values())
    stop_values_dict = {"stops": stop_values}
    return {**main_route, **stop_values_dict}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    red, blue, orange = wagons_rows
    sorted_wagons = []
    for item in zip(red, blue, orange):
        sorted_wagons.append(list(item))
    return sorted_wagons
