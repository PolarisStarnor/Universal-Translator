import unittest
import translation

class TestTranslation(unittest.TestCase):

    def test_translate_fr_en(self):
        from_text = "bonjour, c'est samedi"
        to_text = "hello, it's saturday"

        from_lang = "fr"
        to_lang = "en"

        trans = translation.translate(from_text, from_lang, to_lang)

        print(trans)
        self.assertEqual(trans.lower(), to_text.lower())
