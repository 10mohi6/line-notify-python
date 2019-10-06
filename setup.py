from setuptools import setup, find_packages

with open('README.md') as f:
   long_description = f.read()

setup(
    name  = 'line-notify',
    version = '1.0.0',
    description = 'line-notify is a python client library for line notify api on Python 3.5 and above.',
    long_description = long_description,
    long_description_content_type="text/markdown",
    license = 'MIT',
    author = '10mohi6',
    author_email = '10.mohi.6.y@gmail.com',
    url='https://github.com/10mohi6/line-notify-python',
    keywords = 'line notify python',
    packages = find_packages(),
    install_requires = [],
    python_requires=">=3.5.0",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat',
        'Topic :: System :: Networking',
        'Topic :: Office/Business',
        'License :: OSI Approved :: MIT License'
    ]
)