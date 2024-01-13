class Compensation:
    def __init__(self, role, salary, currency, city, timestamp):
        self.role = role
        self.salary = salary
        self.currency = currency
        self.city = city
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "role": self.role,
            "salary": self.salary,
            "currency": self.currency,
            "city": self.city,
            "timestamp": self.timestamp
        }

    def __str__(self):
        return f"Role: {self.role}, Salary: {self.salary} {self.currency}, City: {self.city}, Timestamp: {self.timestamp}"