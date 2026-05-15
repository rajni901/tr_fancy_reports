{
    'name': 'Fancy PDF Reports',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Beautiful, professional PDF reports for Invoice, Sale, Purchase & Delivery',
    'description': """
Fancy PDF Reports — by Technical Rajni
=======================================
Replaces default Odoo PDF layouts with modern, branded designs.

Features:
- Professional Invoice PDF
- Stylish Sales Quotation / Order PDF
- Clean Purchase Order PDF
- Delivery Order PDF
- Company logo, colors, and footer configurable per company
- Works for both India and US businesses
    """,
    'author': 'Technical Rajni',
    'website': 'https://www.technicalrajni.com',
    'license': 'OPL-1',
    'depends': ['account', 'sale', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_views.xml',
        'report/report_invoice.xml',
        'report/report_sale_order.xml',
        'report/report_purchase_order.xml',
        'report/report_delivery.xml',
        'report/report_base_layout.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'tr_fancy_reports/static/src/css/fancy_report.css',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 49.99,
    'currency': 'USD',
}
