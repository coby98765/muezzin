from src.utils.logger import Logger
import uvicorn
import routs
import os


# logger setup
logger = Logger.get_logger(index="api_log",name="api.main.py")


app = routs.app

API_PORT = int(os.getenv("API_PORT",8000))

if __name__ == "__main__":
    logger.info('API, Starting server...')
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)