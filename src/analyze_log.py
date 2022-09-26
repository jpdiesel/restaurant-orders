import csv


def read_imported_csv(path_to_file):
    with open(path_to_file) as file:
        csv_list = []
        csv_readed = csv.reader(file, delimiter=",", quotechar='"')
        for item in csv_readed:
            csv_list.append(item)
    return csv_list


def most_requested_by_client(csv_list):
    dishes = dict()
    for client, dish, _day in csv_list:
        dishes[client] = dish
    return dishes['maria']


def hamburguers_requests_by_arnaldo(csv_list):
    burguers = 0
    for client, dish, _day in csv_list:
        if client == "arnaldo" and dish == "hamburguer":
            burguers += 1
    return burguers


def never_requested_by_customer(csv_list, customer):
    all_dishes = set()
    joao_dishes = set()

    for client, dish, _day in csv_list:
        all_dishes.add(dish)
    for client, dish, _day in csv_list:
        if client == customer:
            joao_dishes.add(dish)

    return all_dishes - joao_dishes


def days_never_visited_by_customer(csv_list, customer):
    all_days = set()
    joao_day = set()
    for client, _dish, day in csv_list:
        all_days.add(day)
    for client, _dish, day in csv_list:
        if client == customer:
            joao_day.add(day)

    return all_days - joao_day


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, encoding="utf-8") as csvfile:
            log = list(csv.reader(csvfile, delimiter=",", quotechar="\n"))

        result = [
            most_requested_by_client(log),
            hamburguers_requests_by_arnaldo(log),
            never_requested_by_customer(log, "joao"),
            days_never_visited_by_customer(log, "joao")
        ]

        with open("data/mkt_campaign.txt", "w") as csvfile:
            for item in result:
                csvfile.write(str(item))
                csvfile.write('\n')

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
