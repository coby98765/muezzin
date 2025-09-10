from fastapi import FastAPI
from elasticDAL import ElasticDAL

app = FastAPI()
es = ElasticDAL()

@app.get('/all')
def get_all():
    try:
        res = es.get_all()
        return res
    except Exception as ex:
        print(ex)
        raise Exception(ex)

@app.get('/is_bds')
def is_bds():
    try:
        res = es.get_is_bds()
        return res
    except Exception as ex:
        print(ex)
        raise Exception(ex)

@app.get('/threat_level/{level}')
def threat_level(level:str):
    try:
        res = es.get_threat_level(level)
        return res
    except Exception as ex:
        print(ex)
        raise Exception(ex)

@app.get('/search/')
def threat_level(query:str):
    try:
        res = es.search(query)
        return res
    except Exception as ex:
        print(ex)
        raise Exception(ex)