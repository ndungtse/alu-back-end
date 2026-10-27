# API

Python scripts that consume the [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
REST API to report on employees' TODO lists and export them to CSV and JSON.

## Requirements

- Ubuntu 14.04 LTS, `python3` (3.4.3)
- [`requests`](https://pypi.org/project/requests/)

## Files

| File | Description |
| --- | --- |
| `0-gather_data_from_an_API.py` | Prints an employee's TODO list progress and the titles of their completed tasks. |
| `1-export_to_CSV.py` | Exports all tasks of an employee to `USER_ID.csv`. |
| `2-export_to_JSON.py` | Exports all tasks of an employee to `USER_ID.json`. |
| `3-dictionary_of_list_of_dictionaries.py` | Exports the tasks of all employees to `todo_all_employees.json`. |

## Usage

```
$ ./0-gather_data_from_an_API.py 2
$ ./1-export_to_CSV.py 2
$ ./2-export_to_JSON.py 2
$ ./3-dictionary_of_list_of_dictionaries.py
```
