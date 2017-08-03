import re
import unittest


def filter_comment_by_regex(comment):
    patron1 = r'\b[bB]icis?[a-zA-Z ]* plegables?'
    patron2 = r'\b[tT]ern'
    patron3 = r'\b[bB]rompton'

    if re.search(patron1, comment) or re.search(patron2, comment) or re.search(patron3, comment):
        return True
    else:
        return False


class FilterRegexTest(unittest.TestCase):

    def test_bici_plegable_es_true(self):
        resultado_obtenido = filter_comment_by_regex('Bici plegable')
        self.assertTrue(resultado_obtenido)

    def test_zanahoria_es_false(self):
        resultado_obtenido = filter_comment_by_regex('zanahoria')
        self.assertFalse(resultado_obtenido)

    def test_bicis_plegables_es_true(self):
        resultado_obtenido = filter_comment_by_regex('Bicis plegables')
        self.assertTrue(resultado_obtenido)

    def test_bici_plegable_minusculas_es_true(self):
        resultado_obtenido = filter_comment_by_regex('bici plegable')
        self.assertTrue(resultado_obtenido)

    def test_tern_es_true(self):
        resultado_obtenido = filter_comment_by_regex('Tern')
        self.assertTrue(resultado_obtenido)

    # def test_ternera_es_false(self):
    #     resultado_obtenido = filter_comment_by_regex('ternera')
    #     self.assertFalse(resultado_obtenido)
