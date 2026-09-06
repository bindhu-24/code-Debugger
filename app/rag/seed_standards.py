from app.database.connection import SessionLocal
from app.database.models import CodingStandard
from app.rag.embeddings import generate_embedding

standards = [
    {
        "title": "Use Descriptive Variable Names",
        "language": "python",
        "category": "Readability",
        "content": "Use descriptive variable names that clearly communicate the purpose of the value."
    },
    {
        "title": "Avoid Bare Except",
        "language": "python",
        "category": "Error Handling",
        "content": "Avoid bare except clauses because they catch all exceptions and can hide unexpected errors."
    },
    {
        "title": "Validate User Input",
        "language": "python",
        "category": "Security",
        "content": "Validate and sanitize user input before processing it to prevent unexpected behavior and security vulnerabilities."
    },
    {
        "title": "Avoid SQL Injection",
        "language": "python",
        "category": "Security",
        "content": "Use parameterized queries instead of constructing SQL statements by concatenating user input."
    },
    {
        "title": "Use Type Hints",
        "language": "python",
        "category": "Maintainability",
        "content": "Use type hints for function parameters and return values to improve readability and maintainability."
    },
    {
        "title": "Avoid Hardcoded Secrets",
        "language": "python",
        "category": "Security",
        "content": "Do not hardcode API keys, passwords, tokens, or other sensitive credentials in source code."
    },
    {
        "title": "Handle Division by Zero",
        "language": "python",
        "category": "Bug Risk",
        "content": "Validate divisors before performing division to prevent ZeroDivisionError."
    },
    {
        "title": "Use Specific Exceptions",
        "language": "python",
        "category": "Error Handling",
        "content": "Catch specific exception types instead of using broad exception handlers."
    },
    {
        "title": "Avoid Silent Failures",
        "language": "python",
        "category": "Error Handling",
        "content": "Do not silently ignore exceptions. Log or properly handle errors so failures can be diagnosed."
    },
    {
        "title": "Keep Functions Focused",
        "language": "python",
        "category": "Maintainability",
        "content": "Functions should have a single clear responsibility and avoid unnecessary complexity."
    },
    # 11
{
    "title": "Use PEP 8 Formatting",
    "language": "python",
    "category": "Readability",
    "content": "Follow PEP 8 formatting conventions for indentation, spacing, line length, imports, and overall Python code style."
},

# 12
{
    "title": "Use snake_case Naming",
    "language": "python",
    "category": "Readability",
    "content": "Use snake_case for variables, functions, and module names to follow standard Python naming conventions."
},

# 13
{
    "title": "Use PascalCase for Classes",
    "language": "python",
    "category": "Readability",
    "content": "Use PascalCase naming for classes so that class definitions are immediately distinguishable from functions and variables."
},

# 14
{
    "title": "Avoid Unused Imports",
    "language": "python",
    "category": "Code Quality",
    "content": "Remove imports that are not used because unnecessary imports increase clutter and can make dependencies harder to understand."
},

# 15
{
    "title": "Avoid Unused Variables",
    "language": "python",
    "category": "Code Quality",
    "content": "Remove variables that are assigned but never used because they add unnecessary complexity and may indicate incomplete code."
},

# 16
{
    "title": "Avoid Global Variables",
    "language": "python",
    "category": "Maintainability",
    "content": "Avoid unnecessary global variables because they create hidden dependencies and make code harder to test and maintain."
},

# 17
{
    "title": "Use Constants for Fixed Values",
    "language": "python",
    "category": "Maintainability",
    "content": "Store frequently used fixed values in named constants instead of repeating magic numbers or strings throughout the code."
},

# 18
{
    "title": "Avoid Magic Numbers",
    "language": "python",
    "category": "Readability",
    "content": "Replace unexplained numeric literals with descriptive constants so that their purpose is clear to other developers."
},

# 19
{
    "title": "Keep Functions Short",
    "language": "python",
    "category": "Maintainability",
    "content": "Keep functions reasonably short and focused so that they are easier to understand, test, debug, and maintain."
},

# 20
{
    "title": "Avoid Deep Nesting",
    "language": "python",
    "category": "Readability",
    "content": "Avoid deeply nested conditionals and loops because excessive nesting makes control flow difficult to understand and maintain."
},

# 21
{
    "title": "Use Early Returns",
    "language": "python",
    "category": "Readability",
    "content": "Use early returns to handle invalid or exceptional conditions before the main logic, reducing unnecessary nesting."
},

# 22
{
    "title": "Avoid Duplicate Code",
    "language": "python",
    "category": "Maintainability",
    "content": "Avoid duplicating the same logic in multiple places. Extract reusable functionality into functions or classes when appropriate."
},

# 23
{
    "title": "Use List Comprehensions Appropriately",
    "language": "python",
    "category": "Code Quality",
    "content": "Use list comprehensions for simple transformations and filtering, but avoid them when the logic becomes difficult to read."
},

# 24
{
    "title": "Use Context Managers",
    "language": "python",
    "category": "Resource Management",
    "content": "Use context managers such as with statements when working with files, database connections, locks, or other resources that require cleanup."
},

# 25
{
    "title": "Close Resources Properly",
    "language": "python",
    "category": "Resource Management",
    "content": "Ensure files, connections, sockets, and other external resources are properly closed or released after use."
},

# 26
{
    "title": "Handle File Not Found Errors",
    "language": "python",
    "category": "Error Handling",
    "content": "Handle FileNotFoundError when accessing files that may not exist instead of allowing unexpected application crashes."
},

# 27
{
    "title": "Avoid Catching Exception Broadly",
    "language": "python",
    "category": "Error Handling",
    "content": "Avoid catching the generic Exception type unless there is a clear reason because broad exception handling can hide programming errors."
},

# 28
{
    "title": "Preserve Exception Context",
    "language": "python",
    "category": "Error Handling",
    "content": "When re-raising exceptions, preserve the original exception context so that debugging information and the root cause are not lost."
},

# 29
{
    "title": "Use Logging Instead of Print",
    "language": "python",
    "category": "Observability",
    "content": "Use the logging module instead of print statements for application diagnostics so that log levels and output destinations can be controlled."
},

# 30
{
    "title": "Do Not Log Sensitive Data",
    "language": "python",
    "category": "Security",
    "content": "Never log passwords, API keys, authentication tokens, credit card information, or other sensitive user data."
},

# 31
{
    "title": "Use Environment Variables for Configuration",
    "language": "python",
    "category": "Security",
    "content": "Store environment-specific configuration such as API keys, database URLs, and service credentials in environment variables rather than source code."
},

# 32
{
    "title": "Validate API Input",
    "language": "python",
    "category": "Security",
    "content": "Validate API request parameters and payloads before processing them to prevent invalid data and unexpected application behavior."
},

# 33
{
    "title": "Avoid Command Injection",
    "language": "python",
    "category": "Security",
    "content": "Avoid constructing shell commands from untrusted user input and use safe subprocess APIs with argument lists when system commands are required."
},

# 34
{
    "title": "Avoid Unsafe Deserialization",
    "language": "python",
    "category": "Security",
    "content": "Avoid deserializing untrusted data with unsafe mechanisms such as pickle because malicious data can execute arbitrary code."
},

# 35
{
    "title": "Use Secure Password Hashing",
    "language": "python",
    "category": "Security",
    "content": "Store passwords using secure password hashing algorithms such as Argon2 or bcrypt instead of plaintext or reversible encryption."
},

# 36
{
    "title": "Use Parameterized Database Queries",
    "language": "python",
    "category": "Security",
    "content": "Use parameterized database queries or ORM query parameters instead of string concatenation when inserting user-controlled values into SQL."
},

# 37
{
    "title": "Validate Numeric Input",
    "language": "python",
    "category": "Bug Risk",
    "content": "Validate numeric input and expected ranges before performing calculations to prevent invalid values and runtime errors."
},

# 38
{
    "title": "Check for None Values",
    "language": "python",
    "category": "Bug Risk",
    "content": "Check values that may be None before accessing attributes, indexing, or performing operations that require a concrete value."
},

# 39
{
    "title": "Avoid Mutable Default Arguments",
    "language": "python",
    "category": "Bug Risk",
    "content": "Avoid using mutable objects such as lists or dictionaries as default function arguments because they are shared between function calls."
},

# 40
{
    "title": "Handle KeyError",
    "language": "python",
    "category": "Bug Risk",
    "content": "Safely access dictionary keys when the key may not exist by using get, membership checks, or appropriate exception handling."
},

# 41
{
    "title": "Handle IndexError",
    "language": "python",
    "category": "Bug Risk",
    "content": "Validate list or sequence indexes before accessing them when the index may be outside the valid range."
},

# 42
{
    "title": "Avoid Comparing Floating Point Values Directly",
    "language": "python",
    "category": "Bug Risk",
    "content": "Avoid relying on exact equality comparisons for floating point values and use an appropriate tolerance when numerical precision matters."
},

# 43
{
    "title": "Use Unit Tests",
    "language": "python",
    "category": "Testing",
    "content": "Write unit tests for important functions and business logic to detect regressions and verify expected behavior."
},

# 44
{
    "title": "Test Edge Cases",
    "language": "python",
    "category": "Testing",
    "content": "Test boundary conditions, empty inputs, invalid inputs, missing values, and other edge cases that may expose unexpected behavior."
},

# 45
{
    "title": "Avoid Hardcoded Test Dependencies",
    "language": "python",
    "category": "Testing",
    "content": "Avoid making tests dependent on specific external services or environments; use mocks, fixtures, or controlled test data when appropriate."
},

# 46
{
    "title": "Document Public Functions",
    "language": "python",
    "category": "Documentation",
    "content": "Add clear docstrings to public functions and classes to explain their purpose, parameters, return values, and important behavior."
},

# 47
{
    "title": "Keep Comments Meaningful",
    "language": "python",
    "category": "Documentation",
    "content": "Write comments that explain why complex or non-obvious logic exists instead of comments that merely repeat what the code already says."
},

# 48
{
    "title": "Avoid Long Parameter Lists",
    "language": "python",
    "category": "Maintainability",
    "content": "Avoid functions with excessive numbers of parameters because they become difficult to understand, call, test, and maintain."
},

# 49
{
    "title": "Use Dependency Injection",
    "language": "python",
    "category": "Architecture",
    "content": "Use dependency injection for external services, database sessions, and configurable components to improve testability and separation of concerns."
},

# 50
{
    "title": "Separate Business Logic from API Routes",
    "language": "python",
    "category": "Architecture",
    "content": "Keep business logic in service or domain layers instead of placing complex processing directly inside FastAPI route handlers."
},
]


def seed_standards():
    db = SessionLocal()

    try:
        existing_titles = {
            standard.title
            for standard in db.query(CodingStandard).all()
        }

        inserted = 0 
        updated = 0

        for standard in standards:
            if standard["title"] in existing_titles:
                continue
                           
            embedding = generate_embedding(standard["content"])

            db.add(
                CodingStandard(
                    **standard,
                    embedding=embedding
                )
            )

            inserted += 1
            
        db.commit()

        print(f"Inserted {inserted} new coding standards ")
        print(f"Total standards should now be: {len(existing_titles) + inserted}")
    
    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_standards()