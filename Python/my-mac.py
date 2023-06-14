import config
import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.camera import Camera
from viam.services.vision import VisionClient


async def connect():
    creds = Credentials(
        type='robot-location-secret',
        payload=config.secret)
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds)
    )
    return await RobotClient.at_address(config.address, opts)


async def main():
    robot = await connect()

    print('Resources:')
    print(robot.resource_names)

    # camera
    camera = Camera.from_robot(robot, "camera")
    camera_return_value = await camera.get_image()
    print(f"camera get_image return value: {camera_return_value}")
    camera_return_value.save("camera_image.jpg")

    # camera_mlmodel
    camera_mlmodel = Camera.from_robot(robot, "camera_mlmodel")
    camera_mlmodel_return_value = await camera_mlmodel.get_image()
    print(f"camera_mlmodel get_image return value: {camera_mlmodel_return_value}")
    camera_mlmodel_return_value.save("ml_image.jpg")

    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
