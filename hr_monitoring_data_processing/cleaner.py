def filter_nondigits(data: list) -> list:
    """
    This function filters all strings from list that are not integers
    """


    """

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    new_list = []

    
    for item in data:
        x = item.strip()
        #if that item in the data is an integer, add it to the list
        if x.isdigit():
            new_list.append(int(x))
        else:
            continue
    return new_list



def filter_outliers(data: list) -> list:
    """
    This function filters the outliers from the list that are not in range of 30 - 250
    """
    hrt =[]
    for item in data:
        #checks if item is between 30 - 250, if so - add to list
        if item >30 and item < 250:
            hrt.append(item)
        else:
            continue
    return hrt    