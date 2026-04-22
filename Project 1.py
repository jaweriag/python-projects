import pandas as pd
class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.math_score = float(math_score)
        self.science_score = float(science_score)
        self.status = ""

    def check_status(self):
        average = (self.math_score + self.science_score) / 2
        if average >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"
df=pd.read_csv('raw_grade.csv')


df = df.fillna(0)

# 3. Integration
student_results = []

for index, row in df.iterrows():
    # Instantiate object
    s = Student(row['Student_Name'], row['Math_Score'], row['Science_Score'])
    # Call method
    s.check_status()

    # Collect data
    student_results.append({
        'Student_Name': s.name,
        'Math_Score': s.math_score,
        'Science_Score': s.science_score,
        'Status': s.status
    })

# 4. Exporting (Pandas)
final_df = pd.DataFrame(student_results)
final_df['School_Year'] = "2023-2024"

final_df.to_csv('final_grades.csv', index=False)

# Final Output Display
print("Final Grades Report:")
print(final_df)