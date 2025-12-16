# CLInventory

Command-line inventory management system with full CRUD operations for managing business resources.

## About

First Python project, developed as a learning exercise to practice object-oriented programming, database integration, and software architecture principles. Built within two weeks of starting Python.

## Features

Complete CRUD (Create, Read, Update, Delete) functionality for:
- **Employees**: Manage staff records
- **Clients**: Track customer information
- **Providers**: Maintain supplier database
- **Products**: Catalog inventory items
- **Sales**: Record and track transactions

## Architecture

Modular design with clear separation of concerns:

```
CLInventory/
├── main.py          # Entry point and main menu loop
└── src/
    ├── database.py  # Database operations and models
    ├── cli.py       # User interface and interaction
    └── config.py    # Configuration settings
```

This structure separates business logic from presentation, making the codebase easier to maintain and future-proof for potential API conversion.

## Tech Stack

- Python
- SQLite
- PyInstaller (for executable generation)
- VS Code

## Technical Highlights

- Menu-driven interface using `while True` loops with `match` statements
- Clean separation between data layer and interface layer
- Compiled to standalone executable for easy distribution
- Modular architecture designed with future API conversion in mind

## Status

Completed learning project. Functional and ready for portfolio demonstration.

## Future Considerations

Originally planned for API conversion, but currently on hold to focus on data science and machine learning fundamentals. The modular architecture makes this upgrade straightforward when needed.

## Purpose

Educational project demonstrating:
- Python fundamentals and syntax
- Database integration with SQLite
- Software architecture and separation of concerns
- CLI application development
- Distribution and deployment practices
