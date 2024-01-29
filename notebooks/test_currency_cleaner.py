import pandas as pd
import numpy as np
from currency_cleaner import currency_cleaner


def test_currency_cleaner_df():

    test_data_dict = {
        "movie_title": {
            0: "Snow White and the Seven Dwarfs",
            1: "Pinocchio",
            2: "Fantasia",
            3: "Song of the South",
            4: "Cinderella",
        },
        "release_date": {
            0: "Dec 21, 1937",
            1: "Feb 9, 1940",
            2: "Nov 13, 1940",
            3: "Nov 12, 1946",
            4: "Feb 15, 1950",
        },
        "genre": {
            0: "Musical",
            1: "Adventure",
            2: "Musical",
            3: "Adventure",
            4: "Drama",
        },
        "MPAA_rating": {0: "G", 1: "G", 2: "G", 3: "G", 4: "G"},
        "total_gross": {
            0: "$184,925,485",
            1: "$84,300,000",
            2: "$83,320,000",
            3: "$65,000,000",
            4: "$85,000,000",
        },
        "inflation_adjusted_gross": {
            0: "$5,228,953,251",
            1: "$2,188,229,052",
            2: "$2,187,090,808",
            3: "$1,078,510,579",
            4: "$920,608,730",
        },
    }

    test_df = pd.DataFrame.from_dict(test_data_dict)

    # Tests that output object is a dataframe
    assert (
        isinstance(
            currency_cleaner(test_df, ["total_gross", "inflation_adjusted_gross"]),
            pd.DataFrame,
        )

    ), "Output object is not a DataFrame"


def test_currency_cleaner_rows():

    test_data_dict = {
        "movie_title": {
            0: "Snow White and the Seven Dwarfs",
            1: "Pinocchio",
            2: "Fantasia",
            3: "Song of the South",
            4: "Cinderella",
        },
        "release_date": {
            0: "Dec 21, 1937",
            1: "Feb 9, 1940",
            2: "Nov 13, 1940",
            3: "Nov 12, 1946",
            4: "Feb 15, 1950",
        },
        "genre": {
            0: "Musical",
            1: "Adventure",
            2: "Musical",
            3: "Adventure",
            4: "Drama",
        },
        "MPAA_rating": {0: "G", 1: "G", 2: "G", 3: "G", 4: "G"},
        "total_gross": {
            0: "$184,925,485",
            1: "$84,300,000",
            2: "$83,320,000",
            3: "$65,000,000",
            4: "$85,000,000",
        },
        "inflation_adjusted_gross": {
            0: "$5,228,953,251",
            1: "$2,188,229,052",
            2: "$2,187,090,808",
            3: "$1,078,510,579",
            4: "$920,608,730",
        },
    }

    test_df = pd.DataFrame.from_dict(test_data_dict)

    # Tests that all rows were kept
    assert (
        currency_cleaner(test_df, ["total_gross", "inflation_adjusted_gross"]).shape[0]
        == 5
    ), "The new DataFrame does not have correct number of rows"


def test_currency_cleaner_col_num():

    test_data_dict = {
        "movie_title": {
            0: "Snow White and the Seven Dwarfs",
            1: "Pinocchio",
            2: "Fantasia",
            3: "Song of the South",
            4: "Cinderella",
        },
        "release_date": {
            0: "Dec 21, 1937",
            1: "Feb 9, 1940",
            2: "Nov 13, 1940",
            3: "Nov 12, 1946",
            4: "Feb 15, 1950",
        },
        "genre": {
            0: "Musical",
            1: "Adventure",
            2: "Musical",
            3: "Adventure",
            4: "Drama",
        },
        "MPAA_rating": {0: "G", 1: "G", 2: "G", 3: "G", 4: "G"},
        "total_gross": {
            0: "$184,925,485",
            1: "$84,300,000",
            2: "$83,320,000",
            3: "$65,000,000",
            4: "$85,000,000",
        },
        "inflation_adjusted_gross": {
            0: "$5,228,953,251",
            1: "$2,188,229,052",
            2: "$2,187,090,808",
            3: "$1,078,510,579",
            4: "$920,608,730",
        },
    }

    test_df = pd.DataFrame.from_dict(test_data_dict)

    # Tests all columns remain
    assert (
        currency_cleaner(test_df, ["total_gross", "inflation_adjusted_gross"]).shape[1]
        == 6
    ), "The new DataFrame does not have correct number of columns"


