from codrone_edu.drone import Drone

drone = Drone()

drone.pair()

drone.takeoff()
# ドローンを5秒間ホバリングさせる
drone.hover(5)
drone.land()

drone.close()
