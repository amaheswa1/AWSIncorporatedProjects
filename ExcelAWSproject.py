import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials and bucket information
AWS_ACCESS_KEY = 'your_access_key'
AWS_SECRET_KEY = 'your_secret_key'
BUCKET_NAME = 'your_bucket_name'

def download_s3_file(file_name, bucket):
    """
    Downloads a file from an Amazon S3 bucket using the provided credentials.

    Parameters:
        file_name (str): The name of the file to be downloaded.
        bucket (str): The name of the S3 bucket.

    Returns:
        bool: True if download is successful, False otherwise.
    """
    # Create an S3 client with provided credentials
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
    try:
        # Download the file from the bucket and save with the same name
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
    """
    Sorts the sheets in an Excel file alphabetically by their sheet names.

    Parameters:
        file_name (str): The name of the Excel file to be sorted.
    """
    # Load the Excel file
    xl = pd.ExcelFile(file_name)

    # Get the names of the sheets and sort them alphabetically
    sheet_names = sorted(xl.sheet_names)

    # Create a new Excel file to save the sorted sheets
    with pd.ExcelWriter(file_name) as writer:
        for sheet in sheet_names:
            # Read the sheet into a DataFrame
            df = xl.parse(sheet)
            # Save the DataFrame to the new Excel file with the sorted sheet name
            df.to_excel(writer, sheet_name=sheet)

def main():
    file_name = '/Users/adharshmaheswaran/TwitterAWSproject/test1.xlsx'
    # Uncomment the following lines if you want to download the file from S3 before sorting
    # if download_s3_file(file_name, BUCKET_NAME):
    # Call the function to sort the Excel file's sheets
    sort_excel_sheet_by_name(file_name)
    print(f'{file_name} has been sorted by sheet names')

if __name__ == '__main__':
    main()
