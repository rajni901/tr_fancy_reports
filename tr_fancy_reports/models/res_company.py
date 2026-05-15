from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    report_header_color = fields.Char(
        string='Report Header Color',
        default='#1a1a5e',
    )
    report_accent_color = fields.Char(
        string='Report Accent Color',
        default='#6c3fc5',
    )
    report_footer_text = fields.Text(
        string='Report Footer Text',
        default='Thank you for your business!',
    )
    report_show_bank_details = fields.Boolean(
        string='Show Bank Details on Reports',
        default=True,
    )
    report_show_payment_terms = fields.Boolean(
        string='Show Payment Terms',
        default=True,
    )
    report_tagline = fields.Char(
        string='Report Tagline',
        default='Solutions | Automation | Innovation',
    )
