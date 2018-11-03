from setuptools import setup

setup(
    name='cp2stdout',
    packages=['cp2stdout'],
    version='@@VERSION@@',
    description='COOPER to MQTT',
    url='https://github.com/hardwario/cp2stdout',
    author='HARDWARIO s.r.o.',
    author_email='ask@hardwario.com',
    license='MIT',
    keywords = ['cooper', 'zmq', 'iot', 'stdout'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Environment :: Console',
        'Intended Audience :: Science/Research'
    ],
    install_requires=[
        'click>=6.7', 'PyYAML>=3.13','pyzmq>=17.1','schema>=0.6', 'simplejson>=3.16'
    ],
    entry_points='''
        [console_scripts]
        cp2stdout=cp2stdout.app:main
    '''
)
