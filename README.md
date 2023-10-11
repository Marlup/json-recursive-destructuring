# JSON Data De-structuring Functions

This Python library provides two functions for de-structuring JSON data into a structured format.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Functions](#functions)
  - [direct recursion destructure](#direct-recursion-destructuring)
  - [indirect recursion destructure](#indirect-recursion-destructuring)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

When working with JSON data, it is often useful to de-structure it into a more readable and structured format. This library offers two functions to achieve this:

1. `direct_recursive_destructure`: This function recursively de-structures a JSON object and provides information about keys, values, nesting, and key trails.

2. `indirect_recursive_json_destructure`: This function also recursively de-structures a JSON object but follows a different approach, providing information about keys, values, nesting, and key trails.

## Requirements

This requires Python 3.x.x or higher.

## Functions

### Direct-recursion-destructuring

```python
def direct_recursive_destructure(data: dict, 
                                 n_nestings: int=0,
                                 on_key_trail: bool=True,
                                 sep: str="-"
                                 ):
    """
    Recursively de-structure a JSON object and collect key-related information.

    Args:
        data (dict): The input JSON object to be de-structured.
        n_nestings (int): The number of nestings in the JSON structure.
        on_key_trail (bool): Whether to include key trails.
        sep (str): The separator used in key trails.

    Returns:
        tuple: A tuple containing the de-structured information, including keys, values, key trails, and nesting level.
    """
```

### Indirect-recursion-destructuring

```python
def indirect_recursive_json_destructure(data: dict, 
                                        on_key_trail: bool=True,
                                        sep: str="-"
                                        ):
    """
    Recursively de-structure a JSON object using an alternative approach.

    Args:
        data (dict): The input JSON object to be de-structured.
        on_key_trail (bool): Whether to include key trails.
        sep (str): The separator used in key trails.

    Returns:
        tuple: A tuple containing the de-structured information, including keys, values, key trails, and nesting level.
    """
```

## Usage

You can use these functions to de-structure JSON data and retrieve structured information about the keys, values, and nesting. Below is an example of how to use these functions:

```python
# Example usage of direct_recursive_destructure
only_keys, keys_with_their_values, trailed_keys, n_nestings = direct_recursive_destructure(json_obj)

# Example usage of indirect_recursive_json_destructure
only_keys, keys_with_its_values, trailed_keys, only_pairs, max_level, steps = indirect_recursive_json_destructure(json_obj)
```

## Contributing

We welcome contributions from the open-source community. If you'd like to contribute to this project, please follow our contributing guidelines.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
