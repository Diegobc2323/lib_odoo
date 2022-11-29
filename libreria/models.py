import random
from odoo import models, fields, api
from odoo.exceptions import ValidationError

import time
from datetime import datetime

#create autor model
class Autor(models.Model):
    _name = 'libreria.autor'
    _description = 'Modelo de autor'

    name = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    fecha_fallecimiento = fields.Date(string="Fecha de fallecimiento")
    nacionalidad = fields.Char(string="Nacionalidad", required=True)
    libros = fields.One2many('libreria.libro', 'autor', string="Libros")
    edad = fields.Integer(string="Edad")
 
    
    @api.onchange('fecha_nacimiento')
    def _onchange_fecha_nacimiento(self):
        if self.fecha_nacimiento:
            self.edad = datetime.now().year - self.fecha_nacimiento.year
    
    @api.onchange('fecha_fallecimiento')
    def _onchange_fecha_fallecimiento(self):
        if self.fecha_fallecimiento:
            self.edad = self.fecha_fallecimiento.year - self.fecha_nacimiento.year
    
#create libro model
class Libro(models.Model):
    _name = 'libreria.libro'
    _description = 'Modelo de libro'

    titulo = fields.Char(string="Titulo", required=True)
    autor = fields.Many2one('libreria.autor', string="Autor")
    fecha_publicacion = fields.Date(string="Fecha de publicacion", required=True)
    editorial = fields.Char(string="Editorial", required=True)
    precio = fields.Float(string="Precio", required=True)

    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.precio < 5:
                raise ValidationError("El precio tiene que ser mayor a 5 euros")
    
#create lector model
class Lector(models.Model):
    _name = 'libreria.lector'
    _description = 'Modelo de lector'

    name = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    nacionalidad = fields.Char(string="Nacionalidad", required=True)
    libros = fields.Many2many('libreria.libro', string="Libros")

