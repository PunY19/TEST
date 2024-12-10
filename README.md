# Thai Dependency Parser
`ThaiDepparse` is a Thai dependency parser trained

## Content
1. [Installation](#installation)
2. [Usage](#Usage)

## Installation
`ThaiDepparse` can be installed usig `pip`ː
```
pip install ThaiDepparse
```

## Usage
### Initalizing

```python
from ThaiDepparse import depparse

nlp = load_model()
```

```python
from ThaiDepparse import depparse

text = 'ฉันอยากกินข้าวที่แม่ทำ'

dep = depparse(text, nlp)
```