#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    diff = [abs(x[0]-y[0]) for x,y in zip(predictions, net_worths)]

    final_len = int(0.9 * len(diff))

    import numpy as np

    list_ages = ages.tolist()
    list_net_worths = net_worths.tolist()

    while len(diff) > final_len:
        max_diff_index = diff.index(max(diff))
        # del ages[max_diff_index]
        # del net_worths[max_diff_index]
        # del diff[max_diff_index]
        list_ages.pop(max_diff_index)
        list_net_worths.pop(max_diff_index)
        diff.pop(max_diff_index)

    for i in range(len(diff)):
        cleaned_data.append((list_ages[i], list_net_worths[i], diff[i]))

    return cleaned_data

