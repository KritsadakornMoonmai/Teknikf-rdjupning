import Config
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Config.create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)