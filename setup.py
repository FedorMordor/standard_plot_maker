#!/usr/bin/env python

from setuptools import setup

setup(name='standard_plot_maker',
        version='0.1.0',
        #list folders, not files
        packages=['standard_plot_maker',
            'standard_plot_maker.test'],
        url='https://www.github.com/FedorMordor/standard_plot_maker.git',
        license='LICENSE.txt',
        description='An awesome package that draws fancy plots',
        long_description=open('README.md').read(),
        scripts=['standard_plot_maker/bin/script.py'],
        #package_data={'standard_plot_maker': ['data/cap_data.txt']},
        )
