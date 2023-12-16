import setuptools
import pathlib

# Read the contents of your README file
with open(pathlib.Path('README.md'), encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='crafter',
    version='1.8.3',
    description='Open world survival game for reinforcement learning.',
    url='http://github.com/danijar/crafter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['crafter'],
    package_data={'crafter': ['data.yaml', 'assets/*']},
    entry_points={'console_scripts': ['crafter=crafter.run_gui:main']},
    install_requires=[
        'numpy', 'imageio', 'pillow', 'opensimplex', 'ruamel.yaml',
    ],
    extras_require={'gui': ['pygame']},
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
