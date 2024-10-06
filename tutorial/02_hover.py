from codrone_edu.drone import Drone


"""
ドローンを離陸させ、5秒間ホバリングさせた後、着陸させる
"""

drone = Drone()

drone.pair()

drone.takeoff()
# ドローンを5秒間ホバリングさせる
drone.hover(5)
drone.land()

drone.close()
