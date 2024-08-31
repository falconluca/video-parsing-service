from gevent import monkey
from video_service import VideoService

# 使用 monkey patch 使标准库的 I/O 操作变为非阻塞
monkey.patch_all()

if __name__ == '__main__':
    # 创建并运行视频服务
    video_service = VideoService()
    video_service.run()