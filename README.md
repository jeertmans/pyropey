# PyRopey

[![CI Build Status][github-ci-img]][github-ci]
[![Latest Release][pypi-version-badge]][pypi-version-url]
[![Python version][pypi-python-version-badge]][pypi-version-url]
[![Documentation][docs-rtd-img]][docs-rtd-url]

Python bindings for Rust's [Ropey](https://github.com/cessen/ropey) library.

From Ropey's repository: *Ropey is a utf8 text rope for Rust, designed to be the backing text-buffer for applications such as text editors. Ropey is fast, robust, and can handle huge texts and memory-incoherent edits with ease.*

PyRopey aims to provide the performance and accessible interface of Rope into Python's world.

## Installing

`PyRopey` is available in any platform and can be installed with `pip`:
```
pip install ropey
```

*Note: PyRopey is currently in pre-release status and major changes are to be expected*.

## Example Usage

Adapted from Ropey's example.

```python
from ropey import Rope

# Load a text file.
let text = Rope.from_file("my_great_book.txt")

# Print the 516th line (zero-indexed).
print(text.line(515))  # Not implemented yet

# Get the start/end char indices of the line.
let start_idx = text.line_to_char(515)  # Not implemented yet
let end_idx = text.line_to_char(516)

# Remove the line...
text.remove(slice(start_idx, end_idx))

# ...and replace it with something better.
text.insert(start_idx, "The flowers are... so... dunno.\n")

# Print the changes, along with the previous few lines for context.
let start_idx = text.line_to_char(511)
let end_idx = text.line_to_char(516)
print(text.slice(slice(start_idx, end_idx)))  # Not implemented yet

# Write the file back out to disk.
text.write_to_file("my_great_book.txt")
```

PyRopey's philosophy is to provide an API that is as close as possible to the original methods in Ropey. This is why we recommend using their [documentation](https://docs.rs/ropey/latest/ropey/index.html) for more details.

## Contributing

Contributions are more than welcome! Here are a few objectives:

- [ ] Implement (almost) every methods from `ropey::Rope`
- [ ] Write Python tests for every method
- [ ] Write stubs for every method
- [ ] Document every method
- [ ] Create docs, hosted on ReadTheDocs
- [ ] Build automated benchmarks to compared `ropey` with builtin alternatives

[pypi-version-badge]: https://img.shields.io/pypi/v/ropey?label=Ropey
[pypi-version-url]: https://pypi.org/project/ropey/
[pypi-python-version-badge]: https://img.shields.io/pypi/pyversions/ropey
[github-ci-img]: https://github.com/jeertmans/pyropey/actions/workflows/CI.yml/badge.svg
[github-ci]: https://github.com/jeertmans/pyropey/actions?query=workflow%3Aci
[docs-rtd-url]: https://pyropey.readthedocs.io/en/latest/?badge=latest
[docs-rtd-img]: https://readthedocs.org/projects/pyropey/badge/?version=latest
