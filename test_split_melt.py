import pandas as pd
from split_melt import split_melt


def test_split_melt_rows():
    test_dict = {
        "movie_title": {
            0: "The Adventures of Ichabod and Mr. Toad",
            1: "Lady and the Tramp",
            2: "The Aristocats",
            3: "The Jungle Book",
            4: "Snow White and the Seven Dwarfs",
            5: "Pinocchio",
            6: "Fantasia",
            7: "Dumbo",
        },
        "release_date": {
            0: "October 5, 1949",
            1: "June 22, 1955",
            2: "December 24, 1970",
            3: "October 18, 1967",
            4: "December 21, 1937",
            5: "February 7, 1940",
            6: "November 13, 1940",
            7: "October 23, 1941",
        },
        "hero": {
            0: "Mr. Toad and Ichabod Crane",
            1: "Lady and Tramp",
            2: "Thomas and Duchess",
            3: "Mowgli",
            4: "Snow White",
            5: "Pinocchio",
            6: None,
            7: "Dumbo",
        },
        "villian": {
            0: "Mr. Winkie and The Headless Horseman",
            1: "Si and Am",
            2: "Edgar Balthazar",
            3: "Kaa and Shere Khan",
            4: "Evil Queen",
            5: "Stromboli",
            6: "Chernabog",
            7: "Ringmaster",
        },
        "song": {
            0: "The Merrily Song",
            1: "Bella Notte",
            2: "Ev'rybody Wants to Be a Cat",
            3: "The Bare Necessities\n",
            4: "Some Day My Prince Will Come",
            5: "When You Wish upon a Star",
            6: None,
            7: "Baby Mine",
        },
    }

    test_df = pd.DataFrame.from_dict(test_dict)

    assert (
        split_melt(
            test_df,
            ["movie_title", "release_date", "song"],
            ["hero", "villian"],
            " and ",
            "character_type",
            "character_name",
        ).shape[0]
        == 21
    ), "Number of rows returned is incorrect"


def test_split_melt_cols():

    test_dict = {
        "movie_title": {
            0: "The Adventures of Ichabod and Mr. Toad",
            1: "Lady and the Tramp",
            2: "The Aristocats",
            3: "The Jungle Book",
            4: "Snow White and the Seven Dwarfs",
            5: "Pinocchio",
            6: "Fantasia",
            7: "Dumbo",
        },
        "release_date": {
            0: "October 5, 1949",
            1: "June 22, 1955",
            2: "December 24, 1970",
            3: "October 18, 1967",
            4: "December 21, 1937",
            5: "February 7, 1940",
            6: "November 13, 1940",
            7: "October 23, 1941",
        },
        "hero": {
            0: "Mr. Toad and Ichabod Crane",
            1: "Lady and Tramp",
            2: "Thomas and Duchess",
            3: "Mowgli",
            4: "Snow White",
            5: "Pinocchio",
            6: None,
            7: "Dumbo",
        },
        "villian": {
            0: "Mr. Winkie and The Headless Horseman",
            1: "Si and Am",
            2: "Edgar Balthazar",
            3: "Kaa and Shere Khan",
            4: "Evil Queen",
            5: "Stromboli",
            6: "Chernabog",
            7: "Ringmaster",
        },
        "song": {
            0: "The Merrily Song",
            1: "Bella Notte",
            2: "Ev'rybody Wants to Be a Cat",
            3: "The Bare Necessities\n",
            4: "Some Day My Prince Will Come",
            5: "When You Wish upon a Star",
            6: None,
            7: "Baby Mine",
        },
    }

    test_df = pd.DataFrame.from_dict(test_dict)

    assert (
        split_melt(
            test_df,
            ["movie_title", "release_date", "song"],
            ["hero", "villian"],
            " and ",
            "character_type",
            "character_name",
        ).shape[1]
        == 5
    ), "Number of columns returned is incorrect"


