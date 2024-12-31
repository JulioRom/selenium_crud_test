from flask import render_template, request, redirect, url_for
from models import Item

def init_routes(app, db):
    @app.route('/')
    def index():
        items = Item.query.all()
        return render_template('index.html', items=items)

    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            new_item = Item(name=name, description=description)
            db.session.add(new_item)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('create.html')

    @app.route('/update/<int:item_id>', methods=['GET', 'POST'])
    def update(item_id):
        item = Item.query.get_or_404(item_id)
        if request.method == 'POST':
            item.name = request.form['name']
            item.description = request.form['description']
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('update.html', item=item)

    @app.route('/delete/<int:item_id>', methods=['POST'])
    def delete(item_id):
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('index'))
