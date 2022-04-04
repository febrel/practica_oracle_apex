
from werkzeug.exceptions import abort # Cuando intente hacer un registro que no le pertenece
from db import get_db
from auth import login_required
from flask import (Blueprint, flash, g, render_template, request, url_for, session, redirect)
from datetime import datetime

# Todas las funciones con todas las rutas esta va ser la ruta /todo

bp = Blueprint('todo', __name__)

@bp.route('/contenido')
@login_required
def contenido():
    # Buscar a base datos, todos los todo que el ha realizado
    db, c = get_db()
    # Es muy importante el orden para el index

    c.execute("SELECT r.day, r.time, u.usuario, r.ubicacion FROM usuarios u, registros r WHERE r.id_usuarios = u.id AND r.id_usuarios = %s",(g.user[0],))
    todos = c.fetchall()

    return render_template("registros.html", todos= todos)



@bp.route('/marcar')
@login_required
def marcar():
    # Buscar a base datos, todos los todo que el ha realizado
    db, c = get_db()
    # Es muy importante el orden para el index


    fecha = datetime.today().strftime('%Y-%m-%d')
    hora = datetime.today().strftime('%H:%M:%S')

    c.execute('INSERT INTO registros (day, time, ubicacion, id_usuarios ) VALUES (%s, %s, %s, %s)' , (fecha, hora, 'Oficina', g.user[0]))
    db.commit()

    return redirect(url_for("todo.contenido"))