STANDARDS = [
    {
        "title": "SQL Injection Prevention",
        "category": "Security",
        "content": """
Never concatenate user input directly into SQL queries.
Use parameterized queries or ORM methods.
"""
    },

    {
        "title": "Hardcoded Secrets",
        "category": "Security",
        "content": """
Passwords, API keys, and tokens must never be hardcoded.
Use environment variables or secret managers.
"""
    },

    {
        "title": "Meaningful Function Names",
        "category": "Readability",
        "content": """
Function names should clearly describe behavior.

Bad:
def x():

Good:
def calculate_total_price():
"""
    },

    {
        "title": "Avoid Duplicate Code",
        "category": "Maintainability",
        "content": """
Duplicate code increases maintenance cost.

Bad:
def add(a,b):
    return a+b

def sum_numbers(x,y):
    return x+y

Good:
def add_numbers(a,b):
    return a+b
"""
    },

    {
        "title": "DRY Principle",
        "category": "Maintainability",
        "content": """
Follow the Don't Repeat Yourself principle.

Extract repeated logic into reusable functions or classes.
"""
    },

    {
        "title": "Use Type Hints",
        "category": "Best Practice",
        "content": """
Use type hints for better readability and static analysis.

Good:
def calculate_total(price: float) -> float:
    return price
"""
    },

    {
        "title": "Avoid Infinite Loops",
        "category": "Bug Risk",
        "content": """
Infinite loops without exit conditions can freeze applications.

Bad:
while True:
    print("running")
"""
    },

    {
        "title": "Input Validation",
        "category": "Security",
        "content": """
Always validate user input before processing it.
"""
    },

    {
        "title": "Exception Handling",
        "category": "Reliability",
        "content": """
Handle exceptions properly instead of allowing crashes.
"""
    },

    {
        "title": "Avoid Magic Numbers",
        "category": "Readability",
        "content": """
Avoid unexplained numeric constants.

Bad:
if age > 18:

Good:
MINIMUM_AGE = 18
if age > MINIMUM_AGE:
"""
    }
]