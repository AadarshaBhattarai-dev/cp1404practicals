from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Limo", 100, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare for 18 km: {fare:.2f}")
    expected = round((SilverServiceTaxi.price_per_km if hasattr(SilverServiceTaxi, "price_per_km") else 1.23) * 2 * 18 + taxi.flagfall, 1)
    expected = round(1.23 * 2 * 18 + taxi.flagfall, 1)
    assert fare == expected, f"Fare {fare} != expected {expected}"

if __name__ == "__main__":
    main()
