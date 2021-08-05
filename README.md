# RUNNN

A handy tool for launching python scripts with large amounts of arguments using a more readable yaml file.

## Install

```bash
git clone https://github.com/peteriz/runnn.git
cd runnn
pip install .
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

## Argument definition

```yaml
app:
  # prefix to amend
  cmd_prefix: python
  # add positional arguments
  positional: first_arg second_arg

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
  param4: 'this is a sentence'
  # bool argument
  param5: true
  # list argument
  param6: [1,2,3]
```

## Features

- define yaml syntax for features
  - hyperparameter key for running hyperparameter search

- runnn.py arguments:
  - run
  - generate run command and print
  - if hyperparameter exist will run or print all commands
  - hyperparameter support: lists of argument, range as float/int, count (number of random draws)

- create setup.py with `runnn` command and and pip package
