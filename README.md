# linenotipy

[![PyPI](https://img.shields.io/pypi/v/linenotipy)](https://pypi.org/project/linenotipy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/10mohi6/line-notify-python/branch/master/graph/badge.svg)](https://codecov.io/gh/10mohi6/line-notify-python)
[![Build Status](https://travis-ci.com/10mohi6/line-notify-python.svg?branch=master)](https://travis-ci.com/10mohi6/line-notify-python)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/linenotipy)](https://pypi.org/project/linenotipy/)

linenotipy is a python client library for line notify api on Python 3.5 and above.


## Installation

    $ pip install linenotipy

## Usage

```python
#
# basic
#
from linenotipy import Line

line = Line(token='XXXXXXXXXX')
line.post(message="Hello, world.")

#
# image
#
from linenotipy import Line

line = Line(token='XXXXXXXXXX')
line.post(message="Hello, image.", imageFile="test.png")

#
# stamp
#
from linenotipy import Line

line = Line(token='XXXXXXXXXX')
line.post(message="Hello, stamp.", stickerPackageId=3, stickerId=180)


```
sticker [documentation](https://devdocs.line.me/files/sticker_list.pdf)


## Getting started

For help getting started with LINE Notify API, view our online [documentation](https://notify-bot.line.me/doc/en/).


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request