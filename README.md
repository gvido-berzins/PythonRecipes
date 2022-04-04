# PythonRecipes

My personal Python "Recipe Book".

I have a summary and description for some scripts and I'm planning to do some
kind of search based on these two, for now it's just a bunch of scripts in a
repository.

## Documented scripts

### `transpose_list_to_column.py`

#### Summary

Turn a list of values into a column for Sheets API

### `os_pathlib_bench.py`

#### Summary

Testing the speed of pathlib and os doing path operations

#### Description

Simple test of concatinating and creating a directory

### `os_path_alternative.py`

#### Summary

pathlib Path object operations

#### Description

Showing the same operations that can be done with os module, instead using pathlib module

### `regex_sorting.py`

#### Summary

Sort a list of filenames, with using one or 3 keys

### `shallowing_deep.py`

#### Summary

Testing the difference between shallow and deep copy

### `global_scope.py`

#### Summary

Global variables

#### Description

Testing how global variables work within different scopes.

### `merge_dict.py`

#### Summary

Merge a dictionary in a different function to update the dictionary

### `ranger.py`

#### Summary

Filter a list of dates based on the date range

### `recursive_dict_lookup.py`

#### Summary

Recurse into a dictionary to safely get a value.

#### Description

From a given dictionary (or JSON), return a nested value using the varargs in the function parameters, otherwise return the default value.

### `import_docs.py`

#### Summary

Print documentation for all python modules in the current folder

#### Description

Simple script to get all docs from all modules

### `gen_dates.py`

#### Summary

Generate a list of dates between a certain range

### `yaml_anchors.py`

#### Summary

Read a YAML file which includes anchors

### `find_all_ips_regex.py`

#### Summary

Get all IP addresses from a string using regex.

### `duplicate_spreadsheet_to_folder_with_permissions.py`

#### Summary

Duplicate an existing spreadsheet to a folder with sharing

#### Description

Script creates a new spreadsheet based on a template and copies to to the specified folder (using it's Google Drive folder ID) and gives write permissions to a given domain.

### `docstring_readme.py`

#### Summary

Script for grabbing all module docstrings and creating a readme section

#### Description

I wanted to utilize the docstrings in my Python Recipe GitHub repo, thus this script.

### `schedule_fun.py`

#### Summary

Task scheduler to send a request to a Flask endpoint

#### Description

Using APScheduler schedule a task/function to execute on a specific interval, in this case, a function that sends POST requests to a local flask endpoint.

### `lambdas.py`

#### Summary

Testing the lambda function in filter and sorting

### `function_sig.py`

#### Summary

Print a function signature for give callable

### `record-screen.py`

#### Summary

Simple screen recorder script for a Linux based OS

#### Description

The command strings for Popen can be easily adjusted for Mac OS and Windows. This script can be used in a CI or anywhere else, I had an edge case where I couldn't use library for doing automated UI tests and needed a foolproof way to see what's going on.

### `f-strings.py`

#### Summary

Cheatsheet for f-strings (Just because I keep forgetting how to use them)

#### Description

Ways to use the f-string to perform more than interpolating variables, which includes substitution, raw printing, padding and formatting decimals.
