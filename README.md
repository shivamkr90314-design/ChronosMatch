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
