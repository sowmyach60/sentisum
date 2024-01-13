import csv
from Compensation import Compensation
import Transformer
from Constants import DEFAULT_CURRENCY

class CsvReader():
    def read_csv(self,file_path):
        pass

class CsvReaderFormat1(CsvReader):
    def read_csv(self,file_path):
        compensations = []
        with open(file_path, 'r', newline='',encoding="utf8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                salary = Transformer.get_salary(row["What is your annual salary?"])
                currency = Transformer.get_currency(row["Please indicate the currency"],row['If "Other," please indicate the currency here: '])
                city = Transformer.get_city(row["Where are you located? (City/state/country)"])
                timestamp = row["Timestamp"]
                role = row["Job title"]
                compensation = Compensation(role, salary, currency, city, timestamp)
                compensations.append(compensation)
        return compensations

class CsvReaderFormat2(CsvReader):
    def read_csv(self,file_path):
        compensations = []
        with open(file_path, 'r', newline='',encoding="utf8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                salary = Transformer.get_total_salary(row["Total Base Salary in 2018 (in USD)"],row["Total Bonus in 2018 (cumulative annual value in USD)"],row["Total Stock Options/Equity in 2018 (cumulative annual value in USD)"])
                currency = DEFAULT_CURRENCY
                city = Transformer.get_city(row["Primary Location (City)"])
                timestamp = row["Timestamp"]
                role = row["Job Title In Company"]
                compensation = Compensation(role, salary, currency, city, timestamp)
                compensations.append(compensation)
        return compensations

class CsvReaderFormat3(CsvReader):
    def read_csv(self,file_path):
        compensations = []
        with open(file_path, 'r', newline='',encoding="utf8") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                currency = Transformer.get_currency_from_salary(row["Annual Base Pay"])
                salary = Transformer.get_total_salary(row["Annual Base Pay"],row["Annual Bonus"],row["Annual Stock Value/Bonus"],row["Signing Bonus"])
                city = Transformer.get_city(row["Location"])
                timestamp = row["Timestamp"]
                role = row["Job Title"]
                compensation = Compensation(role, salary, currency, city, timestamp)
                compensations.append(compensation)
        return compensations


