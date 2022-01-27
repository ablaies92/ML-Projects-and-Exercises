# 3rd Capstone -  To develop a generalized, predictive model that can identify and differentiate between different types of fish species that share similar characteristics

The ideal model has a myriad of potential use cases that include the following:
1.	High volume fish processing plant: ability to dynamically identify and separate different (in tandem with robotics) fish species to optimize the handling and processing of fish 
2.	Use for identification of fish species for environmental conservation efforts: this would require augmentation of the existing model to account for different environmental contexts
3.	Potentially leverage existing model to develop a more sophisticated model that can accurately measure the dimensions (length and width) of the fish as well as the weight 

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
