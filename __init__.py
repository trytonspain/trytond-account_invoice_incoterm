# This file is part account_invoice_incoterm module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import invoice
from . import sale


def register():
    Pool.register(
        invoice.Invoice,
        module='account_invoice_incoterm', type_='model')
    Pool.register(
        sale.Sale,
        depends=['sale_incoterm'],
        module='pyme', type_='model')
