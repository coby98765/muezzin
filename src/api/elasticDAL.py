from elasticsearch import Elasticsearch, helpers
from src.utils.logger import Logger
import os

# logger setup
logger = Logger.get_logger(index="api_log",name="api.elasticDAL.py")

class ElasticDAL:
    def __init__(self,index_name="podcasts"):
        HOST = os.getenv("ES_HOST", "http://localhost:9200")
        self.index_name = index_name
        self.request_timeout = 20
        self.verify_certs = True
        try:
            self.es = Elasticsearch(
                hosts=HOST,
                request_timeout=self.request_timeout,
                verify_certs=self.verify_certs
            )
            logger.info(f'ElasticDAL.init, connected to ElasticSearch.')
        except Exception as e:
            logger.error(f"ElasticDAL.init, Error: {e}")


    def get_all(self):
        try:
            query_body = {
                "query": {
                    "match_all": {}
                }
            }
            response = self.es.search(
                index=self.index_name,
                body=query_body)
            logger.info(f'ElasticDAL.get_all, got all.')
            clean_res = self.res_cleaner(response["hits"]["hits"])
            return clean_res
        except Exception as e:
            logger.error(f"ElasticDAL.get_all, Error: {e}")

    def get_is_bds(self):
        try:
            query_body = {
                "query": {
                    "match": {
                        "is_bds": True
                    }
                }
            }
            response = self.es.search(
                index=self.index_name,
                body=query_body)
            logger.info(f'ElasticDAL.get_is_bds, got "is_bds".')
            clean_res = self.res_cleaner(response["hits"]["hits"])
            return clean_res
        except Exception as e:
            logger.error(f"ElasticDAL.get_is_bds, Error: {e}")

    def get_threat_level(self,level):
        try:
            query_body = {
                "query": {
                    "term": {
                        "bds_threat_level": level
                    }
                }
            }
            response = self.es.search(
                index=self.index_name,
                body=query_body)
            logger.info(f'ElasticDAL.get_threat_level, got "bds_threat_level"={level}.')
            clean_res = self.res_cleaner(response["hits"]["hits"])
            return clean_res
        except Exception as e:
            logger.error(f"ElasticDAL.get_threat_level, Error: {e}")

    def search(self,text):
        try:
            query_body = {
                "query": {
                    "match": {
                        "transcript": text
                    }
                }
            }
            response = self.es.search(
                index=self.index_name,
                body=query_body)
            logger.info(f'ElasticDAL.get_all, searched for: "{text}" in transcripts.')
            clean_res = self.res_cleaner(response["hits"]["hits"])
            return clean_res
        except Exception as e:
            logger.error(f"ElasticDAL.insert_data, Error: {e}")

    @staticmethod
    def res_cleaner(res):
        try:
            clean_res = {}
            for r in res:
                clean_res[r["_id"]] = r["_source"]
                return clean_res
        except Exception as e:
            logger.error(f"ElasticDAL.res_cleaner, Error: {e}")
            raise