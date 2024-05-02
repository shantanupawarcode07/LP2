class Employee:
    def __init__(self, name):
        self.name = name
        self.parameters = {}

def evaluate_employee(employee):
    performance_score = 0
    total_weight = 0

    # Define weights for each parameter (can be adjusted as needed)
    weights = {
        "Attendance": 0.1,
        "Quality of Work": 0.2,
        "Teamwork": 0.15,
        "Communication Skills": 0.1,
        "Problem Solving": 0.15,
        "Adaptability": 0.15,
        "Initiative": 0.15
    }

    # Calculate weighted sum of parameter scores
    for param, score in employee.parameters.items():
        if param in weights:
            performance_score += (score * weights[param])
            total_weight += weights[param]
          

    # Normalize the performance score
    
    total_weight=total_weight*10
    performance_score = (performance_score / total_weight) * 100
    print(performance_score)

    # Evaluate performance
    if performance_score >= 90:
        return f"{employee.name} has outstanding performance."
    elif performance_score >= 70:
        return f"{employee.name} has good performance."
    elif performance_score >= 50:
        return f"{employee.name} has satisfactory performance."
    else:
        return f"{employee.name} needs improvement in performance."

# Define parameters for evaluation
parameters = [
    "Attendance",
    "Quality of Work",
    "Teamwork",
    "Communication Skills",
    "Problem Solving",
    "Adaptability",
    "Initiative"
]

# Interactive evaluation
def interactive_evaluation():
    name = input("Enter employee's name: ")
    employee = Employee(name)

    print(f"Please rate {employee.name}'s performance on a scale of 1 to 10 for the following criteria:")

    for param in parameters:
        rating = int(input(f"Rating for {param} (1-10): "))
        if rating < 1 or rating > 10:
            print("Rating must be between 1 and 10.")
            return
        employee.parameters[param] = rating

    print("\nEvaluation Result:")
    print(evaluate_employee(employee))

# Perform evaluation interactively
while True:
    interactive_evaluation()
    if input("Do you want to evaluate another employee? (yes/no): ").lower() != 'yes':
        break
