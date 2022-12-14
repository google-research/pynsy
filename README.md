# Pynsy (Pronounced as pinxy): A Python Analysis Framework 
This sets up a strategy to instrument Python bytecode operations based on calculations of the relevant portion of the stack read or updated by each operation, without any specific logic for different operations.

## Installing Pynsy

Run the following command in the python-analysis directory.

`pip3 install -r requirements.txt`

## Running a custom dynamic analysis defined in a module called `app_module_name` whose main method (or entry method) is `main_method_name`


`python3 run_instrumented.py analysis_module_name app_module_name  [list of arguments passed as sys.argv[2:]]`

For example, to collect shapes of various tensor objects, run:

`python3 run_instrumented.py analyses.load_store_apply demos.mnist `

## Interpreting results for post-processing

When we execute a program with Pynsy, it records information about every load, 
store, and application (e.g. application of a binary/unary operator or calling a 
method) instruction executed by the program in order. The information is stored 
as a dictionary which has some common keys and some instruction specific keys. 
Each dictionary is printed in a new line in JSON format.  One could save the 
sequence of records in a table, and use `panadas` or some data analytics 
framework for further analysis.

The common keys found in each record are the following

 * `module_name`: whose value gives the unique method id whose instruction has generated the log
 * `method_id`: whose value gives the unique method id whose instruction has generated the log
 * `instruction_id`: whose value gives the unique instruction within the method which generated the log
 * `lineno`: line number of the program such that compilation of the statement at the line number resulted in the instruction bytecode
 * `type`: type of the bytecode instruction
 * `execution_index`: the number of instructions executed so far during the execution of the program
 * `indentation`: the indentation of the instruction being executed.  This helps to capture the recursive organization of the instructions
 * `before`: whether the log appears before executing the instruction or not

The other instruction specific keys are:

 * `result`: whose value gives the result produced by the execution of an instruction
 * `operand`: the value of the operand if the instruction executed takes an operand as argument
 * `operand1`: the value of the first operand in the case of a binary instruction operating on two operands
 * `operand2`: the value of the second operand in the case of a binary instruction operating on two operands
 * `var_name`: name of the variable if the instruction accesses the value of the variable 
 * `attr_name`: name of the attribute of the object accessed 
 * `base`: the value of the base object in an instruction where a `base` object's value at `index` is accessed by the instruction
 * `index`: the value of the index object in an instruction where a `base` object's value at `index` is accessed by the instruction
 * `function`: the value of the function being executed
 * `function_name`: the name of the function being called
 * `args_list`: a list of arguments being passed to the function call
 * `frame`: the value of the activation frame containing a given variable name

## Writing a custom dynamic analysis

One can write a custom dynamic analysis for Python instructions of interest by creating a Pynsy analysis class of the form
[analyses/shape_logger.py](analyses/shape_logger.py). 

An analysis should override the following functions:

```
import config

# config.static_program_info contains the static bytecode information
# it maps module_name->method_id->instr_id->Bytecode

def abstraction(obj):
  # return a finite abstraction of the object

def process_event(record):
  # process each event as they are being generated

def process_termination(record_list):
  # process the list of events generated at the end of the execution
```
