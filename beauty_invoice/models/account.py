from odoo import fields, models, api, _
from odoo.addons.beauty_invoice import numero_a_texto

class AccountInvoice(models.Model):
    _inherit = "account.move"


    def get_amount_in_word(self):
        return str(numero_a_texto.Numero_a_Texto(self.amount_total))