def test_split_melt_var_name():

    test_dict = {
        "movie_title": {
            0: "The Adventures of Ichabod and Mr. Toad",
            1: "Lady and the Tramp",
            2: "The Aristocats",
            3: "The Jungle Book",
            4: "Snow White and the Seven Dwarfs",
            5: "Pinocchio",
            6: "Fantasia",
            7: "Dumbo",
        },
        "release_date": {
            0: "October 5, 1949",
            1: "June 22, 1955",
            2: "December 24, 1970",
            3: "October 18, 1967",
            4: "December 21, 1937",
            5: "February 7, 1940",
            6: "November 13, 1940",
            7: "October 23, 1941",
        },
        "hero": {
            0: "Mr. Toad and Ichabod Crane",
            1: "Lady and Tramp",
            2: "Thomas and Duchess",
            3: "Mowgli",
            4: "Snow White",
            5: "Pinocchio",
            6: None,
            7: "Dumbo",
        },
        "villian": {
            0: "Mr. Winkie and The Headless Horseman",
            1: "Si and Am",
            2: "Edgar Balthazar",
            3: "Kaa and Shere Khan",
            4: "Evil Queen",
            5: "Stromboli",
            6: "Chernabog",
            7: "Ringmaster",
        },
        "song": {
            0: "The Merrily Song",
            1: "Bella Notte",
            2: "Ev'rybody Wants to Be a Cat",
            3: "The Bare Necessities\n",
            4: "Some Day My Prince Will Come",
            5: "When You Wish upon a Star",
            6: None,
            7: "Baby Mine",
        },
    }

    test_df = pd.DataFrame.from_dict(test_dict)

    assert "character_type" in split_melt(
        test_df,
        ["movie_title", "release_date", "song"],
        ["hero", "villian"],
        " and ",
        "character_type",
        "character_name",
    ), "variable column name is incorrect or missing"


def test_split_melt_val_name():

    test_dict = {
        "movie_title": {
            0: "The Adventures of Ichabod and Mr. Toad",
            1: "Lady and the Tramp",
            2: "The Aristocats",
            3: "The Jungle Book",
            4: "Snow White and the Seven Dwarfs",
            5: "Pinocchio",
            6: "Fantasia",
            7: "Dumbo",
        },
        "release_date": {
            0: "October 5, 1949",
            1: "June 22, 1955",
            2: "December 24, 1970",
            3: "October 18, 1967",
            4: "December 21, 1937",
            5: "February 7, 1940",
            6: "November 13, 1940",
            7: "October 23, 1941",
        },
        "hero": {
            0: "Mr. Toad and Ichabod Crane",
            1: "Lady and Tramp",
            2: "Thomas and Duchess",
            3: "Mowgli",
            4: "Snow White",
            5: "Pinocchio",
            6: None,
            7: "Dumbo",
        },
        "villian": {
            0: "Mr. Winkie and The Headless Horseman",
            1: "Si and Am",
            2: "Edgar Balthazar",
            3: "Kaa and Shere Khan",
            4: "Evil Queen",
            5: "Stromboli",
            6: "Chernabog",
            7: "Ringmaster",
        },
        "song": {
            0: "The Merrily Song",
            1: "Bella Notte",
            2: "Ev'rybody Wants to Be a Cat",
            3: "The Bare Necessities\n",
            4: "Some Day My Prince Will Come",
            5: "When You Wish upon a Star",
            6: None,
            7: "Baby Mine",
        },
    }

    test_df = pd.DataFrame.from_dict(test_dict)

    assert "character_name" in split_melt(
        test_df,
        ["movie_title", "release_date", "song"],
        ["hero", "villian"],
        " and ",
        "character_type",
        "character_name",
    ), "value column name is incorrect or missing"


def test_split_melt_df():

    test_dict = {
        "movie_title": {
            0: "The Adventures of Ichabod and Mr. Toad",
            1: "Lady and the Tramp",
            2: "The Aristocats",
            3: "The Jungle Book",
            4: "Snow White and the Seven Dwarfs",
            5: "Pinocchio",
            6: "Fantasia",
            7: "Dumbo",
        },
        "release_date": {
            0: "October 5, 1949",
            1: "June 22, 1955",
            2: "December 24, 1970",
            3: "October 18, 1967",
            4: "December 21, 1937",
            5: "February 7, 1940",
            6: "November 13, 1940",
            7: "October 23, 1941",
        },
        "hero": {
            0: "Mr. Toad and Ichabod Crane",
            1: "Lady and Tramp",
            2: "Thomas and Duchess",
            3: "Mowgli",
            4: "Snow White",
            5: "Pinocchio",
            6: None,
            7: "Dumbo",
        },
        "villian": {
            0: "Mr. Winkie and The Headless Horseman",
            1: "Si and Am",
            2: "Edgar Balthazar",
            3: "Kaa and Shere Khan",
            4: "Evil Queen",
            5: "Stromboli",
            6: "Chernabog",
            7: "Ringmaster",
        },
        "song": {
            0: "The Merrily Song",
            1: "Bella Notte",
            2: "Ev'rybody Wants to Be a Cat",
            3: "The Bare Necessities\n",
            4: "Some Day My Prince Will Come",
            5: "When You Wish upon a Star",
            6: None,
            7: "Baby Mine",
        },
    }

    test_df = pd.DataFrame.from_dict(test_dict)

    assert isinstance(
        split_melt(
            test_df,
            ["movie_title", "release_date", "song"],
            ["hero", "villian"],
            " and ",
            "character_type",
            "character_name",
        ),
        pd.DataFrame,
    ), "Output is not a dataframe"
