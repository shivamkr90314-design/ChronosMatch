# ChronosMatch - Test Plan

## 1. Objective
To verify the correct working of the ChronosMatch trading engine.

## 2. Test Cases

| Test Case | Description | Expected Result |
|---|---|---|
| TC01 | Create BUY order | Order accepted |
| TC02 | Create SELL order | Order accepted |
| TC03 | Invalid price | Validation error |
| TC04 | Match BUY and SELL | Trade executed |
| TC05 | Partial matching | Remaining quantity updated |
| TC06 | Price-time priority | Older order gets priority |
| TC07 | Save trade in database | Trade stored successfully |

## 3. Testing Tools
- Python
- Pytest
- SQLite

## 4. Expected Outcome
All test cases should pass successfully.
