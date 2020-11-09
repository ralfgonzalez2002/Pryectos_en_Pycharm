import unittest

class Vericacion(unittest.TestCase):

    def test_suma(self):
        a = 5 + 3
        b = 4 + 4
        self.assertEqual(b, a)

    def test_otra_suma(self):
        a = 7 + 2
        b = 4 + 3
        self.assertNotEqual(a, b, 'Los valores son iguales')

    def test_resta(self):
        a = 6 - 1
        b = 9 - 7
        #self.assertTrue(a != b, 'No se cumple la desigualdad')
        #self.assertFalse(b == a, 'La condicion no es falsa')
        #self.assertGreater (a, b)
        #self.assertGreaterEqual(a, b)
        #self.assertLess(b, a)
        self.assertLessEqual(a, b)



if __name__ == '__main__':
    unittest.main()
