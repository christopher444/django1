Step1 and Step2:

django-admin startproject django1

cd django1

python manage.py startapp app1

Add app1 to setttings.py


Edit models.py and admin.py under the app1 folder 

SELECT * FROM `bigquery-public-data.samples.shakespeare` a where a.corpus_date > 0 and a.corpus = 'hamlet' order by word_count desc limit 100

export to TableA in bigquery console itself

SELECT * FROM `project1-264909.dataset1.TableA`

export as CSV

COPY app1_tablea(word, word_count, corpus,corpus_date)
FROM '/home/ubuntu/bq.csv'
DELIMITER ','
CSV HEADER;

Step 3:
GoogleAds Table in BQ

column_name,data_type
account_code,STRING(255)
account_name,STRING(255)
campaign_code,STRING(255)
currency,STRING(255)
cost,FLOAT64
conversions,INT64
impressions,INT64
clicks,INT64
account_timezone,STRING(255)
network_type,STRING(255)
timestamp,TIMESTAMP
revenueperconversion,FLOAT64
CPC,FLOAT64
CPA,FLOAT64
ROAS,FLOAT64

Please see scripts/two.py for python script to load the table from the sample csv data

After that

UPDATE tablename set CPC =  clicks/cost 
UPDATE tablename set CPA =  conversions/cost
UDPATE tablename set ROAS = (revenueperconversion * conversions)/cost

Step 4:

