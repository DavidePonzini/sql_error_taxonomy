# Error Definitions

This document defines the four top-level SQL error categories adopted in this repository.

Definitions are grounded in **observable properties of queries**, with criteria chosen to remain suitable for **automated detection** while preserving **pedagogical interpretability**.

Unless explicitly stated otherwise, definitions rely solely on:
- the SQL query itself,
- the database schema (metadata),
- and, when required, a reference query expressing the data demand.

No assumptions about student intent are made at this level.

---

# Schema definition
For the following queries, we will be referencing the following schema, adapted from Miedema et Al [^miedema_identifying2022].
Underlined attributes collectively form the primary key for each table.

| Table name | Attributes                          |
| :--------- | :---------------------------------- |
| customer   | <ins>cID</ins>, cName, street, city |
| store      | <ins>sID</ins>, sName, street, city |
| product    | <ins>pID</ins>, pName, suffix       |
| inventory  | <ins>sID</ins>, <ins>pID</ins>, date, quantity, unit_price |

---

# Syntax Errors

**Definition.**  
A *syntax error* occurs when a SQL query violates the syntactic or typing rules of the SQL language and **cannot be executed by the DBMS**.

**Key properties.**
- The DBMS rejects the query at parse time or during static validation.
- No result set is produced.
- The error can be detected without knowledge of the data demand.
- The error is independent of the database instance contents.

**Pedagogical interpretation.**  
Syntax errors typically reflect difficulties with SQL grammar, clause structure, or expression formation, and often arise in early stages of learning.

## Errors
### SYN-1 Ambiguous Database object
#### 1. Ambiguous column  
**Definition:** referring to a column present in at least two tables
referenced in the FROM clause, without specifying which table
the column belongs to.

**Example:** 
```sql
SELECT street
FROM customer, store
```

**Explaination:** both tables contain a column named `street`. Without specifying the table, the database cannot determine which `street` to use.

**Correction:**

```sql
SELECT customer.street
FROM customer, store
```

#### 2. Ambiguous function
**Definition:** 

**Example:** 
```sql

```

**Explaination:** 

**Correction:**

```sql

```


---

# Semantic Errors

**Definition.**  
A *semantic error* occurs when a SQL query is syntactically valid and executable, but its evaluation is **semantically flawed regardless of the data demand**, producing a result that is always meaningless.

**Key properties.**
- The query executes successfully.
- The result set is intrinsically invalid (e.g., always empty or logically inconsistent).
- The error can be detected without reference to the intended task.
- The behavior holds for any possible database instance.

**Pedagogical interpretation.**  
These errors often signal misconceptions about logical conditions, boolean reasoning, or the meaning of operators in SQL.

---

# Logic Errors

**Definition.**  
A *logic error* occurs when a SQL query is syntactically and semantically valid, but **does not satisfy the given data demand**.

**Key properties.**
- The query executes successfully.
- A result set is produced.
- The result does not match the expected outcome defined by the data demand.
- Detection requires comparison with at least one correct reference query or specification.

**Pedagogical interpretation.**  
Logic errors reflect misunderstandings of the problem requirements, relational reasoning, or the mapping between natural language requests and SQL constructs.

---

# Complications

**Definition.**  
A *complication* occurs when a SQL query **satisfies the data demand**, but does so in an **unnecessarily complex, redundant, or non-idiomatic way**.

**Key properties.**
- The query returns a correct result set.
- One or more components are redundant, superfluous, or replaceable by simpler constructs.
- Removing or simplifying these components does not change the result.
- Detection requires knowledge of the data demand.

**Pedagogical interpretation.**  
Complications often indicate partial understanding or overgeneralization of SQL constructs, and provide opportunities for feedback focused on readability, efficiency, and idiomatic query formulation.

---

# Notes on Category Boundaries

- The four top-level categories are **mutually exclusive as primary labels**, but a single query may exhibit **multiple issues**.
- Classification prioritizes **observable query behavior** over inferred intent.
- The distinction between *semantic* and *logic* errors hinges on whether the data demand is required for detection.

# References
[^miedema_identifying2018]: Miedema, Daphne, Efthimia Aivaloglou, and George Fletcher. "Identifying SQL misconceptions of novices: Findings from a think-aloud study." ACM Inroads 13.1 (2022): 52-65. https://dx.doi.org/10.1145/3514214