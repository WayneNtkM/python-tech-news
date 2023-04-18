import pytest
from unittest.mock import patch
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501


PATH = "tech_news.analyzer.reading_plan"


@pytest.fixture
def expected():
    return {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    (
                        "Py tá on",
                        4,
                    ),
                    (
                        "Selenium, BeautifulSoup ou Parsel?",
                        3,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "Pytest + Faker == tristeza",
                        10,
                    )
                ],
            },
        ],
        "unreadable": [
            ("SlowAPI e Estus Flask", 15),
            ("Pandas fast food", 12),
        ],
    }


def mock():
    return [
        {"title":  "Py tá on", "reading_time": 4},
        {"title": "Selenium, BeautifulSoup ou Parsel?", "reading_time": 3},
        {
            "title": "Pytest + Faker == tristeza",
            "reading_time": 10,
        },
        {
            "title": "SlowAPI e Estus Flask",
            "reading_time": 15,
        },
        {
            "title": "Pandas fast food",
            "reading_time": 12,
        },
    ]


@patch(f"{PATH}.ReadingPlanService._db_news_proxy",
       mock)
def test_reading_plan_group_news(expected):
    result = ReadingPlanService().group_news_for_available_time(10)
    assert result == expected

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)
