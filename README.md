# pydantic vs dataclass_factory

A small benchmark for comparing serialization/deserialization speed
using [pydantic](https://github.com/samuelcolvin/pydantic)
and [dataclass_factory](https://github.com/Tishka17/dataclass_factory).

# Run it yourself

Clone this repository and use Makefile!

```bash
git clone https://github.com/amayakasa/pydantic-vs-dataclass_factory

make
```

# Results

Results of complex model's serialization to JSON.

```bash
Tests: Serialize to JSON
 Serialize with Pydantic (1 place)
  Takes 3.7670135498046875e-05 seconds
 Serialize with dataclass_factory (2 place)
  Takes 0.00019979476928710938 seconds
```

Results of complex model's parsing from above serialized JSON.

```bash
Tests: Parsing from JSON
 Serialize with dataclass_factory (1 place)
  Takes 3.5762786865234375e-06 seconds
 Serialize with Pydantic (2 place)
  Takes 2.2649765014648438e-05 seconds
```