# Pynxy (Pronounced as pinxy): A Python Analysis framework 
This sets up a strategy to instrument Python bytecode operations based on calculations of the relevant portion of the stack read or updated by each operation, without any specific logic for different operations.

## Running a custom dynamic analysis defined in a module called `app_module_name` as the main method as `main_method_name`
Run 

`python3 run_instrumented.py app_module_name.main_method_name analysis_module_name.abstraction [list of arguments passed as sys.argv[2:]]`

For example, to run a shape tracing analysis, run:

`python3 run_instrumented.py demos.mnist.init_fun log_shapes_of_tensors.abstraction`
`