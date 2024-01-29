import pandas as pd


def currency_cleaner(data, cols_to_clean, currency_symbol="$", radix_char=","):
    """
    Converts string values in specified columns of a dataframe to float values.

    Parameters
    ----------
    data : pd.DataFrame
        The DataFrame containing the target columns

    cols_to_clean : list of str values
        The target columns containing the string \
values to convert to float values.

    currency_symbol : str, optional, {'$','£','€','¥'}
        The currency symbol used in the string values.
        (Default = '$' which represents dollar currencies)

    radix_char : str, optional, {',',' '}
        The symbol used to separate value periods in the string value.
        (Default is ',' used in USD currency)

    Returns
    -------
    clean_dataframe : pd.Dataframe
        The DataFrame containing the columns converted to float values

    Raises
    ------
    TypeError
        If argument passed to `data` is not of type pd.DataFrame.
        If argument passed to `cols_to_clean` is not a list.
        If argument passed to `currency_symbol` is not a string.
        If any element of `cols_to_clean` list is not a string.

    ValueError
        If empty list is passed to `cols_to_clean`.
        If value passed to `currency_symbol` is not in `currency_symbol_set`.


    KeyError
        If any element of `cols_to_clean` is not a \
column in the target DataFrame.


    Examples
    --------
    currency_cleaner(data,['unit_price','extended_price'],'€', ' ')
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Please pass a pd.DataFrame object to \
`data` parameter."
        )
    clean_dataframe = data.copy()
    original_column_order = clean_dataframe.columns.tolist()

    if not isinstance(cols_to_clean, list):
        raise TypeError("Please pass a list to `cols_to_clean`")

    if not cols_to_clean:
        raise ValueError(
            "List passed to `cols_to_clean` is empty. \
Please populate list with names of columns to clean."
        )

    if not isinstance(currency_symbol, str):
        raise TypeError("Please pass the currency symbol as a string")

    # Ensure that only a currency symbol can be removed
    currency_symbol_set = {"$", "£", "€", "¥"}
    if currency_symbol not in currency_symbol_set:
        raise ValueError(
            'The symbol passed to `curency_symbol` is not supported. \
Choose from "$","£","€" or "¥".'
        )

    # Ensure that only ' ' or ',' can be removed
    radix_char_set = {" ", ","}
    if radix_char not in radix_char_set:
        raise ValueError('Please choose between ","  or " " for `radix_char`')

    # Check that values passed are strings and are columns in target dataframe
    # Convert values in columns to float if true
    # Return list of incorrect values if false
    column_not_string = []
    missing_columns = []
    for column in cols_to_clean:
        if not isinstance(column, str):
            column_not_string.append(column)
        if column not in data:
            missing_columns.append(column)
        else:
            clean_dataframe = (
                clean_dataframe.assign(
                    clean_column=clean_dataframe[column]
                    .str.replace(currency_symbol, "", regex=True)
                    .str.replace(radix_char, "")
                    .astype(float)
                )
                .drop(columns=column)  # drop original column
                .rename(
                    columns={"clean_column": column}
                )  # rename new column to match original column
            )

    if column_not_string:
        raise TypeError(
            "The following items in the `cols_to_clean` list are not strings: "
            + str(column_not_string)
        )

    if missing_columns:
        raise KeyError(
            "The following columns are not part of the \
target dataframe:"+ str(missing_columns)
        )

    clean_dataframe = clean_dataframe.loc[
        :, original_column_order
    ]  # Re-order columns to match column order of original dataframe

    return clean_dataframe
