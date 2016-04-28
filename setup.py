import setuptools

classifiers = ['Development Status :: 3 - Alpha',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: Implementation :: CPython'
               'Topic :: Communications', 'Topic :: Internet',
               'Topic :: Software Development :: Libraries']

requirements = ['pycares>=1,<2', 'tornado>=4.0']
tests_require = ['nose', 'mock', 'codecov', 'coverage']

setuptools.setup(name='tdns',
                 version='0.1.0',
                 description='An asynchronous Tornado wrapper for pycares',
                 long_description=open('README.rst').read(),
                 author='Gavin M. Roy',
                 author_email='gavinmroy@gmail.com',
                 url='http://github.com/gmr/tdns',
                 py_modules=['tdns'],
                 package_data={'': ['LICENSE', 'README.rst']},
                 include_package_data=True,
                 install_requires=requirements,
                 tests_require=tests_require,
                 license=open('LICENSE').read(),
                 classifiers=classifiers)
