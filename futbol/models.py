import random
from odoo import models, fields, api
from odoo.exceptions import ValidationError

import time
from datetime import datetime


class Jugador(models.Model):
    _name = 'futbol.jugador'
    _description = 'Jugador'
    
    name = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    edad = fields.Integer(string="Edad", required=True)
    posicion = fields.Selection([('portero', 'Portero'), ('defensa', 'Defensa'), ('centrocampista', 'Centrocampista'), ('delantero', 'Delantero')], string="Posicion", required=True)
    equipo = fields.Many2one('futbol.equipo', string="Equipo", required=True)
    dorsal = fields.Integer(string="Dorsal", required=True)


class Equipo(models.Model):
    _name = 'futbol.equipo'
    _description = 'Equipo'

    name = fields.Char(string="Nombre", required=True)
    ciudad = fields.Char(string="Ciudad", required=True)
    estadio = fields.Char(string="Estadio", required=True)
    jugadores = fields.One2many('futbol.jugador', 'equipo', string="Jugadores")
    entrenadores = fields.Many2many('futbol.entrenador', 'equipo', string="Entrenadores")



class Entrenador(models.Model):
    _name = 'futbol.entrenador'
    _description = 'Entrenador'

    name = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    edad = fields.Integer(string="Edad", required=True)
    equipo = fields.Many2many('futbol.equipo', string="Equipo", required=True)
    fecha_inicio = fields.Date(string="Fecha de inicio", required=True)
    fecha_fin = fields.Date(string="Fecha de fin", required=True)
