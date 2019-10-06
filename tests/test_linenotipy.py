import os, pytest
from linenotipy import Line

class TestLine(object):

    def setup_method(self, method):
        token = os.environ['line_notify_token']
        self.line = Line(token=token)

    def test_post_message(self):

        expected = 'ok'
        actual = self.line.post(message="Hello, world.")
        assert expected == actual['message']

    def test_post_image(self):

        expected = 'ok'
        actual = self.line.post(message="Hello, image.", imageFile="tests/test.png")
        assert expected == actual['message']

    def test_post_stamp(self):

        expected = 'ok'
        actual = self.line.post(message="Hello, stamp.", stickerPackageId=3, stickerId=180)
        assert expected == actual['message']
