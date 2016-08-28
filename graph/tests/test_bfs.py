import unittest
from graph.bfs import bfs
from nose.tools import set_trace


class TestBfs(unittest.TestCase):

    line = {1 : [2], 2 : [3], 3 : []}

    def test_bfs_line(self):
        self.assertEqual(
            bfs(1, 3, lambda n : self.line[n]),
            [1, 2, 3]
            )
        self.assertEqual(
            bfs(2, 3, lambda n : self.line[n]),
            [2, 3]
            )
        self.assertEqual(
            bfs(3, 1, lambda n : self.line[n]),
            None
            )
    
    loop = {1 : [1]}

    def test_bfs_loop(self):
        self.assertEqual(
            bfs(1, 1, lambda n : self.loop[n]),
            [1, 1]
            )
            
    fakeloop = {1 : [2, 3], 2 : [2], 3 : [1]}
    
    def test_bfs_fakeloop(self):
        self.assertEqual(
            bfs(1, 3, lambda n : self.fakeloop[n]),
            [1, 3]
            )

    royals = {
        'Elizabeth' : [
            'Charles',
            'Andrew',
            'Edward',
            'Anne',
            ],
        'Charles' : [
            'William',
            'Henry',
            ],
        'William' : [
            'George',
            'Charlotte',
            ],
        'Andrew' : [
            'Beatrice',
            'Eugenie',
            ],
        }

    def test_bfs_royals(self):
        def royals_successors(n):
            if n in self.royals:
                return self.royals[n]
            else:
                return []

        # set_trace()
        self.assertEqual(
            bfs('Elizabeth', 'Charlotte', royals_successors),
            ['Elizabeth', 'Charles', 'William', 'Charlotte']
            )
        self.assertEqual(
            bfs('Elizabeth', 'Nigel', royals_successors),
            None
            )

