from setuptools import setup

setup(
    name='icicle_model_card',
    version='0.2',
    packages=['tests', 'icicle_model_card'],
    package_data={'icicle_model_card': ['schema/schema.json']},
    include_package_data=True,
    url='https://github.com/swsachith/icicle_model_card.git',
    license='BSD-3-Clause',
    author='Sachith Withana',
    author_email='swithana@iu.edu',
    description='ICICLE Model Card Tool',
    install_requires=[
        'attrs~=23.1.0',
        'jsonschema~=4.18.6',
        'fairlearn~=0.9.0',
        'scikit-learn~=1.3.1'
    ]
)
