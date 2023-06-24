from setuptools import setup
import glob

setup(
    name='icicle_model_card',
    version='0.1',
    packages=['tests', 'icicle_model_card'],
    url='https://github.com/swsachith/icicle_model_card.git',
    license='BSD-3-Clause',
    author='Sachith Withana',
    author_email='swithana@iu.edu',
    description='ICICLE Model Card Tool',
    data_files=glob.glob('schema/**'),
    install_requires=[
        'attrs~=23.1.0',
        'jsonschema~=4.17.3'
    ]
)
