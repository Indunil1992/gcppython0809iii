import numpy as np
from google.cloud import storage

def handler(request):

    array = np.array([
    [3, 7, 1],
    [10, 3, 2],
    [5, 6, 7]
    ])
    print(np.sort(array, axis=None))

    # def list_blobs(bucket_name):
    # """Lists all the blobs in the bucket."""
    bucket_name = "indu-storage-m3"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)


    return "Successfully executed 1234"
