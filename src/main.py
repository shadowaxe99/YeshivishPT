```python
from flask import Flask, request, jsonify
from translation_engine import translate
from dictionary import searchDictionary
from voice_recognition import recognizeVoice
from pronunciation_guide import guidePronunciation
from lessons import provideLesson
from cultural_insights import provideCulturalInsight

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def handle_translation():
    data = request.get_json()
    result = translate(data['text'])
    return jsonify({'result': result})

@app.route('/dictionary', methods=['GET'])
def handle_dictionary():
    word = request.args.get('word')
    result = searchDictionary(word)
    return jsonify({'result': result})

@app.route('/voice_recognition', methods=['POST'])
def handle_voice_recognition():
    data = request.get_json()
    result = recognizeVoice(data['voice_data'])
    return jsonify({'result': result})

@app.route('/pronunciation_guide', methods=['GET'])
def handle_pronunciation_guide():
    word = request.args.get('word')
    result = guidePronunciation(word)
    return jsonify({'result': result})

@app.route('/lessons', methods=['GET'])
def handle_lessons():
    lesson_id = request.args.get('lesson_id')
    result = provideLesson(lesson_id)
    return jsonify({'result': result})

@app.route('/cultural_insights', methods=['GET'])
def handle_cultural_insights():
    insight_id = request.args.get('insight_id')
    result = provideCulturalInsight(insight_id)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
```