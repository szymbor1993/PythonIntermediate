# Dividend Tool

* [Overview](#overview)
  + [Purpose](#purpose)
  + [Simplified example](#simplified-example)
  + [However, very important thing...](#however-very-important-thing)
* [Task](#task)
  + [Project's skeleton](#projects-skeleton)
  + [Main task](#main-task)
  + [Algorithm](#algorithm)
  + [Hints](#hints)
* [Usage](#usage)
  + [Installation](#installation)
  + [Program](#program)
  + [Testing](#testing)

## Overview
### Purpose
* If you have shares in a foreign company and you acquire dividends, you need to 
know the tax rates both in foreign country and PL
* According to PL law, if foreign tax rate is lower than PL one, you need to pay 
the difference in PLN

### Simplified example
* One has earned 100$ of dividends in the previous year
* The tax rate in USA for dividends is 15%, so he/she receives 85 $
* However, in PL tax rate for dividends is 19%
* So he/she „owes” 4% of it to PL => need to pay 4 $ converted to PLN

### However, very important thing...
* One needs to convert every dividend payment separately, as currency rates may
differ from day to day
* The rule is that one needs to take exchange rate from the 
**previous working day**
* Example, if he/she received dividend on monday, May 1st, the valid exchange 
rate will be from friday, April 28th.

## Task
### Project's skeleton
Here you have a skeleton for this tool:
* input / output handling (InputManager, pydantic models for validation)
* REST API client with logic needed to get previous working day exchange rates
* utils module with several datetime functions
* constants.py file
* main.py as an entry point

### Main task
Your task is to finish this tool, according to details specified in **Overview**
section.

Additionally:
* input should be a JSON in format as in _schemas/input_schema.json_
* output should be available in 2 formats (both printed to the console):
  * JSON in format as in _schemas/output_schema.json_
  * text - please look at _models/output_data.py_
and function \_\_str\_\_

### Algorithm
Here's the exemplary algorithm you can use:
* for each dividend payment:
  * get exchange rates (foreign currency to PLN) from the previous working day
  * calculate foreign tax and polish tax => in result, the difference between 
  them
  * if it is negative, return 0
  * convert it to PLN
  * Sum up calculated PLN values
  * Round it to 2nd decimal place

### Hints
* you can use all knowledge from this workshop, as this project (skeleton) was 
built on python 3.11 
* As an argument to the program provide path to JSON file

## Usage

### Installation
This project requires python 3.10 and two libraries: _requests_ and _pydantic_.\
In order to prepare your environment use _requirements.txt_ file. Run this
command in the main folder of the project:

```bash
pip3 install -r requirements.txt
```

### Program
In order to run this program, type in the main folder of this project:
```bash
python3 main.py <additional_parameters>
```

### Testing
Due to the fact, that program calls REST API of NBP, in order to properly test
your code written in this exercise, I prepared some tests with InputManager and 
RestClient objects mocked. Tests definition is located in 
_tests/test_cases/main.json_ file.

In order to run them, one needs to create unittests configuration. As a module 
name provide _tests.test_main_. You also need to set working directory to 
_main_exercise_ (provide full path).

Alternatively, type the following command in 
_main_exercise_ directory:
```bash
python3 -m unittest tests.test_main
```
