@app.route('/about')
def about():
    return render_template('index.html', title='About',
                           content='This is the About page')