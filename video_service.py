from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
from gevent import spawn, joinall
from file_mgr import FileManager
from video_processor import VideoProcessor


class VideoService:
    """
    Flask 服务类：处理请求和异步任务。
    """

    def __init__(self):
        self.app = Flask(__name__)
        self.file_manager = FileManager()
        self._setup_routes()

    def _setup_routes(self):
        """设置 Flask 路由"""

        @self.app.route("/upload", methods=["POST"])
        def upload_video():
            return self.handle_upload()

    def handle_upload(self):
        """处理上传请求并异步提取音频和封面"""
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        # 保存上传文件并生成唯一文件名
        input_file_path, unique_filename = self.file_manager.save_file(file)
        audio_file_path, cover_file_path = self.file_manager.get_output_paths(
            unique_filename
        )

        # 使用 gevent 异步执行 ffmpeg 提取音频和封面
        audio_operation = spawn(
            VideoProcessor.extract_audio, input_file_path, audio_file_path
        )
        cover_operation = spawn(
            VideoProcessor.extract_cover, input_file_path, cover_file_path
        )
        joinall([audio_operation, cover_operation])  # 等待所有的协程完成

        return jsonify(
            {
                "audio_message": audio_operation.value,
                "cover_message": cover_operation.value,
                "audio_file": audio_file_path,
                "cover_file": cover_file_path,
            }
        )

    def run(self):
        """运行 Flask 应用程序"""
        http_server = WSGIServer(("0.0.0.0", 8000), self.app)
        print("Server is running on http://0.0.0.0:8000")
        http_server.serve_forever()
