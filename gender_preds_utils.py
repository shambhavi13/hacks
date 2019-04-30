import re
import pandas as import pd
import numpy as np 


def _load_data(filename):
    """
    Loads data file and returns  dataframe
    """

    df = pd.read_csv(filename, sep='\t')
    # no need of Person ID for this project
    df = df.drop(columns='Person ID')
    # remove duplicate names
    df = df.drop_duplicates(subset="Person Name")

    return df

def _preprocess(df, col_list, non_latin):
    """
    Preprocess names removes non latin chars and
    return clean string

    non_latin = r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]'
    """

    df = df.copy().dropna()
    for col in col_list:
        contains_non_latin = df[col].str.contains(non_latin)
        series = df[col].apply(
            lambda x: ''.join([c for c in
                               re.sub(r'\s+', ' ', x).strip()]).strip())
        df[col] = series

        df = df[(series != '') &
                (series != 'None') &
                (~contains_non_latin)]
        
    return df

def _preprocess_ascii(df):
    """
    Preprocess names removes non ascii chars
    return clean string
    """
    return ''.join(i for i in text if ord(i)<128)


def _num_chars(df, col):
    """
    Finds the number of characters
    a-z, 0–9, space, dot and a special END token.
    """

    vocab = set(' '.join([str(i) for i in df[col]]))
    vocab.add('END')
    len_vocab = len(vocab)

    return vocab, len_vocab

def _char_idx(vocab):
    """
    assign characters with index
    """
    char_idx = dict((c, i) for i, c in enumerate(vocab))

    return char_idx

def _set_flag(i, len_vocab):
    """
    generates array of zeros
    """
    tmp = np.zeros(len_vocab)
    tmp[i] = 1
    return tmp



