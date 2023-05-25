# Pynsy (Pronounced as pinsy): A Python Analysis Framework 
Pynsy is a framework for writing heavy-weight dynamic analyses for Python programs. 
Pynsy instruments Python bytecode of a target application on-the-fly and provides
a hook to log or inspect each Python bytecode being executed along with dynamic 
information about the operands involved in the bytecode.  
In the distribution you will find several analyses:

## Installing Pynsy

Tested on Python 3.9 and 3.10.  Does not work for Python 3.11.

Run the following command in the python-analysis directory.

`pip3 install -r requirements.txt`

## Running a custom dynamic analysis defined in a module called `app_module_name` whose main method (or entry method) is `main_method_name`


`python3 pynsy.py config.json app_module_name  [list of arguments passed as sys.argv[3:]]`

For example, to check if we are calling `x in L` where L is a long list, we can run the following command:

`python3 pynsy.py config.json demos.key_in_list` `

Another way to invoke Pynsy as a library, you can perform all the imports with Pynsy as follows, say in api_template.py:

```
from pynsy.instrumentation.module_loader import instrument_imports
with instrument_imports():
    import demos.key_in_list
```

One could then run the following command:
`python3 api_template.py config.json ignore` 



## Interpreting results for post-processing

When we execute a program with **Pynsy**, it records information about every load, 
store, and application (e.g. application of a binary/unary operator or ivocation of a 
method) instruction executed by the program in order. The information is stored 
as a dictionary.  One could save the sequence of records in a table, and use `pandas` or some data analytics 
framework for further analysis.

The keys found in each record are the following

 * `module_name`: whose value gives the unique method id whose instruction has generated the log
 * `method_id`: whose value gives the unique method id whose instruction has generated the log
 * `instruction_id`: whose value gives the unique instruction within the method which generated the log
 * `lineno`: line number of the program such that compilation of the statement at the line number resulted in the instruction bytecode
 * `type`: type of the bytecode instruction
 * `indentation`: the indentation of the instruction being executed.  This helps to capture the recursive organization of the instructions
 * `before`: whether the log appears before executing the instruction or not
 * `result_and_args`: whose value gives the result produced by the execution of an instruction
 * `name`: name of the variable or attribute, if the instruction accesses the value of the variable or the attribute 
 * `function_name`: the name of the function being called


## Writing a custom dynamic analysis

One can write a custom dynamic analysis for Python instructions of interest by creating a Pynsy analysis class of the form
[analyses/shape_logger.py](pynsy/analyses/shape_logger.py). 

An analysis should override the following functions:

```
def abstraction(obj):
  # returns a tuple of a Boolean (indicating whether the abstraction should track the logical address of the object) and 
  # a finite abstraction of the object.

def process_event(record):
  # process each event as they are being generated

def process_termination():
  # process the list of events generated at the end of the execution
```
