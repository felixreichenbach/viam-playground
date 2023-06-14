import config
import asyncio
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.board import Board
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

    print('Robot Started!')

    # Initialize the board and the LED on pin 8
    local = Board.from_robot(robot, 'local')
    led = await local.gpio_pin_by_name('8')

    # Create an infinite loop that will blink the LED on and off
    while (True):

        # grab camera from the robot
        webcam = Camera.from_robot(robot=robot, name='mac-main:camera')
        # grab Viam's vision service for the classifier
        my_classifier = VisionClient.from_robot(robot=robot, name='mac-main:vision_analysis')
        img = await webcam.get_image()
        classifications = await my_classifier.get_classifications(image=img, count=1)

        if classifications[0].class_name == 'felix' and classifications[0].confidence > 0.9:
            await led.set(True)
            print(f'Felix identified: {classifications[0].confidence}')
        else:
            await led.set(False)
            print(f'Felix not identified: {classifications[0].confidence}')

        await asyncio.sleep(1)

    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
