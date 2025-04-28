import csv

# Define the CSV file path
csv_file = 'students.csv'

# Set the threshold grade
threshold = 80

# List to hold student names with average grade above the threshold
students_above_threshold = []

# Read the CSV file and process it
with open(csv_file, mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Parse grades (assuming grades are numerical and in the 'grade' column)
        grades = list(map(int, row['grade'].split(',')))  # Assuming grades are separated by commas
        avg_grade = sum(grades) / len(grades)
        
        # Check if the average grade is above the threshold
        if avg_grade > threshold:
            students_above_threshold.append(row['name'])

# Print the students who passed the grade threshold
print('Students with average grade above the threshold:')
for student in students_above_threshold:
    print(student)
