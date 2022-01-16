from distutils.log import debug
from flask import Flask

import view

app = Flask(__name__)



#url
app.add_url_rule('/','index',view.index,methods=['GET','POST'])

#run 
if __name__ == "__main__":
    app.run(debug=True)