import setuptools


setuptools.setup(
    name="mailer",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'gui_scripts': [
            'mailer = mailer.main:main',
        ],
    },
    install_requires=[
        'pandas',
        'pyqt5',
        'xlrd',
    ],
)
