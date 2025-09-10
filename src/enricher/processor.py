from nltk.sentiment.vader import SentimentIntensityAnalyzer
from src.utils.file_IO import FileIO
from src.utils.logger import Logger

# logger setup
logger = Logger.get_logger(index="enricher_log",name="enricher.processor.py")


class Processor:
    hostile_words = None
    less_hostile_words = None

    def __init__(self):
        try:
            hostile_data = FileIO.import_json("../../data/hostile_words.json")
            self.hostile_words = hostile_data["hostile"]
            self.less_hostile_words = hostile_data["less_hostile"]
            logger.info(f'Processor.init, hostile_data received.')
        except Exception as e:
            msg = f"error: {e}"
            logger.error(f"Processor.init, {msg}")
            raise Exception(msg)

    def run(self,text:str,word_count:int):
        bds_stats = {}
        #count hostile word appearance
        hostile_word_count = self.detected_hostile_words(text,self.hostile_words)
        less_hostile_word_count = self.detected_hostile_words(text,self.less_hostile_words)
        sum_points = less_hostile_word_count + (hostile_word_count * 2)
        # get text sentiment
        sentiment = self.sentiment_detector(text)
        # calculate BDS based on hostile word appearance and sentiment
        bds_stats["bds_percent"] = self.calc_bds_percent(sum_points, word_count, sentiment)
        bds_stats["is_bds"] = self.calc_is_bds(bds_stats["bds_percent"])
        bds_stats["bds_threat_level"] = self.calc_threat_level(bds_stats["bds_percent"])
        logger.info(f'Processor.run, Calculation process complete.')
        return bds_stats

    @staticmethod
    def detected_hostile_words(text,hostile_words_list):
        word_counts = {}
        normalized_text = text.lower()
        for hostile_word in hostile_words_list:
            normalized_bad_word = hostile_word.lower()
            count = normalized_text.count(normalized_bad_word)
            if count > 0:
                word_counts[hostile_word] = count
        return sum(word_counts.values())

    @staticmethod
    def calc_bds_percent(sum_points,text_len,sentiment):
        score = (sum_points/text_len) * sentiment
        if score > 100:
            return 100
        elif score < 0:
            return 0
        else:
            return int(score)

    @staticmethod
    def calc_is_bds(percent:float):
        if percent > 35:
            return True
        return False

    @staticmethod
    def calc_threat_level(percent:float):
        if percent <= 10:
            return "none"
        elif percent <= 35:
            return "medium"
        return "high"

    @staticmethod
    def sentiment_detector(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        if score['compound'] > 0.5:
            return 100 #positive
        if score['compound'] < -0.5:
            return score['compound'] * -1000 #negativ
        else:
            return 200 #nutral