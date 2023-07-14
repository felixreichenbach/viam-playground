from datetime import datetime
from dotenv import load_dotenv
import os
import asyncio
import pandas as pd

from viam.rpc.dial import Credentials, DialOptions
from viam.app.client import AppClient
from viam.app.data.client import DataClient, Filter
from viam.proto.app.data import CaptureInterval

"""
    .env file structure:
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

    # Upload binary data to the cloud to be available under Data/Files
    #with open('./media/sample_img.png', 'rb') as f:
    #    data = f.read()
    #await data_client.file_upload(part_id = 'eba0d362-aa1b-4572-83be-a25ae9e5cd65', component_type = None, component_name = None, method_name = None, method_parameters = None, file_extension = None, tags = None, file_name="sample", data=data)

    # Export Image metadata data as JSON structure to file
    data = await data_client.binary_data_by_filter(filter=Filter(component_name="Felix", interval=CaptureInterval(start=datetime.now(), end=datetime.now())), dest="./image_metadata.json")
    
    # Export sensors data as JSON structure to file
    #data = await data_client.tabular_data_by_filter(dest="./viam.json")

    # Load data into Pandas data frame 
    #data = await data_client.tabular_data_by_filter()
    #df = pd.DataFrame(data)
    #print(df)




if __name__ == '__main__':
    asyncio.run(main())
