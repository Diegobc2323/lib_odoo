# -*- coding: utf-8 -*-
import random
import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Coches(models.Model):
    _name = 'coches.coches'
    _description = 'Coches'
    _rec_name = 'matricula'
    _order = 'matricula'

    matricula = fields.Char(string="Matricula", required=True)
    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Modelo", required=True)
    color = fields.Char(string="Color", required=True)
    precio = fields.Float(string="Precio", required=True)
    fecha_matriculacion = fields.Date(string="Fecha de matriculación")
    antiguedad = fields.Integer(string="Antiguedad")
    fecha_venta = fields.Date(string="Fecha de venta")
    comprador = fields.Many2one('coches.comprador', string="Comprador")
    vendedor = fields.Many2one('coches.vendedor', string="Vendedor")
    estado = fields.Selection([('disponible', 'Disponible'), ('vendido', 'Vendido')], string="Estado", default='disponible')

    #validate precio > 69
    @api.constrains('precio')
    def _check_precio(self):
        for record in self:
            if record.precio < 69:
                raise ValidationError("El precio tiene que ser mayor a 69 euros")
    #on change fecha matriculacion calcular antiguedad
    @api.onchange('fecha_matriculacion')
    def _onchange_fecha_matriculacion(self):
        if self.fecha_matriculacion:
            self.antiguedad = datetime.datetime.now().year - self.fecha_matriculacion.year



class comprador(models.Model):
    _name = 'coches.comprador'
    _description = 'Comprador'
    _rec_name = 'nombre'
    _order = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
    email = fields.Char(string="Email", required=True)
    

class vendedor(models.Model):
    _name = 'coches.vendedor'
    _description = 'Vendedor'
    _rec_name = 'nombre'
    _order = 'nombre'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
    email = fields.Char(string="Email", required=True)
   
