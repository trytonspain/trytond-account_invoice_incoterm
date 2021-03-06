# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Bool, Eval

__all__ = ['Invoice']


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'
    incoterm = fields.Many2One('incoterm', 'Incoterm',
        states={
            'readonly': Eval('state') != 'draft',
            },
        depends=['state'])
    incoterm_place = fields.Char('Incoterm Name Place',
        states={
            'required': Bool(Eval('incoterm')),
            'invisible': ~Bool(Eval('incoterm')),
            'readonly': Eval('state') != 'draft',
            },
        depends=['state', 'incoterm'])

    @fields.depends('party')
    def on_change_party(self):
        super(Invoice, self).on_change_party()

        self.incoterm = None
        self.incoterm_place = None
        if self.party:
            self.incoterm = self.party.incoterm \
                if self.party.incoterm else None
            self.incoterm_place = self.party.incoterm_place \
                if self.party.incoterm_place else None
