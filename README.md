# Search Engine

A simple and extensible search engine library in Python.

## Features

- Tokenization
- In-memory storage
- TF-IDF ranking algorithm
- Extensible architecture to add custom tokenizers, storage, and ranking algorithms

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository

```git
git clone https://github.com/chugunov/search-engine.git
```

2. Change directory to the cloned repository

```sh
cd search-engin
```

3. Install the required dependencies

```sh
pip install -r requirements.txt
```

### Usage

```python
from search.engine import Engine

# Initialize the search engine
engine = Engine()

# Index documents
engine.index(1, {"text:": "The cat is on the mat"})
engine.index(2, {"text:": "My dog and cat are the best"})
engine.index(3, {"text:": "The locals are playing"})

# Perform a search
results = engine.search("The cat")

for result in results:
    print(result)
```
