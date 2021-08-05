# runnn

A utility that executes applications with large amounts of arguments using yaml

## Features

- define yaml syntax for features
  - hyperparameter key for running hyperparameter search

- runnn.py arguments:
  - run
  - generate run command and print
  - if hyperparameter exist will run or print all commands
  - hyperparameter support: lists of argument, range as float/int, count (number of random draws)

- create setup.py with `runnn` command and and pip package
