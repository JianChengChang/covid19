# covid19
此 Side Project 是練習將 Covid 19 確診數據視覺化<br>
詳細疫情資訊還請參照衛服部  https://www.cdc.gov.tw/?aspxerrorpath=/ <br>
<br>
### 世界疫情資訊
資料來源來自 John Hopkins<br>
因有時差問題<br>
此資料來源在亞洲並非即時資訊<br>

### 台灣疫情資訊
資料來源來自衛服部每日公告的PDF檔<br>
PDF檔需手動下載到 pdf 資料夾內<br>
pdf資料夾內又分為「境外」與「本土」<br>
用來區分PDF檔<br>

pdf資料夾中有一個pdf_parser.py<br>
能將境外本土內的pdf檔轉成csv檔並放在csv資料夾的abroad與local中<br>
此為Power BI的資料來源