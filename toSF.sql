use database azure;
CREATE FILE FORMAT my_csv_format
TYPE = 'CSV'
FIELD_DELIMITER = ','
SKIP_HEADER = 1;



CREATE STORAGE INTEGRATION azure_integration
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = AZURE
ENABLED = TRUE
AZURE_TENANT_ID = 'c87f340c-7713-40bf-a595-'
STORAGE_ALLOWED_LOCATIONS = ('azure://projectolympics.blob.core.windows.net/github1');

DROP STAGE MY_EXTERNAL_STAGE;

CREATE STAGE my_external_stage
URL = 'azure://projectolympics.blob.core.windows.net/github1'
STORAGE_INTEGRATION = azure_integration
CREDENTIALS = (AZURE_SAS_TOKEN = '?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2023-12-09T13:41:37Z&st=2023-11-12T05:41:37Z&spr=https&sig=0ScB31i%2B4qpVPdpJtanPcoPyiDRjlPEc70Xgs2Cq8p8%3D');


CREATE STAGE my_external_stage
URL = 'azure://.blob.core.windows.net/github1'
CREDENTIALS = (AZURE_SAS_TOKEN = '?sv=2022-11-02&ss=bfqt&srt=sco&s05:41:37Z&spr=https&sig=0ScB31i%2B4qpVPdpJtanPcoPyiDRjlPEc70Xgs2Cq8p8%3D');

drop table my_reddit_data
CREATE TABLE my_reddit_data (
    title VARCHAR(500),
    selftext VARCHAR(8000), 
    created_utc TIMESTAMP_NTZ,
    upvotes INT,
    url VARCHAR(1000)
);

COPY INTO my_reddit_data
FROM @MY_EXTERNAL_STAGE/data_20231112_163403.csv
FILE_FORMAT = (FORMAT_NAME = my_csv_format)
ON_ERROR = CONTINUE;

SHOW FILE FORMATS;

CREATE FILE FORMAT MY_CSV_FORMAT
    TYPE = 'CSV'
    FIELD_DELIMITER = ','
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    EMPTY_FIELD_AS_NULL = TRUE
    TRIM_SPACE = TRUE;



