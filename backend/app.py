from flask import Flask
from routes import init_routes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/crud_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

init_routes(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
