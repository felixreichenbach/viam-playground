import config
import asyncio
import time
from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from pygame import mixer, time


def play_sound():
    print('sound')
    mixer.init()
    sound = mixer.Sound('./Python/media/example_MP3_700KB.mp3')
    channel = sound.play()
    while channel.get_busy():
        time.wait(100)  # ms
        print('playing...')
    print('finished')

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

    play_sound()

    # Don't forget to close the robot when you're done!
    await robot.close()

if __name__ == '__main__':
    asyncio.run(main())
