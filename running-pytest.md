# Running pytest

Here are some ways of running pytest

```bash
# Running all tests
python -m pytest -s

# Running a specific collection of tests
python -m pytest -s tests/some_test.py

# Running a single test function
python -m pytest -s tests/repository_manager_test.py -k test_repository_download

# Running tests with an environment variable
GITLAB_ACCESS_TOKEN=<TOKEN> python -m pytest -s

## Or by setting in once
export GITLAB_ACCESS_TOKEN=<TOKEN>
export SOME_VAR=something_needed

python -m pytest -s

## Or setting all variables from a file
source `cat .env`
```
