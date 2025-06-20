import csv
import argparse
from dataclasses import dataclass
from typing import List

@dataclass
class EmployeePerformance:
    name: str
    score: float
    category: str

def categorize(score: float) -> str:
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    else:
        return "Needs Improvement"

def read_employees(csv_path: str) -> List[EmployeePerformance]:
    employees = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                score = float(row['score'])
            except (ValueError, KeyError):
                continue
            category = categorize(score)
            employees.append(EmployeePerformance(name=row.get('name', ''), score=score, category=category))
    return employees

def print_report(employees: List[EmployeePerformance]):
    if not employees:
        print("No employee data available")
        return
    scores = [e.score for e in employees]
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    print(f"Average score: {average:.2f}")
    print(f"Highest score: {highest:.2f}")
    print(f"Lowest score: {lowest:.2f}")
    print("\nEmployee Performance:\n")
    for e in employees:
        print(f"{e.name}: {e.score:.2f} ({e.category})")

def main():
    parser = argparse.ArgumentParser(description='Employee performance evaluator')
    parser.add_argument('csv', help='Path to CSV file with columns: name,score')
    args = parser.parse_args()
    employees = read_employees(args.csv)
    print_report(employees)

if __name__ == '__main__':
    main()
