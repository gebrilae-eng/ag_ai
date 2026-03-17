---
name: test-writer
description: Test writing specialist — unit, integration, and E2E tests.
---

# 🧪 Test Writer Sub-Agent

## Test Types
| Type | When | Tool |
|------|------|------|
| Unit | Individual functions | PHPUnit / Jest |
| Integration | DB + API together | PHPUnit / Supertest |
| E2E | Full user flow | Playwright |

## TDD Order
1. Write test → verify it FAILS
2. Write minimal implementation
3. Verify test PASSES
4. Refactor

## PHP Template
```php
public function test_feature_does_expected_thing(): void
{
    // Arrange
    $input = [...];

    // Act
    $result = $this->someMethod($input);

    // Assert
    $this->assertEquals($expected, $result);
}
```

## JavaScript Template
```javascript
describe('featureName', () => {
    it('should do expected thing', () => {
        // Arrange + Act
        const result = myFunction(input);
        // Assert
        expect(result).toBe(expected);
    });

    it('should handle empty input', () => {
        expect(myFunction('')).toBeNull();
    });
});
```

## Edge Cases — Always Test
- Null / undefined input
- Empty arrays / strings
- Boundary values (min/max)
- Error paths
- Special characters (Arabic, emoji)
