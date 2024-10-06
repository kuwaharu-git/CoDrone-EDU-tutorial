# CoDrone EDUライブラリからDroneクラスをインポート
from codrone_edu.drone import Drone


"""
ドローンを離陸させる
"""

# ドローンのインスタンスを作成
drone = Drone()

# ドローンとペアリングを行う
drone.pair()

# ドローンを離陸させる
drone.takeoff()

# ドローンを着陸させる
drone.land()

# ドローンとの接続を閉じる
drone.close()
