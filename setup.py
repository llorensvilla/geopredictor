# setup.py
from setuptools import setup, find_packages

setup(
    name='geopocket',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'geopocket = geopocket.predictor:main',
            #                      ^ paquete     ^ archivo .py sin extensión
            #                                    ^ función main() dentro de predictor.py
        ],
    },
    install_requires=[
        'numpy',
        'scipy',
        'scikit-learn'
    ],
    python_requires='>=3.8',
)

