from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='ORM for Contentful',
    version='0.2.0',
    author='David Feldman',
    author_email='dsfeldman@visiblelab.org',
    description="A Python library for Contentful to let you create/maintain Content Types and queries in ORM style.",
    packages=['contentful_orm', 'contentful_orm.fields'],
    scripts=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/rightandleftbrain/ContentORM',
    install_requires=[
        'contentful_management',
        'python-baseconv'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
