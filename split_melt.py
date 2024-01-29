import pandas as pd


def split_melt(
    data,
    id_columns,
    cols_to_split_melt,
    delimiter,
    variable_name="variable",
    val_name="value",
):
    """
    Splits string values in specified column/s, melts values resulting from \
split into the dataframe, any NaN values are removed.

    Parameters
    ----------
    data : df.DataFrame
        The dataframe containing the columns to split and melt.

    id_columns : list of strings
        The columns from the target dataframe to keep in the new dataframe \
that identify the melted values.

    cols_to_split_melt : list of strings
        The columns from the target dataframe containing values to split and \
melt into the new dataframe

    delimiter : string
        Character/s to split string on.

    Variable_name : string, optional
        Name of the variable column in the new dataframe.
        default = 'variable'

    val_name : string, optional
        Name of the value column in the new dataframe (contains the \
melted split values)
        default = 'value'

    Returns
    -------
    df_clean : pd.Dataframe
        The new melted dataframe.

    Raises
    ------
    TypeError
        If argument passed to `data` parameter is not a dataframe
        If argument passed to `id_columns` is not a list
        If argument passed to `cols_to_split_melt` is not a list.
        If argument passed to `delimiter` is not a string
        If argument passed to `variable_name` is not a string
        If argument passed to 'val_name' is not a string

    KeryError
        If any item in `id_columns` list is not a column in target dataframe
        If any item in `cols_to_split_melt` is not a column in target dataframe

    ValueError
        If `id_columns` is passed an empty list.
        If `cols_to_split_melt` is passed an empty list.

    Examples
    --------
    >>> melted_dataframe = split_melt(
       data,
       ["school_id"],
       ["teachers", "students"],
       variable_name="Teacher/Student",
       val_name="name",
   )

    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError(
            "Please pass a pd.DataFrame object to \
`data` parameter."
        )

    if not isinstance(id_columns, list):
        raise TypeError(
            "Please pass a list of strings to \
`id_columns` parameter"
        )

    if not id_columns:
        raise ValueError(
            "List passed to `id_columns` is empty. \
Please populate list with names of id_columns"
        )

    if not isinstance(cols_to_split_melt, list):
        raise TypeError(
            "Please pass a list of strings to \
`cols_to_split_melt`"
        )

    if not cols_to_split_melt:
        raise ValueError(
            "List passed to `cols_to_split_melt` is empty. \
Please populate list with names of columns to split and melt"
        )

    if not isinstance(delimiter, str):
        raise TypeError("`delimiter` must be a string!")

    if not isinstance(variable_name, str):
        raise TypeError("`variable_name` must be a string!")

    if not isinstance(val_name, str):
        raise TypeError("`val_name` must be a string!")

    # Check that values in `id_columns` are strings
    # And contained in target dataframe
    not_id_col = []
    id_col_not_string = []

    for id_column in id_columns:
        if not isinstance(id_column, str):
            id_col_not_string.append(id_column)
        if id_column not in data:
            not_id_col.append(id_column)

    if id_col_not_string:
        raise TypeError(
            "The following items in `id_columns` are not strings: "
            + str(id_col_not_string)
        )

    if not_id_col:
        raise KeyError(
            "The following column names passed to `id_columns` \
are not columns in the target dataframe: "
            + str(not_id_col)
        )

    # Create new base dataframe to concatenate to
    # Will be melted after concatenation
    df_to_melt = data.loc[:, id_columns]

    # Check that values in `cols_to_split_melt`
    # Are strings and contained in dataframe
    not_split_col = []
    split_col_not_string = []
    for column in cols_to_split_melt:
        if not isinstance(column, str):
            split_col_not_string.append(column)
        if column not in data:
            not_split_col.append(column)

        # Expand and concatenate only if column
        # Present in dataframe
        else:
            col_expanded = data.loc[:, column].str.split(delimiter, expand=True)
            for column_name in col_expanded.columns.tolist():
                col_expanded = col_expanded.rename(columns={column_name: column})
            df_to_melt = pd.concat([df_to_melt, col_expanded], axis=1)

    # Raise errors if items in `cols_to_split_melt`
    # Are not strings or not in target dataframe
    if split_col_not_string:
        raise TypeError(
            "The following items in `cols_to_split_melt` are not strings: "
            + str(split_col_not_string)
        )

    if not_split_col:
        raise KeyError(
            "The following column names passed to `cols_to_split_melt` are \
not columns in the target dataframe: "
            + str(not_split_col)
        )

    # Melt concatenated dataframe
    # Drop NaN values
    # Strip remaining values
    # Rename value column
    df_melted = df_to_melt.melt(
        id_vars=id_columns, var_name=variable_name, value_name="temp"
    )
    df_clean = df_melted[~df_melted["temp"].isna()].reset_index(drop=True)
    df_clean = df_clean.assign(temp=df_clean.loc[:, "temp"].str.strip()).rename(
        columns={"temp": val_name}
    )

    # Remove variable column if only one column split and melted
    if len(cols_to_split_melt) == 1:
        df_clean = df_clean.drop(columns=variable_name)

    return df_clean
