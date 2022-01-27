import pdfplumber
import os 
import pandas as pd
import shutil

from datetime import datetime

### Get PDF path information
class PdfSet:

    def __init__(self, folder_path):
        self.path = folder_path
        self.pdf = [_ for _ in os.listdir(self.path) if _.endswith(".pdf")]
        self.pdf_files =  [os.path.join(self.path ,_) for _ in self.pdf]
    
    def get(self):
        return self.path, self.pdf, self.pdf_files

class Parser:
    
    @staticmethod
    def abroad():
        
        # set pdf path
        pdf_set = PdfSet(r'D:\git\covid19\pdf\境外')
        pdf_path, pdf, pdf_files = pdf_set.get()

        # get data
        doc = pdfplumber.open(pdf_files[0])
        for i in range(len(doc.pages)):
            if i == 0:
                p = doc.pages[i]
                df = p.extract_table()[1:]
            else:
                p = doc.pages[i]
                tmp = p.extract_table()[1:]
                df.extend(tmp)
    
        doc.close()
        # establish df
        df = pd.DataFrame(df, columns=['序號', '案號', '入境日/旅遊迄日', '國籍', '性別', '年齡', '旅遊國家', '確診日', '長程落地採檢','備註'])
        df.drop(['備註'],inplace=True,axis=1)
        update_date = datetime.now().strftime('%Y/%m/%d')
        save_date = datetime.now().strftime('%Y_%m_%d')
        df['update_date'] = update_date

        # save csv
        df.to_csv(r'D:\git\covid19\csv\abroad'+'\\'+save_date+'.csv', index = False)
        shutil.rmtree(pdf_path)
        os.mkdir(pdf_path)
    
    @staticmethod
    def local():
        
        # set pdf path
        pdf_set = PdfSet(r'D:\git\covid19\pdf\本土')
        pdf_path, pdf, pdf_files = pdf_set.get()

        # date = [
        #     '2022/01/09','2022/01/10','2022/01/11',
        #     '2022/01/12','2022/01/13','2022/01/14',
        #     '2022/01/15','2022/01/16','2022/01/17',
        # ]

        # for item, d in zip(pdf_files, date):
        for item in pdf_files:
            # get data
            doc = pdfplumber.open(item)
            for i in range(len(doc.pages)):
                if i == 0:
                    p = doc.pages[i]
                    df = p.extract_table()[1:]
                else:
                    p = doc.pages[i]
                    tmp = p.extract_table()[1:]
                    df.extend(tmp)
    
            doc.close()

            # establish df
            df = pd.DataFrame(df, columns=['序號','案號','國籍','地區','性別','年齡','是否為突破性感染','COVID-19疫苗接種','發病日','症狀','採檢日','確診日','採檢途徑','備註'])
            update_date = datetime.now().strftime('%Y/%m/%d')
            # save_date = d.replace("/","_")
            save_date = datetime.now().strftime('%Y_%m_%d')
            # df['update_date'] = d
            df['update_date'] = update_date

            # save csv
            df.to_csv(r'D:\git\covid19\csv\local'+'\\'+save_date+'.csv', index = False)
        
        shutil.rmtree(pdf_path)
        os.mkdir(pdf_path)