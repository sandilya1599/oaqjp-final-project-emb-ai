import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def testEmotion(self):
        dominant_emotion = emotion_detector('I am glad this happened')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'joy')

        dominant_emotion = emotion_detector('I am really mad about this')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'anger')

        dominant_emotion = emotion_detector('I feel disgusted just hearing about this')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'disgust')

        dominant_emotion = emotion_detector('I am so sad about this')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'sadness')

        dominant_emotion = emotion_detector('I am really afraid that this will happen')['dominant_emotion']
        self.assertEqual(dominant_emotion, 'fear')

if __name__ == "__main__":
    unittest.main()