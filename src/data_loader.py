# Build a DataLoader class: takes a CSV filepath, loads data into a list of dicts,
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
        self.data: list[dict[str, str]] = [] # self.data should be a list containing dictionaries where the keys and values are strings.

        # example
#       [
#           {"name": "Ali", "grade": "85"},
#           {"name": "Sara", "grade": "92"}
#       ]




        # why assign an empty list to self.data?
        
        # when the object is first created

        # loader = DataLoader("students.csv")

        # python executes def __init__(self, filepath: str) -> None:

        # At that moment, the CSV has not been loaded yet.
        
        # So we need a place to store the data later.

        # We create an empty container

        # think:

        # DataLoader object
        #       filepath = "students.csv"
        #           data = []

        # The object now has a data attribute, but it's empty for the moment.

        # then what happens after?

        # self.load_data() runs

        # inside load_data(), self.data.append(row) adds the dicts one by one

        # e.g.

        # before first row, self.data = []

        # after reading Ali, self.data = [
#                                           {"name": "Ali", "grade": "85"}
#                                        ]

        # then Sara will be added, then John similarly

        self.load_data()

    def load_data(self) -> None:
        """
        Reads the CSV file and stores each row as a dictionary.
        """
        with open(self.filepath, "r") as file:
            lines = file.readlines()

        headers = lines[0].strip().split(",")

        for line in lines[1:]: # Loop through each data row in the CSV (skip the header)

            # what does lines[1:] means?

            # lines = [
#                       "name,grade\n",  # lines[0] (header)
#                       "Ali,85\n",      # lines[1]
#                       "Sara,92\n",     # lines[2]
#                       "John,70\n"      # lines[3]
#                     ]

            # lines[1:] results

            # [
#               "Ali,85\n",
#               "Sara,92\n",
#               "John,70\n"
#             ]


            values = line.strip().split(",") # Remove whitespace/newline and split the row into individual values
            # e.g. "Ali,85\n" --> ["Ali", "85"]

            row = {} # Create an empty dictionary for the current row

            for i in range(len(headers)): # Loop through each column index
                # e.g. headers = ["name", "grade"]

                # length is 2, so:
                # i = 0
                # i = 1

                row[headers[i]] = values[i] # Match each header with its corresponding value
                # e.g. row["name"] = "Ali"
                # row["grade"] = "85"

                # result:
                # {"name": "Ali", "grade": "85"}

            self.data.append(row) # Add the completed dictionary to the data list

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

        if self.count() > 0: # Accessing self.data[0] on an empty list would cause an IndexError,
            # so first check that at least one record was loaded
            print(f"First record: {self.data[0]}")