from codrone_edu.drone import Drone
import time

"""
ドローンの下部の距離センサーの値を取得する例
"""

drone = Drone()
drone.pair()

print(
    "ドローンの下部の距離センサーの値を取得します。ドローンを持って上下に動かしてみてください。"
)
# ドローンの下部の距離センサーの値を1秒間隔で10回取得
for i in range(10):
    # ドローンの下部の距離センサーの値を取得
    bottom_range = drone.get_bottom_range()
    print(bottom_range)
    time.sleep(1)

drone.close()
