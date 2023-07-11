import asyncio

from .src.api import Foo

from viam import logging
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions


async def connect():
    creds = Credentials(type="robot-location-secret",
                        payload="<ROBOT_LOCATION_SECRET>")
    opts = RobotClient.Options(refresh_interval=0, dial_options=DialOptions(
        credentials=creds), log_level=logging.DEBUG)
    return await RobotClient.at_address("<ROBOT_ADDRESS>", opts)


async def main():
    robot = await connect()

    print("Resources:")
    print(robot.resource_names)

    foo = Foo.from_robot(robot, name="foo1")
    resp = await foo.set_state(True)
    print("do_one result:", resp)

    await robot.close()


if __name__ == "__main__":
    asyncio.run(main())
