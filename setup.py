from setuptools import setup


setup(
    name='hobson',
    version=__import__('hobson').__version__,
    url='https://github.com/asweigart/hobson',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A GUI toolkit with simple features, take it or leave it. Cross-platform, text-based, built on tkinter, pure Python 3.'),
    license='BSD',
    packages=[],
    test_suite='tests',
    install_requires=[],
    keywords="",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)