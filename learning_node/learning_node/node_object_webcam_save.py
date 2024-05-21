#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

"""
@作者: 古月居(www.guyuehome.com)
@说明: ROS2节点示例-通过摄像头识别检测图片中出现的苹果
"""

# import rclpy                            # ROS2 Python接口库
# from rclpy.node import Node             # ROS2 节点类

# import cv2                              # OpenCV图像处理库
# import numpy as np                      # Python数值计算库


# def main(args=None):                                                       # ROS2节点主入口main函数
#     rclpy.init(args=args)                                                  # ROS2 Python接口初始化
#     node = Node("node_object_webcam")                                      # 创建ROS2节点对象并进行初始化
#     node.get_logger().info("保存当前图像")

#     cap = cv2.VideoCapture(0)
#     image_count = 0

    
#     while rclpy.ok():
#         ret, image = cap.read()          # 读取一帧图像
         
#         if ret == True:
#             # object_detect(image)          # 苹果检测
#              image_filename = f"image_{image_count}.jpg"
#              cv2.imwrite(image_filename, cap)
#              node.get_logger().info(f"Saved image as {image_filename}")
#              image_count += 1
        
        
#     node.destroy_node()                  # 销毁节点对象
#     rclpy.shutdown()                     # 关闭ROS2 Python接口
import rclpy
from rclpy.node import Node
import cv2

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.capture = cv2.VideoCapture(0)  # Open the default camera (usually the first one)
        self.image_count = 0

    def save_image(self):
        ret, frame = self.capture.read()
        if ret:
            # 设置图片保存路径和名称
            image_filename = "/home/sxy/dev_ws/src/ros2_21_tutorials/learning_node/" + f"image_{self.image_count}.jpg"
            # 保存图片
            cv2.imwrite(image_filename, frame)
            self.get_logger().info(f"Saved image as {image_filename}")
            self.image_count += 1
        else:
            self.get_logger().error("Failed to capture image")
        # 展示正在采集的图像
        show_name = '正在拍摄图片,共计5张,当前第' + f"{self.image_count}" + '张'
        cv2.imshow(show_name, frame)
        # 设置imshow的持续时间
        cv2.waitKey(1000)
        # 时间到后关闭窗口
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()
    
    # 拍摄5张图片,可根据需求更改
    set_capture_count = 5

    while rclpy.ok():
            
            for i in range(set_capture_count):           
                camera_node.save_image()
                # rclpy.spin_once(camera_node)   # 若使用回调函数则启用这一行代码
            camera_node.destroy_node()
            rclpy.shutdown()

if __name__ == '__main__':
    main()