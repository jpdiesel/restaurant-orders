from collections import Counter
from src.analyze_log import (never_requested_by_customer, days_never_visited_by_customer)


class TrackOrders:
    def __init__(self):
        self._orders = []
    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._orders)

    def add_new_order(self, customer, order, day):
        self._orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        ordered = dict()
        for client, dish, _day in self._orders:
            if client == customer:
                ordered[dish] = ordered.get(dish, 0) + 1
         
        return max(ordered, key=ordered.get)

    # https://stackoverflow.com/questions/48606406/find-most-frequent-value-in-python-dictionary-value-with-maximum-count

    def get_never_ordered_per_customer(self, customer):
        return never_requested_by_customer(self._orders, customer)

    def get_days_never_visited_per_customer(self, customer):
        return days_never_visited_by_customer(self._orders, customer)

    def get_busiest_day(self):
        visited = dict()
        for _client, _dish, day in self._orders:
            visited[day] = visited.get(day, 0) + 1
        return max(visited, key=visited.get)

    def get_least_busy_day(self):
        visited = dict()
        for _client, _dish, day in self._orders:
            visited[day] = visited.get(day, 0) + 1
        return min(visited, key=visited.get)
