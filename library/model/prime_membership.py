from odoo import fields, models, api


class PrimeMembership(models.Model):
    _name = 'prime.membership'
    _rec_name = 'member'
    member = fields.Many2one('library.managment', string='Member')
    phone = fields.Char(string="Phone No", required=True)
    address = fields.Text(string="Address")
    receptionist = fields.Char(string="Receptionist", default="Mr.Shah")
    payment_done = fields.Boolean(string="Payment", default=True)
    is_prime_member = fields.Boolean(string="Prime Member", help="If you purchased Prime Membership or not?",
                                     default=True)

    @api.onchange('member')
    def onchange_member(self):
        self.phone = self.member.phone
        self.address = self.member.address
