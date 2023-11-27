from app_logger.logger import APP_LOGGER
import os


class extract_article_text:
    def __init__(self,text):
        self.input_text=text
        self.fileObject=open("Log_Files_Collection/Prediction_Logs/Result_Log.txt","a+")
        self.log=APP_LOGGER()


    def load_user_data(self):
        try:
            self.log.log(self.fileObject,'Extracting the text from article')
            
        except Exception as e:
            self.log.log(self.fileObject,e)
            raise e