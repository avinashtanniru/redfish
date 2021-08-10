import click
import lib.ImportSysConfigFile as imp
import lib.ResetDracPass as rstpwd
import lib.GeneratePass as np
import yaml
import os

def common_params(func):
    @click.option('-s', '--source', envvar='SOURCE', default=os.path.join(os.getcwd(), "config.yml"),
              type=str, help='Source YAML file.')
    # @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@click.group()
def cli():
    """
    This is a Redfish CLI Tool.
    """

@cli.command('enableAD', short_help='Enable AD to DELL.')
@common_params
def enableAD(source):
    """
    Enable AD to iDRAC.
    """
    print("AD Enabled")
    y = getConfig(source)
    for x in y['IDRAC']:
        imp.args['ip'] = x['host']
        imp.args['u'] = x['user']
        imp.args['p'] = x['pass']
        imp.Run()

@cli.command('resetPWD', short_help='Reset root password for DELL iDrac.')
@click.option('-f', '--file', envvar='FILE', default=os.path.join(os.getcwd(), "passwords.csv"),
              type=str)
@common_params
def resetPWD(source,file):
    """
    Reset root password for DELL idrac.
    """
    print("Reset Root Password")
    y = getConfig(source)
    np.export(file, 'create', 'h')
    for x in y['IDRAC']:
        newpwd = np.get_password()
        rstpwd.args['ip'] = x['host']
        rstpwd.args['u'] = x['user']
        rstpwd.args['p'] = x['pass']
        rstpwd.args['np'] = newpwd

        rstpwd.Run()
        data = [ x['host'], newpwd ]
        print(data)
        np.export(file, data, 'a')

def getConfig(source):
    with open(source, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
