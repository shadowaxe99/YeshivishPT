```python
from typing import List, Dict

class Lesson:
    def __init__(self, title: str, content: str, quiz: Dict[str, str]):
        self.title = title
        self.content = content
        self.quiz = quiz

class LessonModel:
    def __init__(self):
        self.lessons = []

    def add_lesson(self, title: str, content: str, quiz: Dict[str, str]):
        lesson = Lesson(title, content, quiz)
        self.lessons.append(lesson)

    def get_lesson(self, title: str) -> Lesson:
        for lesson in self.lessons:
            if lesson.title == title:
                return lesson
        return None

    def get_all_lessons(self) -> List[Lesson]:
        return self.lessons

lesson_model = LessonModel()
```