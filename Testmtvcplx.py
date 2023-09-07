import unittest
import numpy as np
import base as mt


class TestCplxOperations (unittest.TestCase):

    def test_sumavect (self):
        v1=np.array([complex(2,3), complex(4, -1), complex (6, -5)])
        v2 = np.array([complex(1,-7), complex(0, 9), complex (-4, 4)])
        expected = np.array([complex(3,-4), complex(4,8), complex(2,-1)])
        suma = mt.sumavect(v1, v2)
        np.testing.assert_almost_equal(suma, expected)

        v1 = np.array([complex(15, 20), complex(38, -4), complex(5, -61)])
        v2 = np.array([complex(7, -8), complex(89, 24), complex(32, 0)])
        expected = np.array([complex(22, 12), complex(127, 20), complex(37, -61)])
        suma = mt.sumavect(v1,v2)
        np.testing.assert_almost_equal(suma, expected)

    def test_sum_inver (self):
        v1 = np.array([complex(2,3), complex(4, -1), complex (6, -5)])
        expected = np.array([complex(0,0), complex(0,0), complex(0,0)])
        suma = mt.sum_inver(v1)
        np.testing.assert_almost_equal (suma, expected)

        v2 = np.array([complex(15, 20), complex(38, -4), complex(5, -61)])
        expected = np.array([complex(0, 0), complex(0, 0), complex(0, 0)])
        suma = mt.sum_inver(v2)
        np.testing.assert_almost_equal(suma, expected)

    def test_multEsc_vect(self):
        v1 = np.array([complex(2,3), complex(4, -1), complex (6, -5)])
        E = 4
        expected =  np.array([complex(8, 12), complex(16, -4), complex(24, -20)])
        mult = mt.multEsc_vect(E , v1)
        np.testing.assert_almost_equal (mult, expected)

        v2 = np.array ([complex(15, 20), complex(38, -4), complex(5, -61)])
        E = 4
        expected = np.array([complex(60, 80), complex(152, -16), complex(20, -244)])
        mult = mt.multEsc_vect(E , v2)
        np.testing.assert_almost_equal (mult, expected)

    def test_SumMatrix (self):
        matriz1= np.matrix([[complex(2,3), complex(45, -1)], [complex (69, -5),complex(20,-5)]])
        matriz2 = np.matrix ([[complex(15,8), complex(42, -51)], [ complex (6, -5),complex(95,-22)]])
        expected = np.matrix ([[complex(17,11), complex(87, -52)], [ complex (75, -10),complex(115,-27)]])
        sumaMatrix = mt.SumMatrix(matriz1, matriz2)
        np.testing.assert_almost_equal(sumaMatrix, expected)

        matriz3 = np.matrix([[complex(0,0), complex(11, -22)], [complex (33, -44),complex(55,-66)]])
        matriz4 = np.matrix ([[complex(77,88), complex(99, -51)], [ complex (63, -54),complex(95,-22)]])
        expected = np.matrix ([[complex(77,88), complex(110, -73)], [ complex (96, -98),complex(150,-88)]])
        sumaMatrix = mt.SumMatrix(matriz3 , matriz4)
        np.testing.assert_almost_equal (sumaMatrix, expected)


    def test_SumAditMatriz(self):
        matrizO= np.matrix([[complex(2, 3), complex(45, -1)], [complex(69, -5), complex(20, -5)]])
        expected= np.matrix([[complex(0, 0), complex(0, 0)], [complex(0, 0), complex(0, 0)]])
        sumadit = mt.SumAditMatriz(matrizO)
        np.testing.assert_almost_equal (sumadit, expected)

        matrizO = np.matrix([[complex(15,8), complex(42, -51)], [ complex (6, -5),complex(95,-22)]])
        expected = np.matrix([[complex(0, 0), complex(0, 1)], [complex(0, 0), complex(0, 0)]])
        sumadit = mt.SumAditMatriz(matrizO)
        np.testing.assert_almost_equal(sumadit, expected)

    def test_MultEMatrix(self):
        matriz_original= np.matrix([[complex(2, 3), complex(45, -1)], [complex(69, -5), complex(20, -5)]])
        expected = np.matrix([[complex (8, 12), complex(180,-4)], [complex(276,-20), complex(80, -20)]])
        multMatEsc = mt.MultEMatrix(4* matriz_original)
        np.testing.assert_almost_equal (multMatEsc, expected)

        matriz_original = np.matrix([[complex(2, 3), complex(45, -1)], [complex(69, -5), complex(20, -5)]])
        expected = np.matrix([[complex (4, 6), complex(90,-2)], [complex(138,-10), complex(40, -10)]])
        multiMatEsc = mt.MultEMatrix(2* matriz_original)
        np.testing.assert_almost_equal (multiMatEsc, expected)

    def test_transpuestaMatriz (self):
        matriz_original = np.matrix([[complex(2, 3), complex(45, -1)], [complex(69, -5), complex(20, -5)]])
        expected = np.matrix([[complex(2, 3), complex(69, -5)], [complex(45, -1), complex(20, -5)]])
        transpose = mt.transpuestaMatriz(matriz_original)
        np.testing.assert_almost_equal(transpose, expected)

        matriz_original = np.matrix([[complex(15,8), complex(42, -51)], [ complex (6, -5),complex(95,-22)]])
        expected = np.matrix([[complex(15,8), complex (6, -5)], [ complex(42, -51),complex(95,-22)]])
        transpose = mt.transpuestaMatriz(matriz_original)
        np.testing.assert_almost_equal (transpose, expected)


    def test_transVector (self):
        vector_original = np.array([complex(2,3), complex(4, -1), complex (6, -5)])
        expected = np.array([complex(2,3), complex(4, -1), complex (6, -5)])
        transposev = mt.transVector(vector_original)
        np.testing.assert_almost_equal (transposev,expected )

        vector_original = np.array([complex(1,-7), complex(0, 9), complex (-4, 4)])
        expected = np.array([complex(1,-7), complex(0, 9), complex (-4, 4)])
        transvect = mt.transVector(vector_original)
        np.testing.assert_almost_equal (transvect, expected)

    def test_ConjMatrix (self):
        mo = np.matrix([[complex(1,3), complex(4, -6)], [ complex (7, -9),complex(2,-5)]])
        expected = np.matrix([[complex(1,-3), complex(4, 6)], [ complex (7, 9),complex(2,5)]])
        conj = mt.ConjMatrix(mo)
        np.testing.assert_almost_equal(conj, expected)

        mo = np.matrix ([[complex(1,3), complex(4, 5)], [ complex (6, -5),complex(9,-0)]])
        expected = np.matrix([[complex(1, -3), complex(4, -5)], [complex(6, 5), complex(9, 0)]])
        conj = mt.ConjMatrix(mo)
        np.testing.assert_almost_equal(conj, expected)


    def test_ConjVect (self):
        vo = np.array([complex(2,3), complex(4, -1), complex (6, -5)])
        expected = np.array([complex(2,-3), complex(4, +1), complex (6, +5)])
        conj = mt.ConjVect(vo)
        np.testing.assert_almost_equal(conj, expected)

        vo = np.array([complex(1,-7), complex(0, 9), complex (-4, 4)])
        expected = np.array([complex(1,7), complex(0, -9), complex (-4, -4)])
        conj = mt.ConjVect(vo)
        np.testing.assert_almost_equal(conj, expected)

    def test_adjunMatrix(self):
        mo = np.matrix([[complex(1,3), complex(4, -6)], [ complex (7, -9),complex(2,-5)]])
        expected = np.matrix([[complex(1,-3), complex (7, 9)], [ complex(4, 6),complex(2,5)]])
        adj = mt.adjunMatrix(mo)
        np.testing.assert_almost_equal(adj, expected)

        mo = np.matrix ([[complex(1,3), complex(4, 5)], [ complex (6, -5),complex(9,-0)]])
        expected = np.matrix ([[complex(1,-3), complex (6, 5)], [ complex(4, -5),complex(9,0)]])
        adj = mt.adjunMatrix(mo)
        np.testing.assert_almost_equal(adj, expected)

    def test_accmatrix(self):
        m = np.matrix([complex(11, -27)])
        v = np.array([[complex(1, 3), complex(4, 5)]])
        expected = np.matrix([complex(92, 6), complex (179, -53)])
        acc = mt.accmatrix(m, v)
        np.testing.assert_almost_equal(acc, expected)

        m = np.matrix([complex(15, 30)])
        v = np.array([[complex(1, 6), complex(9, 25)]])
        expected = np.matrix([complex(-165, 120), complex(-615, 645)])
        acc = mt.accmatrix(m, v)
        np.testing.assert_almost_equal(acc, expected)


    def test_productMatrix(self):
        mo= np.matrix([[complex(1,3), complex(4, -6)], [complex (7, -9),complex(2,-5)]])
        m1= np.matrix ([[complex(1,3), complex(4, 5)], [complex (6, -5),complex(9,-0)]])
        expected = np.matrix ([[complex(-14,-50), complex(25,-37)], [complex (21,-28 ),complex(91,-46)]])
        product= mt.productMatrix(mo, m1)
        np.testing.assert_almost_equal (product, expected)

        mo = np.matrix([[complex(2, 6), complex(8, -12)], [complex(14, -18), complex(4, -10)]])
        m1 = np.matrix([[complex(1, 3), complex(4, 5)], [complex(6, -5), complex(9, -0)]])
        expected = np.matrix([[complex(-28, -100), complex(50, -74)], [complex(42, -56), complex(182, -92)]])
        product = mt.productMatrix(mo, m1)
        np.testing.assert_almost_equal(product, expected)

    def test_ProdcIntVc(self):
        v1 = np.array([complex(2,3), complex(4, -1), complex (6, -5)])
        v2 = np.array([complex(1,-7), complex(0, 9), complex (-4, 4)])
        expected = complex(28, 69)
        productInt = mt.ProdcIntVc(v1, v2)
        np.testing.assert_almost_equal (productInt, expected)

        v3 = np.array([complex(-2,31), complex(14, -10), complex (16, -35)])
        v4 = np.array([complex(11,-27), complex(50, 19), complex (-4, 44)])
        expected = complex(3181, 1005)
        productInt = mt.ProdcIntVc(v3, v4)
        np.testing.assert_almost_equal(productInt, expected)

    def test_normVect (self):
        v1 = np.array([complex(2, 3), complex(4, -1), complex(6, -5)])
        norma = mt.normVect(v1)
        self.assertAlmostEquals(norma, 9.53, places = 1)

        v2 = np.array([complex(1,-7), complex(0, 9), complex (-4, 4)])
        norma = mt.normVect(v2)
        self.assertAlmostEquals(norma, 12.76, places = 1)

    def test_DistVect (self):
        v1 = np.array([complex(2, 3), complex(4, -1), complex(6, -5)])
        v2 = np.array([complex(1,-7), complex(0, 9), complex (-4, 4)])
        distance = mt.DistVect(v1, v2)
        self.assertAlmostEquals(distance, 19.94, places = 1)

        v1 = np.array([complex(1, 3), complex(7, -1), complex(6, -9)])
        v2 = np.array([complex(6, -7), complex(1, 9), complex(-3, 0)])
        distance = mt.DistVect(v1, v2)
        self.assertAlmostEquals(distance, 20.56 ,places=1)

if __name__ == '__main__':
    unittest.main()