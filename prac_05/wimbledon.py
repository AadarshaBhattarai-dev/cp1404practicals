"""
CP1404 Practical 05
"""

FILENAME = "wimbledon.csv"


def main():
    records = load_data(FILENAME)
    champions = count_champions(records)
    countries = get_countries(records)

    print("Wimbledon Champions:")
    for name, wins in champions.items():
        print(f"{name} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_data(filename):
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def count_champions(records):
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_countries(records):
    countries = set()
    for record in records:
        countries.add(record[1])
    return countries

main()
