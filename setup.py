from setuptools import setup, find_packages
with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name = 'Automated_Resume_Ranking',
    version = '1.0',
    description = '',
    url = 'https://github.com/MedEleliem/Automated_Resume_Ranking',
    author = 'Mohamed EL-ELIEM',
    author_mail = 'med.eleliem@gmail.com',
    license = 'AIOX',
    packages = ['nlp_resume'],
    package_dir = {'':'nlp_resume'},
    install_requires = required,
)