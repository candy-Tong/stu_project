# coding=utf-8
from app import app
# from flow import flow_manager
from views import views

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)