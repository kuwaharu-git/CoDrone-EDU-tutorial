from codrone_edu.drone import Drone


"""
ドローンを前進させる例
"""

drone = Drone()

drone.pair()

print("離陸")
drone.takeoff()
print("1秒間ホバリング")
drone.hover(1)
# ドローンを前進させる
print("ピッチ変数を30に設定します")
drone.set_pitch(30)  # ピッチ変数の値を30に設定
print("3秒間前進")
drone.move(3)  # 3秒間前進
print("1秒間ホバリング")
drone.hover(1)
print("再度3秒間前進")
drone.move(3)  # 再度3秒間前進
drone.hover(1)
print("ピッチ変数を0に設定します")
drone.set_pitch(0)  # ピッチ変数の値を0に設定
print("3秒間ホバリング")
drone.move(3)  # 今度は動かない(3秒間ホバリング)
drone.land()

drone.close()
