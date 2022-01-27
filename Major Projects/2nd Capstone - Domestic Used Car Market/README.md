# 1st Capstone - Can Big Mountain Resort Raise their Daily Ticket Price?

This analysis includes various notebooks that break up the comprehensive Data Science project lifecycle (initial data discovery/loading (data wrangling), exploratory data analysis, preprocessing and modelling)

The purpose of this data science project is to come up with a pricing model for ski resort tickets in our market segment. Big Mountain suspects it may not be maximizing its returns, relative to its position in the market. It also does not have a strong sense of what facilities matter most to visitors, particularly which ones they're most likely to pay more for. This project aims to build a predictive model for ticket price based on a number of facilities, or properties, boasted by resorts (at the resorts). This model will be used to provide guidance for Big Mountain's pricing and future facility investment plans.

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
