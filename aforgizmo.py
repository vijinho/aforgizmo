'''
Aforgizmo CLI
==============

An App which saves, retrieves, edits and displays aphorisms
'''

import click
import os
import pwd
import models

# setup config passing storage
class Config(object):
    def __init__(self):
        self.verbose = False
pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('-v', '--verbose', is_flag=True)
@click.option('-l', '--logfile',
              type=click.File('w'),
              required=False)
@pass_config
def cli(config, verbose, logfile):
    config.verbose = verbose
    config.logfile = logfile
    config.username = pwd.getpwuid(os.getuid())[0]

    # display some verbose information
    if config.verbose:
        click.echo(click.style('Verbose mode: Enabled',
                               fg='white',
                               bold=True,
                               reverse=True,
                               blink=True))

@cli.command()
@click.option('-a', '--author',
              prompt='Who are you quoting?',
              help='The author of the aphorism.',
              required=True,
              default='Anonymous')
@click.option('-s', '--source',
              prompt='Where did you source the text?',
              help='The source of the aphorism text.',
              required=False,
              default='Unknown')
@click.option('-text', '--aphorism',
              prompt='Write the aphorism',
              help='The text of the aphorism itself.',
              required=True)
@click.option('-t', '--hashtags',
              prompt='Hashtags',
              help='Hashtags for the aphorism, space or comma separated, '
                   '# symbol optional',
              required=False,
              default='none')
@pass_config
def add(config, author, source, aphorism, hashtags):
    '''Add an aphorism.'''
    try:
        aphorism = models.Aphorism(
            author=author,
            source=source,
            aphorism=aphorism,
            hashtags=hashtags)
        aphorism.save()
    except Exception:
        click.echo(click.style('Failed saving the aphorism!',fg='red'),
                           file=config.logfile)
    else:
        click.echo(click.style('Saved the aphorism successfully.',fg='green'),
                   file=config.logfile)

@cli.command()
@click.option('-id',
              type=int,
              required=True,
              prompt='Aphorism Id',
              help='The aphorism id within the database')
@pass_config
def get(config, id):
    '''Get an aphorism by ID.'''
    click.echo(click.style('LOADING FROM THE DATABASE NOT YET IMPLEMENTED',
                           fg='red'),
                           file=config.logfile)
@cli.command()
@click.option('-id',
              type=int,
              required=True,
              prompt='Aphorism Id',
              help='The aphorism id within the database')
@pass_config
def remove(config, id):
    '''Remove an aphorism by ID.'''
    click.echo(click.style('DELETING FROM THE DATABASE NOT YET IMPLEMENTED',
                           fg='red'),
                           file=config.logfile)

@cli.command()
@pass_config
def random(config):
    '''Get a random aphorism.'''
    click.echo(click.style('LOADING A RANDOM APHORISM FROM THE DATABASE NOT '
                           'YET IMPLEMENTED',
                           fg='red'),
                           file=config.logfile)

@cli.command()
@click.option('-sf', '--source-file',
              required=True,
              help='The full path to the source file.',
              prompt='Source File',
              default='data/aphorisms.json')
@click.option('-if', '--input-format',
              type=click.Choice(['json', 'csv']),
              default='json',
              prompt='Input Format (json|csv)',
              help='The input format of the source file.')
@pass_config
def insert(config, source_file, input_format):
    '''Insert aphorisms by file.'''
    click.echo(click.style('IMPORTING APHORISMS TO THE DATABASE NOT '
                           'YET IMPLEMENTED',
                           fg='red'),
                           file=config.logfile)

@cli.command()
@click.option('-tf', '--target-file',
              type=click.File('w'),
              required=True,
              help='The full path to the output target file.',
              prompt='Target Output File',
              default='data/dumpfile.json')
@click.option('-of', '--output-format',
              type=click.Choice(['text', 'json', 'csv', 'html']),
              default='json',
              prompt='Output Format (json|csv|txt|html)',
              help='The output format of the data.')
@pass_config
def dump(config, target_file, output_format):
    '''Dump all aphorisms to a file.'''
    click.echo(click.style('OUTPUT OF APHORISMS FROM THE DATABASE NOT '
                           'YET IMPLEMENTED',
                           fg='red'),
                           file=config.logfile)

@cli.command()
@pass_config
def list(config):
    '''Show all aphorisms.'''
    click.echo(click.style('LISTING OF APHORISMS FROM THE DATABASE NOT '
                           'YET IMPLEMENTED',
                           fg='red'),
                           file=config.logfile)

@cli.command()
@click.option('-t', '--tag',
              required=True,
              prompt='Search Tag',
              help='The tag to search for.')
@pass_config
def search(config, tag):
    '''Search for an aphorism by tag.'''
    click.echo(click.style('SEARCHING FOR APHORISMS IN THE DATABASE NOT '
                           'YET IMPLEMENTED',
                           fg='red'),
                           file=config.logfile)

if __name__ == '__main__':
    cli()
