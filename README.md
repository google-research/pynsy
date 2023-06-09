# Pynsy: Python Analysis Framework

Pynsy (pronounced "pin-sy") is a framework for writing heavyweight dynamic
analyses for Python programs.

Pynsy instruments Python bytecode of a target application on-the-fly and
provides a hook to log or inspect each Python bytecode being executed along with
dynamic information about the operands involved in the bytecode. In the
distribution you will find several analyses.

*This is not an officially supported Google product.*

## Installation

Run the following command to install Pynsy.

```bash
pip3 install -e .
```

## Running a custom dynamic analysis

Use the following command to run a custom analysis defined in `config.json`.

```bash
python3 -m pynsy.main config.json <module> <arguments...>
```

For example, to check for expensive list membership operations (`x in L` where
`L` is a long list), we can run the following command:

```bash
python3 -m pynsy.main config.json demos.key_in_list
python3 -m pynsy.main config.json demos.mnist
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
[analyses/shape_logger.py](pynsy/analyses/shape_logger.py).

An analysis should define the following functions:

```python
def abstraction(obj):
  # returns a tuple of a bool (indicating whether the abstraction should track the logical address of the object) and
  # a finite abstraction of the object.

def process_event(record):
  # process each event as they are being generated

def process_termination():
  # process the list of events generated at the end of the execution
```

Typically, analyses process only specific Python instruction types (e.g.
function calls, or loads and stores) and ignore others.

