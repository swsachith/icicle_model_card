from setuptools import setup

setup(
    name='model-cards-icicle',
    version='0.1',
    packages=['tests', 'model-cards-icicle'],
    url='https://github.com/swsachith/model-card-icicle.git',
    license='BSD-3-Clause',
    author='Sachith Withana',
    author_email='swithana@iu.edu',
    description='ICICLE Model Card Tool',
    install_requires=[
        'attrs~=23.1.0',
        'jsonschema~=4.17.3'
    ]
)
