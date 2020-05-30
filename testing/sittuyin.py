# -*- coding: UTF-8 -*-


import unittest

from pychess.Utils.logic import validate
from pychess.Utils.lutils.lmovegen import genCheckEvasions, genCaptures, genAllMoves
from pychess.Utils.lutils.lmove import toAN
from pychess.Utils.Move import parseAN, parseSAN
from pychess.Variants.asean import SittuyinBoard

# . . . ♜ . ♜ . .
# . . . . ♝ ♛ . .
# ♚ ♞ . ♝ . . . ♟
# . . . . ♟ . ♟ ♙
# . . . . ♙ ♟ ♙ .
# ♙ . ♖ ♗ ♘ . . .
# . ♟ . ♕ ♔ ♗ . .
# . . ♖ . . . . .
FEN0 = "3r1r2/4sf2/kn1s3p/4p1pP/4PpP1/P1RSN3/1p1FKS2/2R5 b - - 1 21"

# . . . ♜ . ♜ . .
# . . . . ♝ . . .
# ♚ ♞ . ♝ . . . ♟
# . . . . ♟ . ♟ ♙
# . . . . ♙ ♟ ♙ .
# ♙ . ♖ ♗ ♘ . . .
# . ♟ . ♕ ♔ ♗ . .
# . . ♖ . . . . .
FEN1 = "3r1r2/4s3/kn1s3p/4p1pP/4PpP1/P1RSN3/1p1FKS2/2R5 b - - 1 21"

# . . . . . . . .
# . . . . . . . .
# ♖ . . ♙ . ♚ . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . ♔ . . .
FEN2 = "8/8/R2P1k2/8/8/8/8/4K3 w - - 0 9"

# . . . . . ♚ . .
# . . . . . . . .
# ♖ . . ♙ . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . ♔ . . .
FEN3 = "5k2/8/R2P4/8/8/8/8/4K3 w - - 0 9"

# . . . . . ♚ . .
# . . . . . . . .
# . . ♜ . . ♔ . .
# . . . ♙ . . . ♟
# . . . . . . . .
# . . . . . ♞ ♞ .
# . . . . . . . .
# . . . . . . . .
FEN4 = "5k2/8/2r2K2/3P3p/8/5nn1/8/8 w - - 0 9"

# . . . . . . . .
# . . ♚ . . . . .
# . . . . . . . .
# . . . . . . . .
# ♜ . . . . . . .
# . ♙ . . . . . .
# . . . . . . . .
# . ♖ ♔ . . . . .
FEN5 = "8/2k5/8/8/r7/1P6/8/1RK5[] w - - 0 9"


class SittuyinTestCase(unittest.TestCase):
    def test_validate(self):
        """Testing validate move in Sittuyin variant"""

        board = SittuyinBoard(setup=FEN0)
        print(board)
        self.assertTrue(validate(board, parseAN(board, 'f4f3')))
        self.assertTrue(validate(board, parseAN(board, 'b2b1')))
        self.assertTrue(validate(board, parseAN(board, 'b2c1')))

        # no promotion if we have Met (queen)
        self.assertFalse(validate(board, parseAN(board, 'b2b2f')))
        self.assertFalse(validate(board, parseAN(board, 'b2a1f')))
        self.assertFalse(validate(board, parseAN(board, 'f4f3f')))
        self.assertFalse(validate(board, parseAN(board, 'b2b1f')))
        self.assertFalse(validate(board, parseAN(board, 'b2c1f')))

        board = SittuyinBoard(setup=FEN1)
        print(board)
        # but (optional) promotion if we don't have Met (queen)
        self.assertFalse(validate(board, parseAN(board, 'b2b2f')))
        self.assertFalse(validate(board, parseSAN(board, 'b2=f')))
        self.assertEqual(parseAN(board, 'b2b2f'), parseSAN(board, 'b2=f'))
        self.assertTrue(validate(board, parseAN(board, 'b2a1f')))
        self.assertTrue(validate(board, parseSAN(board, 'a1=f')))
        self.assertEqual(parseAN(board, 'b2a1f'), parseSAN(board, 'a1=f'))
        self.assertTrue(validate(board, parseAN(board, 'b2c1')))
        self.assertTrue(validate(board, parseAN(board, 'f4f3')))

        self.assertFalse(validate(board, parseAN(board, 'f4f3f')))
        self.assertFalse(validate(board, parseAN(board, 'b2b2')))
        self.assertFalse(validate(board, parseAN(board, 'b2b1f')))
        self.assertFalse(validate(board, parseAN(board, 'b2c1f')))

        board = SittuyinBoard(setup=FEN2)
        print(board)
        # simple pawn move can give check
        self.assertTrue(validate(board, parseAN(board, 'd6d7')))
        # pawn can promote in place
        self.assertTrue(validate(board, parseAN(board, 'd6d6f')))
        # pawn promotion move can't give check
        self.assertFalse(validate(board, parseAN(board, 'd6c7f')))
        self.assertFalse(validate(board, parseAN(board, 'd6e7f')))

        board = SittuyinBoard(setup=FEN3)
        print(board)
        self.assertTrue(validate(board, parseAN(board, 'd6d7')))
        # last pawn being enywhere can promote
        self.assertTrue(validate(board, parseAN(board, 'd6d6f')))
        self.assertTrue(validate(board, parseAN(board, 'd6c7f')))
        self.assertTrue(validate(board, parseAN(board, 'd6c5f')))
        self.assertTrue(validate(board, parseAN(board, 'd6e5f')))
        # pawn promotion move can't give check
        self.assertFalse(validate(board, parseAN(board, 'd6e7f')))

        # https://www.facebook.com/Myanmar-Sittuyin-105323654491347/
        board = SittuyinBoard(setup=FEN5)
        print(board)
        self.assertTrue(validate(board, parseAN(board, 'b3b4')))
        self.assertTrue(validate(board, parseAN(board, 'b3a4')))

        self.assertFalse(validate(board, parseAN(board, 'b3a4f')))
        self.assertTrue(validate(board, parseAN(board, 'b3a2f')))
        self.assertTrue(validate(board, parseAN(board, 'b3c2f')))
        self.assertTrue(validate(board, parseAN(board, 'b3c4f')))
        self.assertFalse(validate(board, parseAN(board, 'b3b3f')))

    def test_geCaptures(self):
        """Testing validate move in Sittuyin variant"""

        board = SittuyinBoard(setup=FEN4)
        print(board)

        moves = set()
        for move in genCaptures(board.board):
            moves.add(toAN(board.board, move))
        self.assertEqual(moves, set(("d5c6",)))

    def test_genCheckEvasions(self):
        """Testing validate move in Sittuyin variant"""
        board = SittuyinBoard(setup=FEN4)
        print(board)

        moves = set()
        for move in genCheckEvasions(board.board):
            moves.add(toAN(board.board, move))
        self.assertEqual(moves, set(("d5c6", "d5d6", "d5e6=F")))

    def test_genAllMoves(self):
        """Testing validate move in Sittuyin variant"""
        board = SittuyinBoard(setup=FEN4)
        print(board)

        moves = set()
        for move in genAllMoves(board.board):
            moves.add(toAN(board.board, move))
        # pseudo legal moves
        m = set(("f6e7", "f6f7", "f6g7", "f6e6", "f6g6", "f6e5", "f6f5", "f6g5", "d5c6", "d5d6", "d5e6=F", "d5c4=F"))
        self.assertEqual(moves, m)


if __name__ == '__main__':
    unittest.main()
