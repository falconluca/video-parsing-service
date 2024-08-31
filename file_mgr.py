import os
import uuid

class FileManager:
    """
    处理文件管理的类：负责文件的保存、路径生成和检查等操作。
    """
    def __init__(self, upload_folder='uploads', audio_folder='audio', cover_folder='covers'):
        self.upload_folder = upload_folder
        self.audio_folder = audio_folder
        self.cover_folder = cover_folder
        self._ensure_directories()

    def _ensure_directories(self):
        """确保文件夹存在"""
        os.makedirs(self.upload_folder, exist_ok=True)
        os.makedirs(self.audio_folder, exist_ok=True)
        os.makedirs(self.cover_folder, exist_ok=True)

    def save_file(self, file):
        """保存上传的文件并生成唯一的文件名"""
        unique_filename = f"{uuid.uuid4().hex}_{file.filename}"
        input_file_path = os.path.join(self.upload_folder, unique_filename)
        file.save(input_file_path)
        return input_file_path, unique_filename

    def get_output_paths(self, unique_filename):
        """生成音频和封面文件的输出路径"""
        audio_file_path = os.path.join(self.audio_folder, f"{unique_filename}.mp3")
        cover_file_path = os.path.join(self.cover_folder, f"{unique_filename}.jpg")
        return audio_file_path, cover_file_path
