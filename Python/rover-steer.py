import config
import asyncio
import time

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.base import Base



async def connect():
    creds = Credentials(
        type='robot-location-secret',
        payload=config.secret)
    opts = RobotClient.Options(
        refresh_interval=0,
        dial_options=DialOptions(credentials=creds,disable_webrtc=True, auth_entity=config.address)
    )
    #return await RobotClient.at_address(config.address, opts)
    return await RobotClient.at_address('192.168.1.123:8080', opts)


async def main():
    robot = await connect()
    
    my_base = Base.from_robot(robot=robot, name="viam_base")

    # Spin the base 10 degrees at an angular velocity of 1 deg/sec.
    await my_base.spin(angle=-90, velocity=100)

    # Move the base 10 mm at a velocity of 1 mm/s, forward.
    my_base.move_straight(distance=500, velocity=50)

    while my_base.is_moving:
        print("Is moving")
        time.sleep(0.5)
    
    print("Stopped moving")


    # Move the base 10 mm at a velocity of -1 mm/s, backward.
    #await my_base.move_straight(distance=10, velocity=-1)
    

    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
