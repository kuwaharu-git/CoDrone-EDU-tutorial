# CoDrone-EDU Pythonプログラムチュートリアル

## ⚠️ **注意事項**

> **1. 安全性について**  
> このチュートリアルを実行する際は、周囲に危険がないことを確認し、十分なスペースを確保してからドローンを飛行させてください。狭い室内や障害物が多い場所での飛行は、ドローンや周囲の人・物に損傷を与える可能性があります。特に人がいる場所では、ドローンの飛行に十分な注意を払い、安全第一で操作してください。
>
> **2. 動作保証について**  
> このチュートリアルで紹介しているプログラムは、特定の環境や設定に基づいて動作確認を行ったものですが、すべての環境での動作を保証するものではありません。ソフトウェアやハードウェアの構成によっては、正しく動作しない場合があります。プログラムの使用によるいかなる損害や問題についても、作成者は一切の責任を負いかねますのでご了承ください。
>
> **3. 自己責任での利用**  
> このチュートリアルを使用する場合、ユーザーは自己の責任において実行してください。ドローンの操作やプログラムの実行によって発生した損害や障害について、作成者は責任を負いません。

---

## 公式ドキュメント
* [Function-Documentation](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation)
* [公式チュートリアル](https://learn.robolink.com/course/python-with-codrone-edu/)


## 1. CoDrone-EUDライブラリのインストール

※pythonがインストールされているのが前提です(ver.3.12以上だと動作しないので3.11以下のpythonが必要です)

依存ライブラリがあるため、できれば仮想環境を作成してインストールすることを推奨します

```bash
pip install codrone-edu 
```

## 2. ドローン、コントローラーのセッティング
まず、コントローラーとPCをUSBで接続します。この際、コントローラーに電池は入れないでください。
ドローン本体に充電済みのバッテーリーを入れると自動的に接続されます。もし接続されない場合は[こちら](https://youtu.be/kMJhf5ykLSo)の動画を参考にペアリングを行ってください。

接続ができたらコントローラーの画面に「LINK」と表示されていることを確認します。もし表示されていない場合は、フライト状態になっているので電源ボタンを一度押して切り替えます。

## 3. 操作プログラム

### 1. 離陸、着陸
※飛行させる際には周囲に気をつけてください。

このプログラムを実行すると、離陸してその後着陸します。

[01_take_off.py](./tutorial/01_take_off.py)

```python
# CoDrone EDUライブラリからDroneクラスをインポート
from codrone_edu.drone import Drone

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

```

### 2. ホバー
このプログラムを実行すると離陸し、その後5秒その場でとどまりその後着陸します。

[02_hover.py](./tutorial/02_hover.py)

```python
from codrone_edu.drone import Drone

drone = Drone()

drone.pair()

drone.takeoff()
# ドローンを5秒間ホバリングさせる
drone.hover(5)
drone.land()

drone.close()

```

## 移動
### 移動する際の主な手順
1. 飛行変数を設定する(移動の方向とパワーの設定)
    * 前後: [set_pitch()](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation#set_pitch)
    * 左右: [set_roll()](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation#set_roll)
    * 上下: [set_throttle()](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation#set_throttle)
    * 向きの変更: [set_yaw()](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation#set_yaw)
2. 移動コマンドの実行(飛行変数を元に何秒動くかどうか)
    * 移動コマンド: [move()](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation#move)

    ※ 飛行変数はmove()実行後も設定した値は変わらないため、次に違う動きをしたい場合は、0に設定し直す必要がある

この方法以外に、あらかじめどのように動くか設定されている関数があります

例
* ドローンを円状に飛行: [circle()](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation/#circle)
* ドローンを四角形の形状で飛行: [square()](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation/#square)
など

他にもいくつかあるので[公式ドキュメントの飛行コマンド](https://docs.robolink.com/docs/CoDroneEDU/Python/Function-Documentation/#flight-commands-movement)のところを参考に使えそうなものを探してみてください

## 前に移動する例

[0303_move_forward.py](./tutorial/03_move_forward.py)

※前に移動するため、実行する際はドローン前方に、障害物、人がいないことを確認し、設置する向きに注意してください。

※飛行変数の値をいきなり大きすぎる値にすると速度がですぎて壁などに衝突する危険があるので初めは小さい値で徐々にあげてどれくらいの速度が出るのか試してみましょう。

実行後、コンソールに今何をしているのかが表示されるのでそれも合わせて確認してみてください。

```python
from codrone_edu.drone import Drone


"""
ドローンを前進させる例
"""

drone = Drone()

drone.pair()

print
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

```

前後左右、上下、回転も同じようにできます。ドキュメントを見ながら前進以外のコードも作成して実行してみてください。

それぞれの方向の移動ができるようになったら今度は四角形に沿って移動、斜めに移動などをどのように飛行変数を設定すれば実現できるか考えて実行してみてください。