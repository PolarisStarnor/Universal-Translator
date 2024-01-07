import unittest
import text_cleanup

class TestCleanupTest(unittest.TestCase):

    def test_cleanup_repetitions(self):
        text_to_clean = "this is a test recording this is a test recording this is a test recording this is a test recording this is a test recording"
        cleaned = text_cleanup.eliminate_repetitions(text_to_clean)

        self.determine_validity(cleaned, text_to_clean)

    def test_cleanup_unconcise(self):
        text_to_clean = "this is a strange statement whereby I say the same thing multiple times" \
                        "since I am bad at making things concise and I need to record a message and make" \
                        "multiple statements that say the same things. This is just a strange statement" \
                        "that requires problems that I don't know how to solve"
        cleaned = text_cleanup.eliminate_repetitions(text_to_clean)

        self.determine_validity(cleaned, text_to_clean)

    def determine_validity(self, cleaned, text_to_clean):
        cleaned_text = ''
        for item in cleaned:
            cleaned_text += item

        print("Cleaned text: " + cleaned_text)

        self.assertIsNotNone(cleaned_text)
        self.assertNotEqual(cleaned_text, "")

        self.assertLessEqual(len(cleaned_text), len(text_to_clean))


if __name__ == '__main__':
    unittest.main()
