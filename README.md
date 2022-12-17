# odom_tf2
Данный модуль для ROS, проверенн и работает на симуляторе версии 0.3 в Ubuntu 18.04. Позволит вам на основе данных одонометрии с камеры Intel Realsense t265 координироваться при помощи стандартных пакетов [clover](https://github.com/CopterExpress/clover). 
## Установка
```bash
cd ~/catkin_ws/src
git clone https://github.com/Elur12/odom_tf2.git
```
В файл (clover.launch)[https://github.com/CopterExpress/clover/blob/master/clover/launch/clover.launch] добавьте строки
```bash
<node name="odom_tf2_broadcaster" pkg="odom_tf2" type="odom_tf2_broadcaster.py" respawn="false" output="screen"/>
```
## Сборка
```bash
cd ~/catkin_ws
catkin_make
sourse ~/.bashrc
```
## Настройка
Для настройки смещения камеры относительно центра дрона используте файл конфигурации(odom_tf2/nodes/config.py).
Укажите смещение по x, y, z камеры относительно центра дрона в переменные: OFFSET_X, OFFSET_Y, OFFSET_Z
## Использование
Пакет добавляет новый frame_id. Если указать "odom_map" в параметр frame_id. То позиционирование дрона будет осуществляться на основе топика /camera/odom/sample. 
##Примеры использования
1. В коде
```bash
import rospy
from clover import srv

navigate = rospy.ServiceProxy('navigate', srv.Navigate)

navigate(x=2, y=1, z=1.5, frame_id='odom_map', auto_arm=True)
```

2. Через консоль
```bash
rosservice call /navigate "{x: 1.5, y: 1.7, z: 1.0, yaw: 0.0, yaw_rate: 0.0, speed: 0.0, frame_id: 'odom_map', auto_arm: true}" 
```
