# Employee File Management System

A Python-based Employee File Management System that collects and validates employee details, prevents duplicate employee IDs, and stores each employee's information in a separate text file.

## Features

* Creates a dedicated folder for employee records
* Takes employee ID, name, and salary as input
* Validates required employee details
* Validates employee ID as a numeric value
* Validates salary as a positive number
* Prevents duplicate employee IDs
* Creates a separate `.txt` file for each employee
* Uses custom exception handling for duplicate IDs
* Handles file-system and unexpected errors

## Project Structure

```text
Employee-File-Management/
│
├── main.py
├── Employee/
│   ├── John_101_2026-09-10.txt
│   └── Alice_102_2026-09-10.txt
│
└── README.md
```

## Technologies & Concepts

* Python 3
* File Handling
* `os` Module
* Exception Handling
* Custom Exceptions
* Input Validation
* String Manipulation
* Loops
* Functions and Variables

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd Employee-File-Management
```

### 3. Run the program

```bash
python main.py
```

## Workflow

```text
Enter Employee Details
        ↓
Validate Input
        ↓
Check Duplicate Employee ID
        ↓
Create Employee File
        ↓
Store Employee Information
```

## File Format

Each employee record is stored as a `.txt` file using the following naming format:

```text
EmployeeName_EmployeeID_Date.txt
```

Example:

```text
John_101_2026-09-10.txt
```

The file contains:

```text
Employee_id : 101
Employee_name : John
Employee_salary : 50000.0
```

## Exception Handling

The application handles:

* Empty employee details
* Invalid employee IDs
* Invalid salary values
* Non-positive salaries
* Duplicate employee IDs
* Unexpected runtime errors

A custom `IdAlreadyExist` exception is used to handle duplicate employee IDs.

## Author

**Komal Rathod**

B.Tech — Artificial Intelligence & Data Science
