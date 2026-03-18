---
paths:
  - "**/*.php"
  - "**/composer.json"
---
# PHP Rules

## Architecture
- Controllers: auth check, input validation, response formatting only
- Business logic lives in Service classes — testable without HTTP
- Inject dependencies via constructor — no service locator globals
- Depend on interfaces not concrete classes
- Value objects for: money amounts, identifiers, date ranges

## Security
- Validate ALL request input at the controller boundary
- PDO prepared statements for ALL dynamic queries — never string concat
- `password_hash(PASSWORD_BCRYPT)` — never MD5, SHA1, or plain text
- `password_verify()` for comparison — never direct string compare
- `session_regenerate_id(true)` after login and privilege changes
- CSRF token on all POST/PUT/PATCH/DELETE requests
- Never expose DB structure or stack traces to end users
- Secrets in `.env` — never in committed config files
- Run `composer audit` in CI

## Naming
- Classes: `PascalCase` — `DrugInventoryService`
- Methods: `camelCase` — `calculateAverageConsumption()`
- Constants: `UPPER_SNAKE` — `OVERSTOCK_THRESHOLD`
- DB tables: `snake_case` plural — `drug_items`

## Error Handling
```php
if (empty($data['drug_id'])) {
    throw new \InvalidArgumentException('drug_id is required');
}
try {
    $result = $this->service->process($data);
} catch (NotFoundException $e) {
    return response()->json(['error' => 'Not found'], 404);
} catch (\Exception $e) {
    Log::error('Processing failed', ['error' => $e->getMessage()]);
    return response()->json(['error' => 'Internal error'], 500);
}
```

## Testing

### Test-First Always
- Write the test BEFORE the implementation
- Verify test FAILS before writing code
- Write minimal code to make test pass
- Refactor only when tests are green

### PHPUnit Conventions
- Test class: `{ClassName}Test`
- Test method: `test_{what}_{expected_result}`
- One assertion concept per test method
- Use `setUp()` for shared fixtures

### What to Test
- All public methods and business logic in Services
- All API endpoints (integration tests)
- Edge cases: null, empty, boundary values, Arabic text
- Error paths — not just happy path

### What to Mock
- External HTTP calls (Telegram API, etc.)
- Time-dependent code (`Carbon::now()` → `Carbon::setTestNow()`)
- File system operations, email sending

### Coverage
- Minimum 80% line coverage
- 100% for: financial calculations, auth logic, security code

### PHPUnit Template
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
    public function test_{what}_{expected_result}(): void
    {
        // Arrange
        $input = [...];
        // Act
        $result = $this->service->method($input);
        // Assert
        $this->assertEquals($expected, $result);
    }
}
```
