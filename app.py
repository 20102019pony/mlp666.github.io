from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def video_page():
    # 视频文件列表，与前端顺序对应
    videos = ['1.mp4', '2.mp4', '3.mp4', '4.mp4']
    return render_template('video.html', videos=videos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
