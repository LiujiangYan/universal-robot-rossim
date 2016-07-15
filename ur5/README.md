### XB06 ROS包

LIR3机器人，包括模型、动力学仿真等ROS package。


#### URDF文件：

一个link需要:  
>1.visual(几何) mesh文件,坐标定义,材质(颜色) ;   
>2.inertial惯量;  
>3.collision 用于碰撞检测。  
  
#### joint需指定其父连杆和子连杆
  
传动系统包括：  
>传动类型；
>关节对应的硬件接口类型；
>驱动器接口类型。


#### launch文件主要有  
>lir3_description/launch/trajectory_test.launch 用于实验轨迹规划算法  

>lir3_gazebo/launch/lir3_world.launch 使用gazebo和ros control进行动力学仿真  






#### vrep
LIR3_ros.ttt是vrep使用的仿真文件，可以接受ros的轴位置命令