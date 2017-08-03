import re
import unittest


def filter_comment_by_regex(comment):
    patrones = [r'\b[bB]icis?[a-zA-Z ]* plegables?', r'\b[tT]ern', r'\b[bB]rompton']
    resultado = False

    for patron in patrones:
        if re.search(patron, comment):
            resultado = True
            break

    return resultado


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
