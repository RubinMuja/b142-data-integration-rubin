# B142 Final Project – COVID-19 Big Data Integration

**Student**: Rubin Muja  
**Student ID**: GH1027906  
**Course**: B142 Data Integration  
**University**: Gisma University of Applied Sciences  

---

## 📁 GitHub Repo  
https://github.com/RubinMuja/b142-data-integration-rubin

## Video Demo  
https://drive.google.com/drive/folders/0B-sQ2EjvYkeQfkZIWTYxazh5N3V6QURaZ2NTdDZyV3QtdXRxZ1M5a1BENVhjYzRxMEhZSEk?resourcekey=0-rMlEQ25hRCvngjvk-r9AyA&usp=sharing
---

## Dataset

Dataset: [Google COVID-19 Open Data](https://github.com/GoogleCloudPlatform/covid-19-open-data)  
Direct file used: [epidemiology.csv](https://storage.googleapis.com/covid19-open-data/v3/epidemiology.csv)

 **Note:** Due to GitHub's 100MB limit, the dataset is not included in this repo.  
Please download and place it in the `data/` folder manually before running the pipeline.

---

##️ How to Run the Spark Pipeline

1. Download the dataset above and save it as:  
   `data/epidemiology.csv`

2. Run the Spark script:
```bash
spark-submit spark_jobs/etl_pipeline.py

