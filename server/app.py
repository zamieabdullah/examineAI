from flask import Flask
from flask_cors import CORS
from models.model import db
import os

# importing environment variables 
from dotenv import load_dotenv
load_dotenv()

# importing models
from models.users import User

# importing routes
from controllers.users import bp as user_routes


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Configure PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" \
                                        f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
db.init_app(app)

# Create the database tables (if they don't exist)
with app.app_context():
    db.create_all()


# Register the routes blueprint
app.register_blueprint(user_routes)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    app.run()