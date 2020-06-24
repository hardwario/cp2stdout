import click
import json
import logging.config
import sys
import simplejson as json
import zmq
from .config import load_config

__version__ = '@@VERSION@@'


@click.command()
@click.option('--config', '-c', 'config_file', type=click.File('r'), required=True, help='Configuration file.')
@click.option('--test', is_flag=True, help='Test configuration file.')
@click.version_option(version=__version__)
def cli(config_file, test=False):
    '''ZeroMQ to stdout.'''

    try:
        config = load_config(config_file)
        config_file.close()
    except Exception as e:
        logging.error('Failed opening configuration file')
        logging.error(str(e))
        sys.exit(1)

    if test:
        click.echo("The configuration file seems ok")
        return

    logging.config.dictConfig(config['log'])
    logging.info('Process started')

    run(config)


def run(config):
    context = zmq.Context()
    sock = context.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, '')
    sock.connect('tcp://%s:%d' % (config['zmq']['host'], config['zmq']['port']))

    while True:
        try:
            payload = sock.recv_json()
            print(json.dumps(payload, use_decimal=True), flush=True)
        except Exception:
            logging.error('Unhandled exception', exc_info=True)


def main():
    try:
        cli()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        click.echo(str(e), err=True)
        sys.exit(1)
