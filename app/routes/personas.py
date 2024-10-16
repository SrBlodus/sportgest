# app/routes/personas.py
from flask import Blueprint, render_template, redirect, flash, request, url_for
from app import db
from app.models.persona import Persona
from app.models.tipo_persona import TipoPersona  # Importa el modelo TipoPersona
from app.models.tipo_documento import TipoDocumento  # Importa el modelo TipoDocumento
from app.models.sexo import Sexo  # Importa el modelo Sexo
from app.models.nacionalidad import Nacionalidad  # Importa el modelo Nacionalidad
from app.models.estado_civil import EstadoCivil  # Importa el modelo EstadoCivil
from app.decorators import role_required  # Importa el decorador

bp = Blueprint('personas', __name__)


@bp.route('/personas', methods=['GET'])
@role_required(['admin', 'operador'])  # Solo los roles admin y operador pueden acceder
def listar_personas():
    personas = Persona.query.all()
    return render_template('personas/listar.html', personas=personas)


@bp.route('/personas/agregar', methods=['GET', 'POST'])
@role_required(['admin', 'operador'])  # Solo los roles admin y operador pueden acceder
def agregar_persona():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        barrio = request.form['barrio']
        numero_documento = request.form['numero_documento']
        tipo_documento_id = request.form['tipo_documento']
        sexo_id = request.form['sexo']
        nacionalidad_id = request.form['nacionalidad']
        estado_civil_id = request.form['estado_civil']
        telefono = request.form['telefono']
        fecha_nacimiento = request.form['fecha_nacimiento']
        tipos_seleccionados = request.form.getlist('tipos')  # Obtener tipos de persona seleccionados

        # Verificar si el correo ya existe
        if Persona.query.filter_by(correo=correo).first():
            flash('El correo ya está en uso. Por favor, usa otro correo.')
            return render_template('personas/agregar.html',
                                   tipos_documento=TipoDocumento.query.all(),
                                   sexos=Sexo.query.all(),
                                   nacionalidades=Nacionalidad.query.all(),
                                   estados_civiles=EstadoCivil.query.all(),
                                   tipos=TipoPersona.query.all(),
                                   nombre=nombre,
                                   apellidos=apellidos,
                                   correo=correo,
                                   direccion=direccion,
                                   ciudad=ciudad,
                                   barrio=barrio,
                                   numero_documento=numero_documento,
                                   tipo_documento=tipo_documento_id,
                                   sexo=sexo_id,
                                   nacionalidad=nacionalidad_id,
                                   estado_civil=estado_civil_id,
                                   telefono=telefono,
                                   fecha_nacimiento=fecha_nacimiento,
                                   tipos_seleccionados=[int(t) for t in tipos_seleccionados])

        # Verificar si el número de documento ya existe
        if Persona.query.filter_by(numero_documento=numero_documento).first():
            flash('El número de documento ya está en uso. Por favor, usa otro número de documento.')
            return render_template('personas/agregar.html',
                                   tipos_documento=TipoDocumento.query.all(),
                                   sexos=Sexo.query.all(),
                                   nacionalidades=Nacionalidad.query.all(),
                                   estados_civiles=EstadoCivil.query.all(),
                                   tipos=TipoPersona.query.all(),
                                   nombre=nombre,
                                   apellidos=apellidos,
                                   correo=correo,
                                   direccion=direccion,
                                   ciudad=ciudad,
                                   barrio=barrio,
                                   numero_documento=numero_documento,
                                   tipo_documento=tipo_documento_id,
                                   sexo=sexo_id,
                                   nacionalidad=nacionalidad_id,
                                   estado_civil=estado_civil_id,
                                   telefono=telefono,
                                   fecha_nacimiento=fecha_nacimiento,
                                   tipos_seleccionados=[int(t) for t in tipos_seleccionados])

        nueva_persona = Persona(
            nombre=nombre,
            apellidos=apellidos,
            correo=correo,
            direccion=direccion,
            ciudad=ciudad,
            barrio=barrio,
            numero_documento=numero_documento,
            tipo_documento_id=tipo_documento_id,
            sexo_id=sexo_id,
            nacionalidad_id=nacionalidad_id,
            estado_civil_id=estado_civil_id,
            telefono=telefono,
            fecha_nacimiento=fecha_nacimiento
        )

        db.session.add(nueva_persona)
        db.session.commit()

        # Manejar la relación con los tipos de persona
        for tipo_id in tipos_seleccionados:
            tipo_persona = TipoPersona.query.get(tipo_id)
            nueva_persona.tipos.append(tipo_persona)

        db.session.commit()
        flash('Persona agregada con éxito.')
        return redirect(url_for('personas.listar_personas'))

    # Si es un GET request, obtener las opciones para los desplegables
    return render_template('personas/agregar.html',
                           tipos_documento=TipoDocumento.query.all(),
                           sexos=Sexo.query.all(),
                           nacionalidades=Nacionalidad.query.all(),
                           estados_civiles=EstadoCivil.query.all(),
                           tipos=TipoPersona.query.all(),
                           tipos_seleccionados=[])


