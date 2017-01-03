# -*- coding: utf-8 -*-
from openerp import models, fields, api
class psicotecnico(models.Model):
	_name = 'tms.psicotecnico'
	name = fields.Char('Nombre', required=True)
	date_release = fields.Date('Fecha')
	chofer =  fields.Many2one('hr.employee')

class viajes(models.Model):
        _name = 'tms.viajes'

	@api.one
	def to_progress(self):
		self.estado = 'progress'


        name = fields.Char('Nombre', required=True)
        date_release = fields.Date('Fecha')
        chofer =  fields.Many2one('hr.employee')
        vehiculo = fields.Many2one('fleet.vehicle')
        estado = fields.Selection(selection=[('draft','Borrador'),('progress','En Progreso'),('done','Finalizado')],default='draft')


class ruta(models.Model):
        _name = 'tms.ruta'

	dominio = fields.Many2one('fleet.vehicle')
	date_release = fields.Date('Fecha de Emision')
	date_end = fields.Date('Fecha de Vencimiento')
	chofer =  fields.Many2one('hr.employee')        
	name = fields.Char('Expedido', required=True)
	comments = fields.Char('Observaciones', required=True)
 
 
