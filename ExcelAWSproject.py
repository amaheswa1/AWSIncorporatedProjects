import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError

AWS_ACCESS_KEY = 'your_access_key'
AWS_SECRET_KEY = 'your_secret_key'
BUCKET_NAME = 'your_bucket_name'

def download_s3_file(file_name, bucket):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    try:
        s3.download_file(bucket, file_name, file_name)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def sort_excel_sheet_by_name(file_name):
    # Load spreadsheet
    xl = pd.ExcelFile(file_name)

    # Load a sheet into a DataFrame by its name
    sheet_names = sorted(xl.sheet_names)

    with pd.ExcelWriter(file_name) as writer:
        for sheet in sheet_names:
            df = xl.parse(sheet)
            df.to_excel(writer, sheet_name=sheet)

def main():
    file_name = '/Users/adharshmaheswaran/TwitterAWSproject/test1.xlsx'
    #if download_s3_file(file_name, BUCKET_NAME):
    sort_excel_sheet_by_name(file_name)
    print(f'{file_name} has been sorted by sheet names')

if __name__ == '__main__':
    main()
