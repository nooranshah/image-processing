from flask import Flask

import views

app = Flask(__name__)

# URL
app.add_url_rule('/index','index',views.base)
app.add_url_rule('/base','base',views.base)



#run
if __name__=='__main__':
    app.run(debug=True)