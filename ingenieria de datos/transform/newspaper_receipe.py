import argparse #convertirlo en un script
import logging

from matplotlib.pyplot import axis #para decirle al usuario que esta sucediendo
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse

import hashlib
import re
import nltk
from nltk.corpus import stopwords
import pandas as pd

logger = logging.getLogger(__name__)



def main(filename):
    logger.info('Strating cleanning process')

    df = _read_data(filename)
    newspaper_uid = _extract_newspaper_uid(filename)
    df = _add_newspaper_uid_column(df, newspaper_uid)
    host = _extract_host(df)
    df = _add_host_column(df, host)
    df = _fill_missing_titles(df)
    df = _generate_uids_for_row(df)
    df = _additional_cleanup(df)
    df = _tokenize_column(df, 'title')
    df = _tokenize_column(df, 'body')
    df = _remove_duplicate_entries(df, 'title')
    df = _drop_rows_with_missing_values(df)
    _save_data(df, filename)

    return df

def _read_data(filename):
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    return newspaper_uid

def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))

    df['newspaper_uid'] = newspaper_uid

    return df

def _extract_host(df):
    logger.info('Extracting host from urls')
    host = df['url'].apply(lambda url: urlparse(url).netloc)

    logger.info('Host detected')
    return host

def _add_host_column(df, host):
    logger.info('Filling host column with host detected')
    df['host'] = host

    return df

def _fill_missing_titles(df):
    logger.info('Filling missing titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url']
                        .str.extract(r'(?P<missing_titles>[^/]+)$')
                        .applymap(lambda title: title.replace('-',' ')))

    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df

def _generate_uids_for_row(df):
    logger.info('Generate uids for row')
    uids = (df
            .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
            .apply(lambda hash_object:hash_object.hexdigest())
    )
    df['uid'] = uids
    
    return df.set_index('uid')

def _additional_cleanup(df):
    logger.info('Remove some punctuation marks from body')
    stripped_body = (df
        .apply(lambda row: row['body'], axis=1)
        .apply(lambda body: re.sub(r'(\n|\r|\[|\]|\')+',r'', body))

    )
    df['body'] = stripped_body
    return df

def _tokenize_column(df, column_name):
    logger.info('Calculating the number of unique tokens in {}'.format(column_name))
    stop_words = set(stopwords.words('spanish'))
    df['n_tokens_{}'.format(column_name)]= (df
                                            .dropna()
                                            .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
                                            .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
                                            .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
                                            .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
                                            .apply(lambda valid_word_list: len(valid_word_list))
                                            )
    return df


def _remove_duplicate_entries(df, column_name):
    logger.info('Removing dupicate entries')
    df.drop_duplicates(subset=[column_name],keep ='first', inplace =True)

    return df

def _drop_rows_with_missing_values(df):
    logger.info('dropping rows with missing values')
    return df.dropna()

def _save_data(df, filename):
    clean_filename = 'clean_{}'.format(filename)
    logger.info('Saving data at location: {}'.format(clean_filename))
    df.to_csv(clean_filename, encoding='utf-8-sig')



if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('filename',
                        help='The path to the dirty data',
                        type=str)
    arg = parse.parse_args()

    df = main(arg.filename)
    #print(df)
    