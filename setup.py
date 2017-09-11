from setuptools import setup, find_packages

setup(
    name='R3PI',
    version='1.0',
    description='test exercise',
    classifiers=[
        'Development Status :: Beta',
        'License :: Open source',
        'Programing language :: Python :: 3.6',
        'Topic :: Test :: restAPI :: Mobile'
    ],
    keywords='test',
    author='Tako Ferenc',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 'requests', 'html-TestRunner', 'Appium-Python-Client'
    ],
    entry_points='''
        [console_scripts]
        R3PI=main:cli
    ''',
)