from flask import Flask

def create_app():
  app = Flask(__name__)
  app.config['SECRETE KEY'] = '#S^/>!#te^'
  
  return app