from prac_09.unreliable_car import UnreliableCar

def main():
    car = UnreliableCar("Unreliable", 100, 30)  # 30% reliability
    drove_total = 0
    attempts = 20
    for i in range(attempts):
        d = car.drive(10)
        print(f"Attempt {i+1}: drove {d} km")
        drove_total += d
    print(f"Total driven after {attempts} attempts: {drove_total} km")
    print(car)

if __name__ == "__main__":
    main()

