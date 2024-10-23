from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        result_1 = emotion_detector('I am glad this happened') # test case for 'joy' emotion
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        result_2 = emotion_detector('I am really mad about this') # test case for 'anger' emotion
        self.assertEqual(result_2['dominant_emotion'], 'anger')
       
        result_3 = emotion_detector('I feel disgusted just hearing about this') # test case for 'disgust' emotion
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = emotion_detector('I am so sad about this') # test case for 'sadness' emotion
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = emotion_detector('I am really afraid that this will happen') # test case for 'fear' emotion
        self.assertEqual(result_5['dominant_emotion'], 'fear')


unittest.main()