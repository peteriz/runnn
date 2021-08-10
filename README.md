# RUNNN

A handy tool for launching python scripts with large amounts of arguments using a more readable yaml file.

## Install

```bash
git clone https://github.com/peteriz/runnn.git
cd runnn
pip install .
```

or 

```bash
pip install git+https://github.com/peteriz/runnn.git
```

## Usage

### Just run

```bash
runnn script.py arg.yaml
```

### Just print the command (don't run)

```bash
runnn script.py arg.yaml --print
```

## Argument definition in yaml file

```yaml
app:
  # prefix to amend
  cmd_prefix: python
  # add positional arguments
  positional: pos_arg1 pos_arg2

# first argument group
arguments_group1:
  # int arg
  param1: 1
  # float arg
  param2: 2.71
  # single char argument (added as -x)
  x: 37

# second argument group
arguments_group2:
  # string argument
  param3: param_num_3
  # long string argument
  param4: 'this is a long string'
  # bool argument
  param5: true
  # list argument
  param6: [1,2,3]
```

running the above yaml with `runnn` and a sample script will result in the following command:

```
python script.py pos_arg1 pos_arg2 --param1=1 --param2=2.71 -x=37 \
    --param3=param_num_3 --param4="this is a long string" --param5=True --param6=[1,2,3]
```

## Upcoming Features

- [ ] Define hyperparameter key in yaml for generating a list of commands for hyperparameter search
- [ ] Add support for multi-processing hyperparameter runs in parallel with progress bar

- `runnn.py` arguments:

  - [X] run
  - [X] generate run command and print
  - [ ] if hyperparameter exist will run or print all commands
  - [ ] hyperparameter support: lists of argument, range as float/int, count (number of random draws)

- [X] Create setup.py with `runnn` command and and pip package
