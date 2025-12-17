
# Student Grade Management System

A Python-based CLI application for managing and analyzing student grades across multiple subjects. The system provides comprehensive grade tracking, statistical analysis, and performance reporting for educational purposes.

## Features

- **Student Data Collection**: Input student names and grades with comprehensive validation
- **Grade Validation**: Ensures all grades are within valid range (0-100)
- **Individual Analysis**: Calculates best grades and averages per student
- **Subject Averages**: Computes average performance across all students per subject
- **Overall Statistics**: Provides overall average grade across all subjects
- **Failure Detection**: Identifies and reports failing grades (≤55)
- **Input Protection**: Robust error handling for all user inputs

## Installation

No installation required. Simply ensure you have Python 3.6+ installed.

```bash
python student_grades.py
```

## Usage

### Running the Program

1. Execute the script
2. Enter the number of students
3. For each student, provide:
   - Name
   - English grade
   - Math grade
4. View comprehensive analysis and statistics

### Example Session

Enter the number of students: 2

Enter details for student 1:  
Enter student's name: Alice Johnson  
Enter English grade: 85  
Enter Math grade: 92

Enter details for student 2:  
Enter student's name: Bob Smith  
Enter English grade: 45  
Enter Math grade: 78

Student Information:  
Student Alice Johnson, Best Grade: 92.00, Average Grade: 88.50  
Student Bob Smith, Best Grade: 78.00, Average Grade: 61.50

Average grades per subject:  
English: 65.00  
Math: 85.00

Overall average grade across all subjects: 75.00

Failing grades per student:  
Alice Johnson: 0 failing grade(s)  
Bob Smith: 1 failing grade(s)

Total failing grades across all students: 1

## Configuration

### Constants

You can modify these constants at the top of the file to adjust system behavior:

PASSING_GRADE = 55 # Minimum grade to pass  
MIN_GRADE = 0 # Minimum allowed grade  
MAX_GRADE = 100 # Maximum allowed grade

## Functions

### Core Functions

#### `get_grade(subject)`
Prompts for and validates a grade for a specific subject.

**Parameters:**
- `subject` (str): Subject name (e.g., "English", "Math")

**Returns:**
- `float`: Valid grade between 0-100

**Validation:**
- Rejects negative numbers
- Rejects values > 100
- Handles non-numeric input

#### `get_student_info()`
Collects complete student information including name and grades.

**Returns:**
- `dict`: Dictionary with keys 'Name', 'English', 'Math'

**Validation:**
- Ensures non-empty names
- Validates all grade inputs

#### `print_student_info(students)`
Displays individual student statistics.

**Parameters:**
- `students` (list): List of student dictionaries

**Output:**
- Student name
- Best grade across subjects
- Personal average grade

#### `calculate_average_grades(students)`
Computes subject and overall averages.

**Parameters:**
- `students` (list): List of student dictionaries

**Returns:**
- `tuple`: (dict of subject averages, float overall average)

**Calculations:**
- Average per subject
- Overall average across all subjects and students

#### `calculate_failing_grades(students)`
Identifies and reports failing grades.

**Parameters:**
- `students` (list): List of student dictionaries

**Output:**
- Failing grades per student
- Total failing grades in the system

#### `main()`
Main program loop handling user interaction and orchestration.

## Input Validation

### Name Validation
- Cannot be empty
- Whitespace automatically trimmed
- Prompts until valid name provided

### Grade Validation
- Must be numeric (int or float)
- Range: 0-100
- Clear error messages for out-of-range values
- Continuous prompting until valid input

### Student Count Validation
- Must be a positive integer
- Must be greater than 0
- Handles non-integer input gracefully

## Grade System

### Passing Criteria
- **Passing Grade**: > 55
- **Failing Grade**: ≤ 55

### Grading Scale Reference
90-100: Excellent  
80-89: Very Good  
70-79: Good  
56-69: Satisfactory  
0-55: Failing

## Output Reports

The system generates four main reports:

### 1. Student Information Report
Individual analysis for each student showing best grade and personal average.

### 2. Subject Average Report
Average performance across all students for each subject.

### 3. Overall Average Report
Combined average across all subjects and all students.

### 4. Failing Grades Report
Detailed breakdown of failing grades per student and system-wide total.

## Error Handling

The system handles various error scenarios:

- **Invalid Grade Input**: Non-numeric values
- **Out-of-Range Grades**: Values < 0 or > 100
- **Empty Names**: Blank or whitespace-only names
- **Invalid Student Count**: Non-integer or negative values
- **Zero Division**: Protected when no students present

## Technical Details

### Data Structure

Student data is stored as a list of dictionaries:

students = [  
{  
'Name': 'Alice Johnson',  
'English': 85.0,  
'Math': 92.0  
},  
{  
'Name': 'Bob Smith',  
'English': 45.0,  
'Math': 78.0  
}  
]

### Performance
- **Time Complexity**: O(n) where n is number of students
- **Space Complexity**: O(n) for storing student data

## Requirements

- Python 3.6 or higher
- No external dependencies

## Future Enhancements

### Potential Features
- **Data Persistence**: Save/load student data from files (JSON, CSV)
- **More Subjects**: Support for additional subjects beyond English and Math
- **Grade History**: Track grades over multiple semesters
- **Visual Reports**: Generate charts and graphs
- **Export Functionality**: Export reports to PDF or Excel
- **Grade Distribution**: Show histogram of grade distributions
- **Student Search**: Find specific students by name
- **Edit Capability**: Modify existing student records
- **Weighted Grades**: Support for weighted subject importance
- **Letter Grades**: Convert numeric grades to letter grades
- **Class Comparison**: Compare multiple classes or sections
- **Attendance Tracking**: Integrate attendance with grades

### Code Improvements
- Unit tests for all functions
- Command-line arguments for batch processing
- Configuration file support
- Logging system for audit trails
- Database integration for larger datasets

## Best Practices Implemented

- **PEP 8 Compliance**: Follows Python style guidelines
- **Constants**: Magic numbers replaced with named constants
- **Comprehensive Docstrings**: All functions documented
- **Input Validation**: Robust error handling throughout
- **Separation of Concerns**: Clear function responsibilities
- **DRY Principle**: No code duplication
- **Meaningful Names**: Clear, descriptive variable and function names

## Educational Use Cases

This system is ideal for:
- Small classroom grade management
- Educational programming exercises
- Learning Python fundamentals
- Understanding data validation
- Practicing error handling
- Teaching basic statistics

## Contributing

Contributions are welcome! Areas for contribution:
- Additional statistical analyses
- New report formats
- Enhanced visualization
- Performance optimizations
- Extended test coverage
- Documentation improvements

## License

This project is licensed under the MIT License.

## Acknowledgments

Developed with feedback from code review focusing on:
- Input validation best practices
- PEP 8 style guidelines
- Comprehensive documentation
- Error handling patterns
- Clean code principles

## Support

For questions, issues, or suggestions, please open an issue in the repository.

---

**Note**: This system is designed for educational purposes and small-scale grade management. For production use with larger datasets, consider implementing database storage and additional security features.



