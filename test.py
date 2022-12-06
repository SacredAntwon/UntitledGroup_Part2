# Licensing:
# Authors: Anthony Maida, Daniel VanDenEykel
# Contact: amaida@csu.fullerton.edu, d.vandeneykel@csu.fullerton.edu
#
# test.py
# This is the unit testing program.

import unittest
import os
import sys
import pathlib as pl

import anime

class TestStringMethods(unittest.TestCase):

    # Test if we generate the correct number of related shows
    def testRelatedShows(self):
        print("Testing number of related shows.")
        cosine_sim2, df = anime.similarity()
        id = 33206
        num = 3
        out_list = "test.txt"
        test = anime.get_recs(id, cosine_sim2, num, out_list)
        print(test)
        print("LENGTH", len(test))

    # Test to see if the json file exists
    def testFile(self):
        print("Testing to see if the file "
        "exists after generating the article.")
        cosine_sim2, df = anime.similarity()
        fileName = "testFile.txt"
        test = anime.get_recs(33206, cosine_sim2, 1, fileName)
        path = pl.Path(fileName)
        self.assertEqual((str(path), path.is_file()), (str(path), True))

if __name__ == '__main__':
    unittest.main()
