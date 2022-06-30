from odoo import fields, models


class BookData(models.Model):
    _name = 'book.data'
    _rec_name = 'book_name'
    book_name = fields.Char(string="Book Name")
    book_type = fields.Selection([('sci', 'Science'), ('comm', 'Commerce'), ('art', 'Arts')])


class Books(models.Model):
    _name = 'books.list'
    books_data = fields.Many2one('book.data', string="Book List")
    books = fields.Many2one('borrow.book', string="Book")
