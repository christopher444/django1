from google.cloud import bigquery

# Construct a BigQuery client object.
def func1():
    client = bigquery.Client('project1-264909')

    # TODO(developer): Set table_id to the ID of table to append to.
    # table_id = "your-project.your_dataset.your_table"
    columns = ["account_code","account_name","campaign_code","currency","cost","conversions","impressions","clicks","account_timezone","network_type","timestamp"]
    rows_to_insert = []
    with open("/home/ubuntu/django1/scripts/file.csv") as file:
        for line in file:
           la =  line.strip().split(',')
     
           x = 0
           d  = {}
           for c in columns:
               d[c] = la[x]
         
               x = x + 1 
           d["revenueperconversion"] = "250.00"
           rows_to_insert.append(d)
    #print(rows_to_insert)
    table_id = "project1-264909.dataset1.GoogleAds"
    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    if errors == []:
        return("New rows have been added.")
    else:
        return("Encountered errors while inserting rows: {}".format(errors))

if __name__ == "__main__":
    print(func1)        