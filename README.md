# Pynxy (Pronounced as pinxy): A Python Analysis framework 
This sets up a strategy to instrument Python bytecode operations based on calculations of the relevant portion of the stack read or updated by each operation, without any specific logic for different operations.

## Installing Pynxy

Run the following command in the python-analysis directory.

`pip3 install -r requirements.txt`

## Running a custom dynamic analysis defined in a module called `app_module_name` whose main method (or entry method) is `main_method_name`


`python3 run_instrumented.py analysis_module_name app_module_name.main_method_name  [list of arguments passed as sys.argv[2:]]`

For example, to collect shapes of various tensor objects, run:

`python3 run_instrumented.py analyses.shape_logger demos.mnist.init_fun `

## Interpreting results for post-processing

When we execute a program with Pynxy, it records information about every load, 
store, and application (e.g. application of a binary/unary operator or calling a 
method) instruction executed by the program in order. The information is stored 
as a dictionary which has some common keys and some instruction specific keys. 
Each dictionary is printed in a new line in JSON format.  One could save the 
sequence of records in a table, and use `panadas` or some data analytics 
framework for further analysis.

The common keys found in each record are the following

`method_id`: whose value gives the unique method id whose instruction has generated the log
`instruction_id`: whose value gives the unique instruction within the method which generated the log
`lineno`: line number of the program such that compilation of the statement at the line number resulted in the instruction bytecode
`type`: type of the bytecode instruction
`execution_index`: the number of instructions executed so far during the execution of the program
`indentation`: the indentation of the instruction being executed.  This helps to capture the recursive organization of the instructions

The other instruction specific keys are:

@todo


`
