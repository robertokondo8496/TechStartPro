import unittest
from bson import ObjectId
import show

class MyTest(unittest.TestCase):
    def testWithoutFilter(self):
        case1 = ['categories']
        exp1 = [{ "_id" : ObjectId("5f9d957afb681241b7874ce4"), "Category" : "Móveis" },{ "_id" : ObjectId("5f9d957afb681241b7874ce5"), "Category" : "Decoração" },{ "_id" : ObjectId("5f9d957afb681241b7874ce6"), "Category" : "Celular" },{ "_id" : ObjectId("5f9d957afb681241b7874ce7"), "Category" : "Informática" },{ "_id" : ObjectId("5f9d957afb681241b7874ce8"), "Category" : "Brinquedos" }]
        res1 = show.show(case1[0])
        self.assertEqual(res1,exp1)

    def testWithFilter(self):
        case2 = ['categories', {"Category": "Celular"}]
        exp2 = [{ "_id" : ObjectId("5f9d957afb681241b7874ce6"), "Category" : "Celular" }]
        res2 = show.show(case2[0], case2[1])
        self.assertEqual(res2,exp2)

    def testWithFakeFilter(self):
        case3 = ['categories', {"Category": "Phone"}]
        exp3 = []
        res3 = show.show(case3[0], case3[1])       
        self.assertEqual(res3,exp3)

if __name__ == '__main__':
    unittest.main()