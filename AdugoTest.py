import unittest
from Adugo import Adugo


class AdugoTest(unittest.TestCase):
    C_NOT_INIT = "NOT_INITIALIZED"
    C_EMPTY = 0
    C_DOG = 2

    EMPTY_LIST = []
    INITIALIZED_LIST = [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2],
                        [12, 2], [13, 1], [14, 2], [15, 2], [16, 0], [17, 0], [18, 0], [19, 0], [20, 0], [21, 0],
                        [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0]]

    JAGUAR_INIT_POS = 13
    JAGUAR_TEST_TARGET = 17

    RANDOM_DOG_POS = 14
    RANDOM_DOG__TEST_TARGET = 19

    def testInit(self):
        adugo = Adugo()
        self.assertListEqual(adugo.getBoard(), AdugoTest.EMPTY_LIST)
        self.assertEqual(adugo.getStatus(), AdugoTest.C_NOT_INIT)

    def testNewBoard(self):
        adugo = Adugo()
        adugo.newBoard()
        self.assertListEqual(adugo.getBoard(), AdugoTest.INITIALIZED_LIST)

    def testJaguarPlay(self):
        adugo = Adugo()
        adugo.newBoard()
        self.assertEqual(adugo.getJaguarPosition(), AdugoTest.JAGUAR_INIT_POS)
        adugo.jaguarWalk(AdugoTest.JAGUAR_TEST_TARGET)
        self.assertEqual(adugo.getJaguarPosition(), AdugoTest.JAGUAR_TEST_TARGET)

    def testDogPlay(self):
        adugo = Adugo()
        adugo.newBoard()
        adugo.jaguarWalk(AdugoTest.JAGUAR_TEST_TARGET)
        self.assertEqual(adugo.getPositionContent(AdugoTest.RANDOM_DOG__TEST_TARGET), AdugoTest.C_EMPTY)
        self.assertEqual(adugo.getPositionContent(AdugoTest.RANDOM_DOG_POS), AdugoTest.C_DOG)
        adugo.dogPlay(AdugoTest.RANDOM_DOG_POS, AdugoTest.RANDOM_DOG__TEST_TARGET)
        self.assertEqual(adugo.getPositionContent(AdugoTest.RANDOM_DOG__TEST_TARGET), AdugoTest.C_DOG)
        self.assertEqual(adugo.getPositionContent(AdugoTest.RANDOM_DOG_POS), AdugoTest.C_EMPTY)


if __name__ == '__main__':
    unittest.main()
