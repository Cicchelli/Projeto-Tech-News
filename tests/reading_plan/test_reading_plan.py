from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest
from unittest.mock import Mock, patch


news_all = [
    {"title": "Python", "reading_time": 4},
    {"title": "Pytest", "reading_time": 3},
    {"title": "Parsel", "reading_time": 10},
    {"title": "Beautiful Soup", "reading_time": 15},
]

result_expected = {
    "readable": [
        {"unfilled_time": 3, "chosen_news": [("Python", 4), ("Pytest", 3)]},
        {"unfilled_time": 0, "chosen_news": [("Parsel", 10)]},
    ],
    "unreadable": [("Beautiful Soup", 15)],
}


def test_reading_plan_group_news():
    find_news_mock = Mock(return_value=news_all)

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
            find_news_mock):
        result = ReadingPlanService.group_news_for_available_time(10)
        assert result == result_expected
