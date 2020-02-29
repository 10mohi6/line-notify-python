import os
import pytest
import time
from linenotipy import Line


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    token = os.environ["line_notify_token"]
    yield Line(token=token)


@pytest.fixture(scope="function", autouse=True)
def line(scope_module):
    time.sleep(1)
    yield scope_module


# @pytest.mark.skip
def test_line_post_message(line):
    expected = "ok"
    actual = line.post(message="Hello, world.")
    assert expected == actual["message"]


# @pytest.mark.skip
def test_line_post_image(line):
    expected = "ok"
    actual = line.post(message="Hello, image.", imageFile="tests/test.png")
    assert expected == actual["message"]


# @pytest.mark.skip
def test_line_post_stamp(line):
    expected = "ok"
    actual = line.post(message="Hello, stamp.", stickerPackageId=3, stickerId=180)
    assert expected == actual["message"]
