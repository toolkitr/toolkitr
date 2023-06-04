from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'A conversion package'
LONG_DESCRIPTION = 'A package that makes it easy to convert values between several units of measurement'

setup(
    name="kitr",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="toolkitr",
    author_email="toolkitr.email@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='toolkitr',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
