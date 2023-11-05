CREATE OR REPLACE STAGE your_stage_name
URL='azure://<storage-account-name>.blob.core.windows.net/<container-name>'
CREDENTIALS=(AZURE_SAS_TOKEN='<your-sas-token>');



COPY INTO your_target_table
FROM @your_stage_name/file_prefix  -- if your files have a prefix, otherwise just use the stage name
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1);
