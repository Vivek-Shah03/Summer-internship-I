from odoo import fields, models


class ReturnBook(models.Model):
    _name = 'return.book'
    # _rec_name = ''

    returned_books = fields.Many2many('borrow.book', 'books', string="Member")
    is_returned = fields.Boolean("Returned")
