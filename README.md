# Video Parsing Service

音视频处理服务

## 安装

1. 克隆仓库：

```bash
git clone https://github.com/falconluca/video-parsing-srv.git
cd video-parsing-srv
```

2. 创建并激活虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用

运行应用程序：

```bash
python main.py
```

上传视频文件，提取音频和封面：

```bash
curl -X POST -F "file=@/path/to/your/video.mp4" http://localhost:8000/upload
```