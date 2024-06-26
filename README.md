# Pynsy: Python Analysis Framework

Pynsy (pronounced "pin-sy") is a framework for writing heavyweight dynamic
analyses for Python programs.

Pynsy instruments Python bytecode of a target application on-the-fly and
provides a hook to log or inspect each Python bytecode being executed along with
dynamic information about the operands involved in the bytecode. In the
distribution you will find several analyses.

Currently, Pynsy supports Python 3.10 and earlier.

*This is not an officially supported Google product.*

## Installation

Run the following command to install Pynsy.

```bash
pip3 install -e .
```

## Running a custom dynamic analysis

Use the following command to run a custom analysis defined in `config.json`.

```bash
python3 -m pynsy.main --config <config> --module <module> -- <arguments...>
```

```bash
# Instrument expensive operations in Python, like a dynamic analysis linter.
#
# Example: catch expensive list membership (`x in list`) calls.
# These calls could be optimized using `set` or `dict`.
python3 -m pynsy.main --config configs/lint.json --module pynsy.demos.key_in_list
```

```bash
# Run tensor shape analysis on JAX MNIST.
python3 -m pynsy.main --config configs/tensor_shape_inference.json --module pynsy.demos.mnist
```

```bash
# Instrument a module that does flag-parsing.
# Use `--` to separate Pynsy flags from instrumented module flags.
python3 -m pynsy.main --config configs/lint.json --module pynsy.demos.flag_parsing \
  -- --string "Hello world" x y 10
```

## Processing analysis results

When Pynsy instruments a program, it records information about every load,
store, and application (e.g. application of a binary/unary operator or
invocation of a method) instruction executed by the program in order.

Program trace information is represented as a sequence of records. Saving
program traces as a table (e.g. CSV file) enables further analysis using
`pandas` or other data analytics frameworks.

Each record has the following keys:

-   `module_name`: the unique method id whose instruction has generated the log.
-   `method_id`: the unique method id whose instruction has generated the log.
-   `instruction_id`: the unique instruction within the method which generated
    the log.
-   `lineno`: line number of the program such that compilation of the statement
    at the line number resulted in the instruction bytecode.
-   `type`: type of the bytecode instruction.
-   `indentation`: the indentation of the instruction being executed. This helps
    to capture the recursive organization of the instructions.
-   `before`: whether the log appears before executing the instruction or not.
-   `result_and_args`: the result produced by the execution of an instruction.
-   `name`: the name of the variable or attribute, if the instruction accesses
    the value of the variable or the attribute.
-   `function_name`: the name of the function being called.

## Writing a custom dynamic analysis

One can write a custom dynamic analysis for Python instructions by creating a
Pynsy analysis class of the form
[analyses/tensor_shape_inference.py](pynsy/type_inference/tensor_shape_inference.py).

An analysis should define the following functions:

```python
def abstraction(obj: Any) -> tuple[bool, Any]:
  """Returns an abstract representation of the given object.

  Args:
    obj: The object to abstract.

  Returns:
    A tuple `(bool, Any)` where the first value indicates whether the
    abstraction should track the location of the object, and the second value
    is a finite abstraction of the object.
  """

def process_event(record):
  """Process each instrumentation event as it is generated."""

def process_termination():
  """Process the list of generated events at the end of analysis."""
```

Typically, analyses process only specific Python instruction types (e.g.
function calls, or loads and stores) and ignore others.

## Research papers

> **"Dynamic Inference of Likely Symbolic Tensor Shapes in Python Machine Learning Programs"**
>
> Koushik Sen, Daniel Zheng.
>
> In _Proceedings of the IEEE/ACM 46th International Conference on Software Engineering: Software Engineering in Practice (ICSE-SEIP 2024)_. ([PDF preprint](https://storage.googleapis.com/gweb-research2023-media/pubtools/pdf/f4c7d2ebfbf919c19bec9f58565c1a2f865f7e98.pdf))
