import unittest
import reader

class MyTest(unittest.TestCase):
    def test(self):
        exp = [ {"Category": "Móveis"},{"Category": "Decoração"},{"Category": "Celular"},{"Category": "Informática"},{"Category": "Brinquedos"}]
        res = reader.read('categorias.csv')
        self.assertEqual(res,exp)

if __name__ == '__main__':
    unittest.main()