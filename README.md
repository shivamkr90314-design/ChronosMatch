# ChronosMatch

An educational Python trading-engine simulation.

## Features
- Buy and sell order management
- Price-time priority
- Full and partial fills
- SQLite trade history
- memoryview demonstration
- Performance benchmark
- Automated unit tests

## Requirements
Python 3.10 or newer.

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
## Project Workflow

ChronosMatch follows a simple order processing workflow:

1. Accept BUY and SELL orders from users.
2. Validate order details such as price and quantity.
3. Store orders in the Order Book.
4. Arrange orders using price-time priority.
5. Match BUY and SELL orders when their prices cross.
6. Execute full or partial trades.
7. Save executed trade records in the SQLite database.
8. Measure basic performance using the benchmarking module.

## Project Objective

The main objective of ChronosMatch is to understand
how a trading engine manages orders, matches trades,
and maintains trade records using Python.
## Core Components

### 1. Order Management
Handles BUY and SELL orders and validates order details.

### 2. Order Book
Stores and organizes orders according to price-time priority.

### 3. Matching Engine
Matches compatible BUY and SELL orders and supports partial execution.

### 4. Database
Uses SQLite to store executed trade records.

### 5. Performance Module
Demonstrates memoryview and measures basic order-processing performance.

### 6. Testing
Uses pytest to check order validation and matching functionality.
ChronosMatch: Zero-Copy High-Frequency Trading Engine

1. Project Introduction

ChronosMatch is a Python-based educational simulation of a high-frequency trading engine. It demonstrates how buy and sell orders can be managed and matched using price-time priority.

The project focuses on order management, trade execution, partial order matching, trade history storage, and basic performance measurement.

2. Core Components

Order Management – "order.py"

- Defines Order and Trade data structures.
- Stores order details such as ID, side, price, and quantity.
- Validates order information.

Order Book – "order_book.py"

- Maintains buy and sell orders.
- Sorts orders based on price and time priority.
- Provides an order book snapshot.

Matching Engine – "matching_engine.py"

- Matches compatible buy and sell orders.
- Supports full and partial order execution.
- Uses price-time priority for matching.

Database – "database.py"

- Uses SQLite to store trade records.
- Supports saving and retrieving trade history.

Performance Module – "performance.py"

- Demonstrates memoryview usage.
- Performs basic performance benchmarking.

Test Module – "tests/test_engine.py"

- Tests order validation.
- Tests matching logic.
- Checks full and partial order execution.
- Verifies price-time priority.

3. Technologies Used

- Python
- SQLite
- Pytest
- VS Code
- Git and GitHub

4. Project Objective

The objective is to understand the basic working principles of a trading engine through order management, matching algorithms, database integration, and testing.

5. Project Status

This project is an educational trading-engine simulation. It is not a production-ready high-frequency trading system.
