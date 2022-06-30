from odoo import fields, models
import datetime


class BorrowBook(models.Model):
    _name = 'borrow.book'
    _rec_name = 'members'
    members = fields.Many2one('library.managment', string='Member', domain=[('status', '=', 'submit')])
    receptionist = fields.Char(string="Receptionist", default="Mr.Shah")
    books = fields.One2many('books.list','books', string="Books")
    borrowing_date = fields.Date(string="Borrowing Date", default=datetime.date.today())
    last_day = fields.Date(string="Last Date To Return", default=datetime.date.today() + datetime.timedelta(days=10))
