from flask import Flask
from exts import db,mail
from blueprints import user_bp,list_bp
import config
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
migrate=Migrate(app,db)

app.register_blueprint(user_bp)
app.register_blueprint(list_bp)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


