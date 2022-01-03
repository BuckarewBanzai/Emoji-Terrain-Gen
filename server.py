import os
import random
import string
import gardener
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    seed = ''.join(random.choice(string.ascii_lowercase) for x in range(64))
    return redirect(url_for('garden', seed=seed))


@app.route('/<string:seed>')
def garden(seed):
    plot = gardener.drawpath(seed)
    return plot


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
