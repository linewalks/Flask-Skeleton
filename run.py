from main import app
import sys
if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=sys.argv[1])
