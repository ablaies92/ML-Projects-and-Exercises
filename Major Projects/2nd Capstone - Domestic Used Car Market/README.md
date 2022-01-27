# 2nd Capstone - Can you model the US Used Car Market?

The objective of this project is to develop a predictive model that automates the domestic used car sales market appraisal and estimation/evaluation process. 

The main driving force behind the development of this model is to minimize laborious efforts that go into researching used car sales data (e.g. what can I get for a 2011 toyota camry SE?) by deploying a model built using historical data with the ability to consume new data (leveraging Bayesian principles – ideal, future state model). 

## Pipenv

The `Pipefile` has all the python dependencies and requirements you should need. So you can use [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/) is you want to create a seperate python enviornment for this project. 

To install pipenv see [here](https://pipenv-fork.readthedocs.io/en/latest/#install-pipenv-today).

To create the env and install the required libraries (once you have pipenv installed) you can just do:
```
pipenv install
```

Then to activate the env and launch jupyter from this env you can do something like the below two commands:
```
pipenv shell
jupyter lab
```
