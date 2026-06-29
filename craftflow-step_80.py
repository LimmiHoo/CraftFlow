# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: CraftFlow
class MessagePolisher:
    def __init__(self):
        self._messages = {
            "welcome": "Добро пожаловать в CraftFlow! Отслеживайте материалы, этапы и вдохновение.",
            "error_missing_field": "Ошибка: поле '{field}' не заполнено. Пожалуйста, проверьте данные.",
            "success_added": "Успешно добавлено!",
            "info_no_projects": "Список проектов пуст. Создайте первый проект для начала работы."
        }

    def get_message(self, key: str) -> str:
        return self._messages.get(key, f"Неизвестное сообщение: {key}")

    def format_project_name(self, name: str) -> str:
        return name.strip().title() if name else "Без названия"

    def generate_example_entry(self):
        return """# Пример добавления проекта в CraftFlow
from craftflow import Project

p = Project(
    name="Керамическая ваза",
    materials=["Глина", "Глазурь"],
    milestones=["Обжиг 1", "Покрытие", "Финальная обжиг"],
    cost=500.0,
    notes="Вдохновлено работами Ричарда Глея."
)"""

if __name__ == "__main__":
    polisher = MessagePolisher()
    print(polisher.get_message("welcome"))
