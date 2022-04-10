def sound_lookup(keys_df, key):
    """A function that returns information for a class label from a dataframe

    Parameters
    ----------
    keys_df: dataframe
        A dataframe containing the class labels and other information.
    key: str
        A string that represents a class label in the data set.
        
    Returns
    -------
    common_name: str
        The common name of the entity identified by the class label.
    scientific_name: str
        The scientific name of the entity indentified in the class label"""
    
    common_name = keys_df["common_name"][keys_df.primary_label == key].item()
    scientific_name = keys_df["scientific_name"][keys_df.primary_label == key].item()
    
    return common_name, scientific_name

def sound_idn(keys_df, key):
    """A function that returns a numeric id for a class label from a dataframe

    Parameters
    ----------
    keys_df: dataframe
        A dataframe containing the class labels and other information.
    key: str
        A string that represents a class label in the data set.
        
    Returns
    -------
    int
        The dataframe index of the entity identified by the class label."""    
    

    return keys_df.index[keys_df['primary_label'] == key].tolist()[0]

def sound_common(keys_df, idn):
    """A function that returns the common name for an index from a dataframe

    Parameters
    ----------
    keys_df: dataframe
        A dataframe containing the class labels and other information.
    idn: int
        The dataframe index value to look up.
        
    Returns
    -------
    str
        The common name of the entity identified by the index value."""    


    return keys_df.loc[idn,"common_name"]

def sound_label(keys_df, idn):
    """A function that returns the class label for an index from a dataframe

    Parameters
    ----------
    keys_df: dataframe
        A dataframe containing the class labels and other information.
    idn: int
        The dataframe index value to look up.
        
    Returns
    -------
    str
        The class label of the entity identified by the index value."""    
    #key = INV_BIRD_CODE[idn]
    #return bird_key["common_name"][bird_key.primary_label == key].item()
    return keys_df.loc[idn,"primary_label"]