@bp.route('/personas/editar/<int:id>', methods=['GET', 'POST'])
@role_required(['admin', 'operador'])  # Solo los roles admin y operador pueden acceder
def editar_persona(id):
    persona = Persona.query.get_or_404(id)

    if request.method == 'POST':
        # Obtener el correo del formulario
        nuevo_correo = request.form['correo']

        # Verificar si el nuevo correo ya está en uso por otra persona (excluyendo la persona actual)
        correo_existente = Persona.query.filter(Persona.correo == nuevo_correo, Persona.id != id).first()
        if correo_existente:
            flash('El correo ya está en uso por otra persona.', 'error')
            return render_template('personas/editar.html', persona=persona,
                                   tipos_documento=TipoDocumento.query.all(),
                                   sexos=Sexo.query.all(),
                                   nacionalidades=Nacionalidad.query.all(),
                                   estados_civiles=EstadoCivil.query.all(),
                                   tipos=TipoPersona.query.all())  # Re-renderizar con los valores actuales

        # Actualizar los campos de la persona
        persona.nombre = request.form['nombre']
        persona.apellidos = request.form['apellidos']
        persona.direccion = request.form['direccion']
        persona.telefono = request.form['telefono']
        persona.ciudad = request.form['ciudad']
        persona.barrio = request.form['barrio']
        persona.numero_documento = request.form['numero_documento']
        persona.tipo_documento_id = request.form['tipo_documento']  # Actualizar el tipo de documento
        persona.sexo_id = request.form['sexo']  # Actualizar el sexo
        persona.nacionalidad_id = request.form['nacionalidad']  # Actualizar la nacionalidad
        persona.estado_civil_id = request.form['estado_civil']  # Actualizar el estado civil
        persona.fecha_nacimiento = request.form['fecha_nacimiento']  # Actualizar la fecha de nacimiento

        # Actualizar tipos de persona
        persona.tipos.clear()  # Limpia los tipos actuales
        tipos_seleccionados = request.form.getlist('tipos')  # Obtiene los tipos seleccionados
        for tipo_id in tipos_seleccionados:
            tipo_persona = TipoPersona.query.get(tipo_id)
            persona.tipos.append(tipo_persona)  # Suponiendo que tienes la relación configurada

        db.session.commit()
        flash('Persona actualizada con éxito.')
        return redirect(url_for('personas.listar_personas'))

    # Obtener las opciones para los desplegables
    tipos_documento = TipoDocumento.query.all()
    sexos = Sexo.query.all()
    nacionalidades = Nacionalidad.query.all()
    estados_civiles = EstadoCivil.query.all()
    tipos = TipoPersona.query.all()  # Obtener todos los tipos de persona para el formulario

    return render_template(
        'personas/editar.html',
        persona=persona,
        tipos_documento=tipos_documento,
        sexos=sexos,
        nacionalidades=nacionalidades,
        estados_civiles=estados_civiles,
        tipos=tipos  # Pasa todos los tipos de persona
    )


@bp.route('/personas/eliminar/<int:id>', methods=['POST'])
@role_required(['admin', 'operador'])  # Solo los roles admin y operador pueden acceder
def eliminar_persona(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    flash('Persona eliminada con éxito.')
    return redirect(url_for('personas.listar_personas'))
