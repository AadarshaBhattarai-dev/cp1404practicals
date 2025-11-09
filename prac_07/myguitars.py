"""CP1404 Practical 07"""

from guitar import Guitar

def main():
    guitars = []
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split("\t")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)

    print("My guitars:")
    for g in guitars:
        print(g)

    guitars.sort()
    print("\nGuitars sorted by year:")
    for g in guitars:
        print(g)

    name = input("Enter guitar name (blank to stop): ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Enter guitar name (blank to stop): ")

    with open("guitars.csv", "w") as out_file:
        for g in guitars:
            out_file.write(f"{g.name}\t{g.year}\t{g.cost}\n")

main()
