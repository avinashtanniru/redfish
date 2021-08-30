from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt')

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir) for ir in install_reqs]


setup(
    name='refdfish',
    version='1.0',
    py_modules=['redfish'],
    author='navneeth0053',
    author_email='navneeth.devops@gmail.com',
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'redfish = redfish:cli',
        ],
    },
)

