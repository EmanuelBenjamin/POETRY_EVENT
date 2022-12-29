from  flask import Flask
from config import config
import route


app = Flask(__name__)

def page_not_found(error):
    return ('Page Not Found'), 404

if __name__ == '__main__':
    app.config.from_object(config['development'])



app.register_blueprint(route.contestant_main,url_prefix = '/inscription')
app.register_blueprint(route.contestantList_main, url_prefix ='/list' )


app.register_error_handler(404, page_not_found)
app.run()

