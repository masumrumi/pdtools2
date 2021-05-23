from pdtools2.reduce_memory.mem_reduce import missing_percentage, reduce_by_category_type, reduce_mem_usage, mem_usage, my_sum

import numpy as np
import pandas as pd


def test_reduce_mem_usage():
    assert isinstance(reduce_mem_usage(pd.DataFrame(
        {'age': [23, np.nan], 'name': ['rafi', 'Masum']})), pd.DataFrame)


def test_mem_usage():
    assert mem_usage(pd.DataFrame(
        {'age': [23, np.nan], 'name': ['rafi', 'Masum']})) == "0.00 MB"


def test_reduce_by_category_type():
    assert isinstance(reduce_by_category_type(pd.DataFrame(
        {'age': [23, np.nan], 'name': ['rafi', 'Masum']})), pd.DataFrame)


def test_missing_percentage():
    assert isinstance(missing_percentage(pd.DataFrame(
        {'age': [23, np.nan], 'name': ['rafi', 'Masum']})), pd.DataFrame)


def test_my_sum():
    assert my_sum(1, 3) == 4
