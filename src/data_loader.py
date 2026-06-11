# Build a DataLoader class:
# takes a CSV filepath, loads data into a list of dicts,
# has methods count(), get_by_index(), print_summary(). Push with docstrings on every method.



class DataLoader:
    """
    Loads data from a CSV file into a list of dictionaries.
    """

    def __init__(self, filepath: str) -> None:
        """
        Initializes the DataLoader and loads the CSV data.

        Args:
            filepath (str): Path to the CSV file.
        """
        self.filepath = filepath

        # Stores CSV records as dictionaries where keys are column names
        # and values are the corresponding row values.
        self.data: list[dict[str, str]] = []

        self.load_data()

    def load_data(self) -> None:
        """
        Reads the CSV file and stores each row as a dictionary.
        """
        with open(self.filepath, "r") as file:
            lines = file.readlines()

        # Extract column names from the header row.
        headers = lines[0].strip().split(",")

        # Process each data row, skipping the header.
        for line in lines[1:]:

            # Split the row into individual values.
            values = line.strip().split(",")

            # Create a dictionary representing a single record.
            row = {}

            # Map each header to its corresponding value.
            for i in range(len(headers)):
                row[headers[i]] = values[i]

            # Store the completed record.
            self.data.append(row)

    def count(self) -> int:
        """
        Returns the number of records loaded.

        Returns:
            int: Total number of records.
        """
        return len(self.data)

    def get_by_index(self, index: int) -> dict[str, str]:
        """
        Returns a record at the specified index.

        Args:
            index (int): Position of the record.

        Returns:
            dict[str, str]: The record dictionary.
        """
        return self.data[index]

    def print_summary(self) -> None:
        """
        Prints a summary of the loaded data.
        """
        print(f"Total records: {self.count()}")

        # Ensure at least one record exists before accessing it.
        if self.count() > 0:
            print(f"First record: {self.data[0]}")
