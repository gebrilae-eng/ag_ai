---
paths:
  - "**/*.php"
---
# PHP Testing Rules

## Test-First Always
- Write the test BEFORE the implementation
- Verify test FAILS before writing code
- Write minimal code to make test pass
- Refactor only when tests are green

## PHPUnit Conventions
- Test class name: `{ClassName}Test`
- Test method name: `test_{what}_{expected_result}`
- One assertion concept per test method
- Use `setUp()` for shared test fixtures

## What to Test
- All public methods
- All business logic in Services
- All API endpoints (integration tests)
- Edge cases: null, empty, boundary values, Arabic text
- Error paths — not just happy path

## What to Mock
- External HTTP calls (Telegram API, etc.)
- Time-dependent code (`Carbon::now()`)
- File system operations
- Email sending

## Coverage Requirements
- Minimum 80% line coverage for all code
- 100% for: financial calculations, auth logic, security code

## PHPUnit Structure
```php
class DrugServiceTest extends TestCase
{
    private DrugService $service;

    protected function setUp(): void
    {
        parent::setUp();
        $this->service = new DrugService(
            $this->createMock(DrugRepositoryInterface::class)
        );
    }

    public function test_calculate_avg_consumption_returns_top3_average(): void
    {
        // Arrange, Act, Assert
    }

    public function test_calculate_avg_consumption_returns_zero_for_new_drug(): void
    {
        // Edge case
    }
}
```
