from dotenv import load_dotenv
import os
import asyncio

from viam.rpc.dial import Credentials, DialOptions
from viam.app.client import AppClient
from viam.app.data.client import DataClient
from viam.proto.app.data import Filter

import viam

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
    
    # d = await data_client.tabular_data_by_filter(Filter())
    # print(f"data are! {d}")

    df = await data_client.tabular_data_by_filter(dest="./viam.json")
    print(df)

if __name__ == '__main__':
    asyncio.run(main())
