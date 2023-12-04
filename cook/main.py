from cook.app import create_app
from cook.config.setup import setup_app

app = create_app()
app = setup_app(app)
