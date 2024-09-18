# SQL Compiler Project

Welcome to the **SQL Compiler** project! This project is designed to parse and compile SQL queries using a custom-built compiler with support for various SQL keywords and functions. This project includes lexical analysis, syntax analysis, and SQL query execution, providing extensive features for handling SQL operations.

## Features

- **Lexical Analysis**: Tokenizes SQL input into meaningful tokens.
- **Syntax Analysis**: Ensures that SQL queries conform to the grammar rules.
- **SQL Keywords Support**:
  - One-word keywords: `DEFAULT`, `UUID`, `USER`, etc.
  - No-input keywords: `CURRENT_TIMESTAMP()`, `NOW()`, `SYSDATE()`, etc.
  - One-input keywords: `RAND(x)`, etc.
  - Two-input keywords: `CONCAT()`, `POWER()`, etc.
  - Support for additional SQL functions and keywords based on custom input.
- **Error Handling**: Provides clear error messages when invalid SQL syntax or keywords are detected.
- **Customizable**: Easily extendable with new SQL keywords and functions as needed.
- **Comprehensive Parsing**: Handles identifiers, keywords, and special SQL constructs.
- **Interactive GUI**: Includes a basic Tkinter-based interface for running SQL queries and displaying results.

## Benefits

- **Extensibility**: Add new SQL features or modify existing ones with ease.
- **Error Reporting**: Provides helpful error messages and identifies where syntax issues occur.
- **Modular Design**: Clean separation between lexical analysis, syntax analysis, and query execution.
- **GUI Integration**: Quickly test your SQL queries via a graphical interface.
- **Testability**: Includes test cases for validating SQL queries.

## Tools and Technologies

- **Python 3.x**: The main language used for development.
- **Tkinter**: Provides a simple GUI for testing and running SQL queries.
- **Git**: Version control to manage project progress and collaboration.
- **LexicalAnalyzer**: Custom lexical analyzer to tokenize SQL queries.
- **SyntaxAnalyzer**: Custom syntax analyzer for parsing SQL queries and ensuring compliance with SQL grammar.
- **SQL Functions**: Comprehensive support for built-in SQL functions and easy extension for custom functions.

## Installation

### Prerequisites

- **Python 3.x**: Make sure you have Python 3.x installed on your system. You can download it from [here](https://www.python.org/downloads/).
  
- **Git**: Install Git to clone the repository. Download from [here](https://git-scm.com/downloads).

### Clone the Repository

1. Open your terminal or command prompt.
2. Run the following command to clone the repository:
    ```bash
    git clone https://github.com/your-username/SQL-Compiler-With-Python.git
    ```
3. Navigate to the project directory:
    ```bash
    cd SQL-Compiler-With-Python
    ```

### Install Dependencies

You may need to install some Python dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not yet created, you can manually install any necessary packages (like `Tkinter` or others) using `pip`:

```bash
pip install tkinter
```

## Usage

1. Navigate to the project directory.
2. Run the GUI using the following command:
    ```bash
    python GUI.py
    ```
3. You will see an interface where you can input SQL queries and test the output. For example, enter an `INSERT` query and see how the compiler processes it.

## Example Queries

Here are some example queries that can be parsed and executed by the compiler:

```sql
-- One-word keyword
INSERT INTO your_table (column1) VALUES (DEFAULT);

-- No-input keyword
INSERT INTO your_table (column1) VALUES (CURRENT_TIMESTAMP());

-- One-input keyword
INSERT INTO your_table (column1) VALUES (UUID('your_uuid_here'));

-- Two-input keyword
INSERT INTO your_table (column1) VALUES (CONCAT('string1', 'string2'));

-- Two-input keyword with multiple values
INSERT INTO your_table (column1) VALUES (CONCAT('string1', 'string2', 'string3'));
```

## Error Handling

The compiler includes detailed error reporting. If there are issues with syntax, such as missing parentheses or invalid SQL constructs, an error message will be shown in the console or GUI window.

Example error message:

```plaintext
SyntaxError: Expected identifier but found "123"
```

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
