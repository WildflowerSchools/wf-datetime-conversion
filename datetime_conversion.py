
import numpy as np
import pandas as pd

def to_pandas_timestamp_utc(datetime):
    try:
        return pd.to_datetime(datetime, unit = 's', utc=True)
    except:
        return pd.to_datetime(datetime, utc=True)

_to_pandas_timestamp_utc_vectorized = np.vectorize(to_pandas_timestamp_utc)

def to_pandas_timestamps_utc(datetimes):
    array = _to_pandas_timestamp_utc_vectorized(datetimes)
    if array.size == 1:
        return array.item()
    else:
        return array

def to_python_datetime_utc(datetime):
    return to_pandas_timestamp_utc(datetime).to_pydatetime()

_to_python_datetime_utc_vectorized = np.vectorize(to_python_datetime_utc)

def to_python_datetimes_utc(datetimes):
    array = _to_python_datetime_utc_vectorized(datetimes)
    if array.size == 1:
        return array.item()
    else:
        return array

def to_isoformat_string(datetime):
    return to_python_datetime_utc(datetime).isoformat()

_to_isoformat_string_vectorized = np.vectorize(to_isoformat_string)

def to_isoformat_strings(datetimes):
    array = _to_isoformat_string_vectorized(datetimes)
    if array.size == 1:
        return array.item()
    else:
        return array

def to_posix_timestamp(datetime):
    return to_python_datetime_utc(datetime).timestamp()

_to_posix_timestamp_vectorized = np.vectorize(to_posix_timestamp)

def to_posix_timestamps(datetimes):
    array = _to_posix_timestamp_vectorized(datetimes)
    if array.size == 1:
        return array.item()
    else:
        return array

def to_numpy_datetime(datetime):
    return to_pandas_timestamp_utc(datetime).to_datetime64()

_to_numpy_datetime_vectorized = np.vectorize(to_numpy_datetime)

def to_numpy_datetimes(datetimes):
    array = _to_numpy_datetime_vectorized(datetimes)
    if array.size == 1:
        return array.item()
    else:
        return array
