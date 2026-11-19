from src.app import create_app

def test_create_app():
    app = create_app()
    assert app is not None
    assert app.config["TESTING"] is False  # ou True dependendo do config
    assert len(app.url_map._rules) > 0
