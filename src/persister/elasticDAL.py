from elasticsearch import Elasticsearch, helpers
from elasticsearch.exceptions import NotFoundError
import os


class ElasticDAL:
    def __init__(self,index_name="podcasts"):
        HOST = os.getenv("ES_HOST", "http://localhost:9200")
        self.index_name = index_name
        self.request_timeout = 20
        self.verify_certs = True
        self.es = Elasticsearch(
            hosts=HOST,
            request_timeout=self.request_timeout,
            verify_certs=self.verify_certs
        )

    def map_index(self,report_map:dict):
        mapping = dict()
        mapping["mappings"] = dict()
        try:
            mapping["mappings"]["properties"] = report_map
            self.es.indices.create(
                index=self.index_name,
                body=mapping,
                ignore=400
            )
            print(f"Index '{self.index_name}' created successfully with mapping.")
        except Exception as e:
            print(f"Error creating index: {e}")


    def insert_data(self,report):
        self.es.index(
            index=self.index_name,
            id=report["_id"],
            body=report
        )
        print(f"Indexed {report["_id"]} report.")
