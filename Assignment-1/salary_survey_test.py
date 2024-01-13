import csv

class CompensationCSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.compensation_data = []

    def read_csv(self):
        with open(self.file_path, 'r', newline='') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                self.compensation_data.append({
                    'role': row.get('role', ''),
                    'salary': float(row.get('salary', 0)),
                    'currency': row.get('currency', ''),
                    'city': row.get('city', ''),
                    'timestamp': row.get('timestamp', '')
                })

    def get_compensation_data(self):
        return self.compensation_data
