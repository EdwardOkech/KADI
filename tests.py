# from . import Score
import unittest
from app import Score

class TestScore(unittest.TestCase):

    def setUp(self):
        # Score.__init__(score=0)
        self.score = -3

    def test_score_is_added(self):

        self.assertTrue(self.score > 0)



if __name__ == '__main__':
	unittest.main()

