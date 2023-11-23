""" main.py

"""
# ----------------------------------------------------------------------
# IMPORTANT: Do not change these import statements
import pandas as pd

# Try to import lec_utils (only required by test functions)
try:
    from webinars import lec_utils as utils
except ImportError:
    print('The module lec_utils was not found. This module is only required by aux/test functions')


# ---------------------------------------------------------------------


def smart_concat(ser1, ser2):
    """ This function will combine `ser1` and `ser2` according to the following
    criteria:

    1. If the indexes of `ser1` and `ser2` have elements in common, this
    function will return a data frame including including all the observations
    in either `ser1` and `ser2`. The columns of this data frame will be <ser1 name> and
    <ser2 name> and the index will not include repeated elements.

    2. Otherwise, this function will return a series including all
    observations from both `ser1` and `ser2`. The name of this new series will
    be <ser1 name>_<ser2 name> and the index will not include any repeated
    elements.


    Parameters
    ----------
    ser1, ser2 : series
        Any two series. The name attribute must not be empty and the index
        of each series must not include repeated labels.

    Returns
    -------
    series, data frame:

        Either a series or a data frame. If the indexes of `ser1` and `ser2`
        have elements in common, returns a data frame containing the "outer
        join" of ser1 and ser2. Otherwise, returns a series containing all
        elements from ser1 and ser2 (in any order)


    Example
    -------

    Example 1:

        ser1:
            idx
            0     0.4
            1     0.0
            2    10.0
            3     1.5
            Name: ser1, dtype: float64

        ser2:
            idx
            3   -99.0
            4     0.2
            5    -9.5
            Name: ser2, dtype: float64

        smart_concat(ser1, ser2) -->

                 ser1  ser2
            idx
            0     0.4   NaN
            1     0.0   NaN
            2    10.0   NaN
            3     1.5 -99.0
            4     NaN   0.2
            5     NaN  -9.5

    Example 2:

        ser1:
            idx
            0     0.4
            1     0.0
            2    10.0
            Name: ser1, dtype: float64
        ser2:
            idx
            3   -99.0
            4     0.2
            5    -9.5
            Name: ser2, dtype: float64

        smart_concat(ser1, ser2) -->

            idx
            0     0.4
            1     0.0
            2    10.0
            3     1.5
            4     0.2
            5    -9.5
            Name: ser1_ser2, dtype: float64

    """
    # <COMPLETE THIS PART>
    common = [x for x in ser2.index if x in set(ser1.index)]
    if len(common) > 0:
        res = pd.concat([ser1,ser2],axis=1)
    else:
        res = pd.concat([ser1,ser2])
        res.name = f"{ser1.name}_{ser2.name}"
    return res


# ----------------------------------------------------------------------------
#  This test function will not be marked.
# ----------------------------------------------------------------------------
def _mk_test_ser(common_idx=True):
    """ Creates the testing series:

    Parameters
    ----------
    common_idx : bool
        If True, the following two series will be created:

            ser1:
                idx
                0     0.4
                1     0.0
                2    10.0
                3     1.5
                Name: ser1, dtype: float64
            ser2:
                idx
                3   -99.0
                4     0.2
                5    -9.5
                Name: ser2, dtype: float64

        Otherwise, create the following two series

            ser1:
                idx
                0     0.4
                1     0.0
                2    10.0
                Name: ser1, dtype: float64
            ser2:
                idx
                3   -99.0
                4     0.2
                5    -9.5
                Name: ser2, dtype: float64



    """
    ser1_cnts = """
      idx ,   ser1
        0 ,    0.4
        1 ,    0.0
        2 ,   10.0
        3 ,    1.5
    """
    ser2_cnts = """
      idx ,  ser2
        3 , -99.0
        4 ,   0.2
        5 ,  -9.5
    """
    ser1 = utils.csv_to_df(ser1_cnts, index_col='idx').loc[:, 'ser1']

    ser2 = utils.csv_to_df(ser2_cnts, index_col='idx').loc[:, 'ser2']

    if common_idx is False:
        cond = ser2.index.isin(ser1.index)
        ser2 = ser2.loc[~cond]

    return (ser1, ser2)


def _print_res():
    """ Auxiliary function to print the result of smart_concat
    Requires lec_utils module (imported as utils)
    """
    # --------------------------------------------------------
    #   Two series with a common index label
    # --------------------------------------------------------
    (ser1, ser2) = _mk_test_ser(common_idx=True)
    df = smart_concat(ser1, ser2)
    utils.pprint(df)

    # --------------------------------------------------------
    #   Two series without a common index label
    # --------------------------------------------------------
    (ser1, ser2) = _mk_test_ser(common_idx=False)
    ser = smart_concat(ser1, ser2)
    utils.pprint(ser)


if __name__ == "__main__":
    # Uncomment to use the _print_res function (requires lec_utils)
    _print_res()
    pass











