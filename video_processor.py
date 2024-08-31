import ffmpeg

class VideoProcessor:
    """
    处理视频的类：负责提取音频和封面。
    """
    @staticmethod
    def extract_audio(input_file_path, output_file_path):
        """使用 ffmpeg 提取音频"""
        try:
            ffmpeg.input(input_file_path).output(output_file_path, **{'q:a': 0, 'map': 'a'}).run()
            return "Audio extraction successful!"
        except Exception as e:
            return str(e)

    @staticmethod
    def extract_cover(input_file_path, output_file_path):
        """使用 ffmpeg 提取封面"""
        try:
            ffmpeg.input(input_file_path).output(output_file_path, vframes=1).run()
            return "Cover extraction successful!"
        except Exception as e:
            return str(e)