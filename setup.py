import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='atcoder-scraper',
    version='0.0.1',
    author='ogyogy',
    author_email='',
    description='atcoder-scraper is a Python library to support automated testing of Atcoder.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ogyogy/atcoder-scraper',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests', 'beautifulsoup4', 'colorama'],
    entry_points={
        'console_scripts': [
            'atcoder-scraper = atcoderscraper.__main__:main',
        ],
    },
)
