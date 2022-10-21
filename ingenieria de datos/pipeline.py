from distutils.command.clean import clean
from distutils.log import info
import logging

from click import command
from sqlalchemy import true
logging.basicConfig(level=logging.INFO)
import subprocess # manipular archivos de terminal
import os
import re
import datetime
import sys

logger = logging.getLogger(__name__)
news_sites_uids = ['semana']
cwd_path = re.sub(r'(\')+',r'', os.path.abspath(os.getcwd()))

def main():
    _extract()
    _transform()
    _load()

def _extract():
    logger.info('Strating extract process')

    for news_site_uid in news_sites_uids:
        subprocess.run([sys.executable, 'main.py', news_site_uid], cwd='./extract')
        now = datetime.datetime.now().strftime('%Y_%m_%d')
        out_file_name = '{news_site_uid}_{datetime}_articles.csv'.format(news_site_uid=news_site_uid, datetime=now)
        command = "MOVE \"{}\\extract\\{}\" \"{}\\transform\\{}_.csv\"".format(cwd_path, out_file_name, cwd_path,news_site_uid)
        subprocess.call(command, shell=True)
        

def _transform():
    logger.info('Strating transform process')
    
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}_.csv'.format(news_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run([sys.executable,'newspaper_receipe.py', dirty_data_filename], cwd='./transform')
        command_delete = "del {}".format(dirty_data_filename)
        subprocess.call(command_delete, shell=True, cwd='./transform')
        command_move = "MOVE \"{}\\transform\\{}\" \"{}\\load\\{}_.csv\"".format(cwd_path, clean_data_filename, cwd_path,news_site_uid)
        subprocess.call(command_move, shell=True, cwd='./transform')

def _load():
    logger.info('Starting load process')

    for news_site_uid in news_sites_uids:
        clean_data_filename = '{}_.csv'.format(news_site_uid)
        subprocess.run([sys.executable, 'main.py', clean_data_filename], cwd='./load')
        command_delete = 'del {}'.format(clean_data_filename)
        subprocess.call(command_delete, shell=True, cwd='./load')

if __name__=='__main__':
    main()