def test_currency_cleaner_col_name():

    test_data_dict = {
        "movie_title": {
            0: "Snow White and the Seven Dwarfs",
            1: "Pinocchio",
            2: "Fantasia",
            3: "Song of the South",
            4: "Cinderella",
        },
        "release_date": {
            0: "Dec 21, 1937",
            1: "Feb 9, 1940",
            2: "Nov 13, 1940",
            3: "Nov 12, 1946",
            4: "Feb 15, 1950",
        },
        "genre": {
            0: "Musical",
            1: "Adventure",
            2: "Musical",
            3: "Adventure",
            4: "Drama",
        },
        "MPAA_rating": {0: "G", 1: "G", 2: "G", 3: "G", 4: "G"},
        "total_gross": {
            0: "$184,925,485",
            1: "$84,300,000",
            2: "$83,320,000",
            3: "$65,000,000",
            4: "$85,000,000",
        },
        "inflation_adjusted_gross": {
            0: "$5,228,953,251",
            1: "$2,188,229,052",
            2: "$2,187,090,808",
            3: "$1,078,510,579",
            4: "$920,608,730",
        },
    }

    test_df = pd.DataFrame.from_dict(test_data_dict)

    # Tests that column names have remained the same
    assert set(
        currency_cleaner(test_df, ["total_gross", "inflation_adjusted_gross"]).columns
    ) == set(test_df.columns), "The column names in the new DataFrame \
have changed"


def test_currency_cleaner_col_ord():

    test_data_dict = {
        "movie_title": {
            0: "Snow White and the Seven Dwarfs",
            1: "Pinocchio",
            2: "Fantasia",
            3: "Song of the South",
            4: "Cinderella",
        },
        "release_date": {
            0: "Dec 21, 1937",
            1: "Feb 9, 1940",
            2: "Nov 13, 1940",
            3: "Nov 12, 1946",
            4: "Feb 15, 1950",
        },
        "genre": {
            0: "Musical",
            1: "Adventure",
            2: "Musical",
            3: "Adventure",
            4: "Drama",
        },
        "MPAA_rating": {0: "G", 1: "G", 2: "G", 3: "G", 4: "G"},
        "total_gross": {
            0: "$184,925,485",
            1: "$84,300,000",
            2: "$83,320,000",
            3: "$65,000,000",
            4: "$85,000,000",
        },
        "inflation_adjusted_gross": {
            0: "$5,228,953,251",
            1: "$2,188,229,052",
            2: "$2,187,090,808",
            3: "$1,078,510,579",
            4: "$920,608,730",
        },
    }

    test_df = pd.DataFrame.from_dict(test_data_dict)

    # Tests that columns remain in same order
    assert (
        currency_cleaner(
            test_df, ["total_gross", "inflation_adjusted_gross"]
        ).columns.tolist()
        == test_df.columns.tolist()
    ), "The columns in the new DataFrame have been re-ordered"


def test_currency_cleaner_col1_dtype():

    test_data_dict = {
        "movie_title": {
            0: "Snow White and the Seven Dwarfs",
            1: "Pinocchio",
            2: "Fantasia",
            3: "Song of the South",
            4: "Cinderella",
        },
        "release_date": {
            0: "Dec 21, 1937",
            1: "Feb 9, 1940",
            2: "Nov 13, 1940",
            3: "Nov 12, 1946",
            4: "Feb 15, 1950",
        },
        "genre": {
            0: "Musical",
            1: "Adventure",
            2: "Musical",
            3: "Adventure",
            4: "Drama",
        },
        "MPAA_rating": {0: "G", 1: "G", 2: "G", 3: "G", 4: "G"},
        "total_gross": {
            0: "$184,925,485",
            1: "$84,300,000",
            2: "$83,320,000",
            3: "$65,000,000",
            4: "$85,000,000",
        },
        "inflation_adjusted_gross": {
            0: "$5,228,953,251",
            1: "$2,188,229,052",
            2: "$2,187,090,808",
            3: "$1,078,510,579",
            4: "$920,608,730",
        },
    }

    test_df = pd.DataFrame.from_dict(test_data_dict)

    # Tests first column converted to float
    assert (
        currency_cleaner(test_df, ["total_gross", "inflation_adjusted_gross"])
        .loc[:, "total_gross"]
        .dtypes
        == np.float64
    ), "The target columns have not been converted to Dtype float"


def test_currency_cleaner_col1_type():

    test_data_dict = {
        "movie_title": {
            0: "Snow White and the Seven Dwarfs",
            1: "Pinocchio",
            2: "Fantasia",
            3: "Song of the South",
            4: "Cinderella",
        },
        "release_date": {
            0: "Dec 21, 1937",
            1: "Feb 9, 1940",
            2: "Nov 13, 1940",
            3: "Nov 12, 1946",
            4: "Feb 15, 1950",
        },
        "genre": {
            0: "Musical",
            1: "Adventure",
            2: "Musical",
            3: "Adventure",
            4: "Drama",
        },
        "MPAA_rating": {0: "G", 1: "G", 2: "G", 3: "G", 4: "G"},
        "total_gross": {
            0: "$184,925,485",
            1: "$84,300,000",
            2: "$83,320,000",
            3: "$65,000,000",
            4: "$85,000,000",
        },
        "inflation_adjusted_gross": {
            0: "$5,228,953,251",
            1: "$2,188,229,052",
            2: "$2,187,090,808",
            3: "$1,078,510,579",
            4: "$920,608,730",
        },
    }

    test_df = pd.DataFrame.from_dict(test_data_dict)

    # Tests that second column converted to float
    assert (
        currency_cleaner(test_df, ["total_gross", "inflation_adjusted_gross"])
        .loc[:, "inflation_adjusted_gross"]
        .dtypes
        == np.float64
    ), "The target columns have not been converted to Dtype float"
