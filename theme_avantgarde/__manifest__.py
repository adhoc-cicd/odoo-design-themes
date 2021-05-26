{
    'name': 'Avantgarde Theme',
    'description': 'Avantgarde is a sophisticated theme to inspire and impress',
    'category': 'Theme/Creative',
    'summary': 'Design, Fine Art, Artwork, Creative, Creativity, Galleries, Trends, Shows, Magazines, Blogs',
    'sequence': 150,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',
        'views/customizations.xml',

        ],
    'images': [
        'static/description/poster.jpg',
        'static/description/avantgarde_screenshot.jpg',
    ],
    'depends': ['theme_common'],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-avantgarde.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_avantgarde/static/src/js/tour.js',
        ],
    }
}