import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        tests = [
            ('I am glad this happened', 'joy'),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid that this will happen', 'fear')
        ]
        for input_text, expected in tests:
            result = emotion_detector(input_text)
            self.assertEqual(result['dominant_emotion'], expected)

if __name__ == '__main__':
    unittest.main()