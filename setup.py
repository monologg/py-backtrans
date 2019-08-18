from setuptools import setup, find_packages

setup(
    name='pybacktrans',
    version='0.1.4',
    url='https://github.com/monologg/py-backtrans',
    license='MIT',
    author='Jangwon Park',
    author_email='adieujw@gmail.com',
    description='PyBacktrans: Python library for backtranslation',
    packages=find_packages(exclude=[]),
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['googletrans',
                      'nltk']
)
