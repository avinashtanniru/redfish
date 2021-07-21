import click
import lib.ImportSysConfigFile as imp
import yaml

@click.group()
def cli():
    """
    This is a Redfish CLI Tool.
    """

@cli.command('enableAD', short_help='Enable AD to DELL')
def enableAD():
    """
    Enable AD to iDRAC.
    """
    print("AD Enabled")
    y = getConfig()
    for x in y['IDRAC']:
        imp.args['ip'] = x['host']
        imp.args['u'] = x['user']
        imp.args['p'] = x['pass']
        imp.Run()

def getConfig():
    with open("config.yml", 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
