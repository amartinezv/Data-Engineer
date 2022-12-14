import argparse
from asyncio.log import logger
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import pandas as pd

from article import Article
from base import Base, Engine, Session

def main(filename):
    Base.metadata.create_all(Engine)
    session = Session()
    logger.info(filename)
    articles = pd.read_csv(filename, on_bad_lines='skip')
    
    for index, row in articles.iterrows():
        logger.info('loading article uid {} into DB'.format(row['uid']))
        article = Article(row['uid'],
                          row['body'],
                          row['host'],
                          row['newspaper_uid'],
                          row['n_tokens_body'],
                          row['n_tokens_title'],
                          row['title'],
                          row['url'])
        session.add(article)
    
    session.commit()
    session.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The file you want to load into the db',
                        type=str)
    args = parser.parse_args()

    main(args.filename)