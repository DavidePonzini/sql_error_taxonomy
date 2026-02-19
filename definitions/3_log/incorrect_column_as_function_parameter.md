## Incorrect column as function parameter
### Definition
An incorrect column is used as a parameter for a function, leading to unintended results.

### Data demand
Calculate the average unit price of products in inventory.

### Example
```sql
SELECT AVG(quantity)
FROM inventory;
```

### Explaination
The query calculates the average of the `quantity` column instead of the `unit_price` column, which is not what the data demand specifies. This results in an incorrect calculation of the average unit price.

### Correction
```sql
SELECT AVG(unit_price)
FROM inventory;
```

