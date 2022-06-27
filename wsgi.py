from app import app
import os

if __name__ == '__main__':
    app.run(debug=False,
    port = int(os.environ.get('PORT', 33507))
)
