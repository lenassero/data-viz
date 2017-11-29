#!/usr/bin/env python
# -*- coding: utf-8 -*- 

__author__ = "Nasser Benabderrazik"

import matplotlib.pyplot as plt

def subplot_value_counts(data, variable, width=0.8):
    """ Plot value counts for one categorical variable.

    Parameters
    ----------

	data: DataFrame
		DataFrame with categorical variables
    variable: string
    	Name of the categorical variable
    width: int, optional
    	Width of the bars

    Returns
    -------

    barplot: single bar plot
    """

    # Value counts (limit to 30 categories)
    counts = data[variable].value_counts()[:30]

    # Number of categories 
    n_categories = len(counts)

    # Categories
    categories = list(counts.index)

    # Plot the bars 
    barplot = plt.bar(height=counts, left=range(n_categories), 
    	              color="green", width=0.8)

    # Change the color of the Missing Values bar 
    if "Missing values" in categories:
        barplot[categories.index("Missing values")].set_color("r")

    # Add the categories as the x labels 
    ticks = [sum(x) for x in zip(range(n_categories), [width/2] * n_categories)]
    plt.xticks(ticks, categories, rotation=80)

    # Add a title and adjust the distance to the figure
    plt.title("'{}' category counts".format(variable), fontsize=14, y=1.02)

    return barplot


def plot_value_counts(data, variables):
    """ Plot value counts of the different categorical variables.

    Parameters
    ----------

	data: DataFrame
		DataFrame with categorical variables
    variable: list
    	Names of the categorical variables
    width: int, optional
    	Width of the bars
    """ 

    # Replace NaN values to be able to show them as a category
    data = data.fillna("Missing values")

    # Number of categorical variables specified
    n_variables = len(variables)

    if n_variables == 1:
    	subplot_value_counts(data, variables[0])
    else:
	    # Adjust the figure height to the number of variables to plot
	    plt.figure(figsize=(14, 6 * (n_variables//2)))

	    # Two subplots per row
	    if n_variables % 2 == 0:
	    	nrows = n_variables / 2
	    else:
	    	nrows = (n_variables+1) / 2

	    for i in range(n_variables):
	    	# Two subplots per row
	        plt.subplot(nrows, 2, i+1)
	        subplot_value_counts(data, variables[i])

	    # Adjust the spacing between subplots
	    plt.subplots_adjust(hspace=1)

	    # Show the figure containing the subplots
	    plt.show()