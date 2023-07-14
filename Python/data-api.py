from datetime import datetime
from dotenv import load_dotenv
import os
import sys
import asyncio
import pandas as pd

from viam.rpc.dial import Credentials, DialOptions
from viam.app.client import AppClient
from viam.app.data.client import DataClient, Filter
from viam.proto.app.data import CaptureInterval


from google.protobuf.timestamp_pb2 import Timestamp

"""
    Credentials are imported through a .env file with the following structure:
    ADDRESS=robot.organisation.viam.cloud
    SECRET=yoursecret
"""
load_dotenv()


async def main():
    address = os.getenv('ADDRESS')
    creds = Credentials(
        type="robot-location-secret",
        payload=os.getenv('SECRET')
    )
    dial_opts = DialOptions(
        credentials=creds,
        auth_entity=address,
    )
    app: AppClient = await AppClient.create(dial_opts)
    data_client: DataClient = app.data_client

    # Configure Time Interval
    date_start = int(datetime(2023, 5, 23, 14, 45, 29).timestamp()) # past
    date_end = int(datetime(2023, 5, 23, 14, 45, 30).timestamp()) # more recent

    if date_start > date_end:
        print("Verify interval! date_start must be before date_end!")
        sys.exit()

    print("// Selected Interval")
    print(f"Start: {datetime.fromtimestamp(date_start)}")
    print(f"Start: {datetime.fromtimestamp(date_end)}")

    # Upload binary data to the cloud to be available under Data/Files in the Viam app
    # with open('./media/sample_img.png', 'rb') as f:
    #    data = f.read()
    # await data_client.file_upload(part_id = 'eba0d362-aa1b-4572-83be-a25ae9e5cd65', component_type = None, component_name = None, method_name = None, method_parameters = None, file_extension = None, tags = None, file_name="sample", data=data)

    # Export Image metadata data as JSON structure to file
    # data = await data_client.binary_data_by_filter(filter=Filter(component_name="mac-pro-legacy", interval=CaptureInterval(start=Timestamp(seconds=date_start), end=Timestamp(seconds=date_end))), dest="./image_metadata.json")
    data = await data_client.binary_data_by_filter(filter=Filter(component_name="camera", interval=CaptureInterval(start=Timestamp(seconds=date_start), end=Timestamp(seconds=date_end))), dest="./image_metadata.json")

    # Export sensors data as JSON structure to file
    # data = await data_client.tabular_data_by_filter(filter=Filter(component_name="accelerometer", interval=CaptureInterval(start=Timestamp(seconds=date_start), end=Timestamp(seconds=date_end))), dest="./sensor.json")
    data = await data_client.tabular_data_by_filter(filter=Filter(component_name="accelerometer"), dest="./sensor.json")

    # Load data into Pandas data frame
    # data = await data_client.tabular_data_by_filter()
    # df = pd.DataFrame(data)
    # print(df)


if __name__ == '__main__':
    asyncio.run(main())
