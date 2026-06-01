from src.data_loader import DataLoader
from pathlib import Path

def main() -> None:
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "students.csv"

    """
    Creates a DataLoader object and demonstrates its methods.
    """
    loader = DataLoader(str(csv_path))

    print("Record count:", loader.count())

    print("\nSecond record:") # Print a newline for better readability, then display the second record (index 1)
    # Demonstrate accessing a specific record (second item) to verify data loading
    print(loader.get_by_index(1))

    print("\nSummary:")
    loader.print_summary()


if __name__ == "__main__":
    main()