---
paths:
  - "**/*.php"
  - "**/composer.json"
---
# PHP Patterns

## Thin Controllers, Explicit Services
- Controllers handle: auth check, input validation, response formatting
- Business logic lives in Service classes — testable without HTTP

## DTOs and Value Objects
- Replace associative arrays with DTOs for requests and API responses
- Value objects for: money amounts, identifiers, date ranges

## Dependency Injection
- Inject dependencies via constructor — no service locator globals
- Depend on interfaces not concrete classes

## Repository Pattern
```php
interface DrugRepositoryInterface {
    public function findById(int $id): ?Drug;
    public function findOverstocked(int $threshold): Collection;
}
```

## Error Handling
```php
// Always validate before processing
if (empty($data['drug_id'])) {
    throw new \InvalidArgumentException('drug_id is required');
}

// Use specific exception types
try {
    $result = $this->service->process($data);
} catch (NotFoundException $e) {
    return response()->json(['error' => 'Not found'], 404);
} catch (\Exception $e) {
    Log::error('Processing failed', ['error' => $e->getMessage()]);
    return response()->json(['error' => 'Internal error'], 500);
}
```

## Naming
- Classes: `PascalCase` — `DrugInventoryService`
- Methods: `camelCase` — `calculateAverageConsumption()`
- Constants: `UPPER_SNAKE` — `OVERSTOCK_THRESHOLD`
- DB tables: `snake_case` plural — `drug_items`
