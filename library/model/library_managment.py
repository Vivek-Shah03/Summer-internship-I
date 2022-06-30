from odoo import fields, api, models
from odoo.exceptions import ValidationError


class LibraryManagment(models.Model):
    _name = 'library.managment'
    _rec_name = 'name'
    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone No", required=True)
    receptionist = fields.Many2one('receptionist.data', string="Receptionist")
    address = fields.Text(string="Address")
    photo = fields.Image(string="Photograph")
    desc = fields.Html(string="Description")
    status = fields.Selection(
        [('draft', 'Draft'), ('submit', 'Submit'), ('cancel', 'Cancel')], default='draft')

    @api.constrains('phone')
    def phone_validate(self):
        if len(self.phone) != 10:
            raise ValidationError("Phone Number Must Be Of 10 Digits!")
        else:
            if not self.phone.isnumeric():
                raise ValidationError("Phone Number Must contain only Digits!")

    def submit_action(self):
        self.status = "submit"

    def action_cancel(self):
        self.status = 'cancel'

    def draft_action(self):
        self.status = 'draft'


class Receptionist(models.Model):
    _name = 'receptionist.data'
    _rec_name = 'receptionist'

    receptionist = fields.Char("Receptionist")
