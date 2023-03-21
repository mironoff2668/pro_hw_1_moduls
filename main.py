from datetime import datetime
from accounting.application.salary import calculate_salary
from accounting.db.people import get_employees


if __name__ == '__main__':
    print(datetime.today())
    calculate_salary()
    get_employees()