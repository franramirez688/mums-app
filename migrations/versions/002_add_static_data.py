"""add initial static data

Revision ID: 002_add_static_data
Revises: 001_initial_schema
Create Date: 2016-08-13 19:53:00.153788

"""

# revision identifiers, used by Alembic.
revision = '002_add_static_data'
down_revision = '001_initial_schema'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


# tables declarations
price_type_table = sa.table('price_types',
    sa.column('id', sa.Integer),
    sa.column('name', sa.String),
    sa.column('unit', sa.String)
)

product_type_table = sa.table('product_types',
    sa.column('id', sa.Integer),
    sa.column('name', sa.String),
)

product_table = sa.table('products',
    sa.column('id', sa.Integer),
    sa.column('name', sa.String),
    sa.column('price', sa.Float),
    sa.column('unit_for_price', sa.Integer),
    sa.column('price_type_id', sa.Integer),
    sa.column('product_type_id', sa.Integer),
)

# initial models data
price_types_data = [
    {'id': 1, 'name': 'grams', 'unit': 'gr'},
    {'id': 2, 'name': 'unit', 'unit': 'ud'},
]

product_types_data = [
    {'id': 1, 'name': 'main dish'},
    {'id': 2, 'name': 'dessert'},
    {'id': 3, 'name': 'drink'},
]

products_data = [
    {'name': 'Ensalada de espinacas', 'price': 1.65,
     'unit_for_price': 100, 'price_type_id': 1, 'product_type_id': 1},
    {'name': 'Tortellini a la carbonara', 'price': 1.30,
     'unit_for_price': 100, 'price_type_id': 1, 'product_type_id': 1},
    {'name': 'Pollo al curry', 'price': 1.55,
     'unit_for_price': 100, 'price_type_id': 1, 'product_type_id': 1},
    {'name': 'Arroz con verduras', 'price': 1.55,
     'unit_for_price': 100, 'price_type_id': 1, 'product_type_id': 1},
    {'name': 'Pizza primavera', 'price': 2.00,
     'unit_for_price': 1, 'price_type_id': 2, 'product_type_id': 1},
    {'name': 'Carne estofada', 'price': 2.15,
     'unit_for_price': 100, 'price_type_id': 1, 'product_type_id': 1},
    {'name': 'Agua', 'price': 1.20,
     'unit_for_price': 1, 'price_type_id': 2, 'product_type_id': 3},
    {'name': 'Zumo de naranja', 'price': 2.00,
     'unit_for_price': 1, 'price_type_id': 2, 'product_type_id': 3},
    {'name': 'Manzana', 'price': 2.00,
     'unit_for_price': 1, 'price_type_id': 2, 'product_type_id': 2},
    {'name': 'Tarta de queso', 'price': 2.50,
     'unit_for_price': 1, 'price_type_id': 2, 'product_type_id': 2},
]

def upgrade():
    op.bulk_insert(price_type_table, price_types_data)
    op.bulk_insert(product_type_table, product_types_data)
    op.bulk_insert(product_table, products_data)


def downgrade():
    op.execute("DELETE * FROM price_types")
    op.execute("DELETE * FROM product_types")
    op.execute("DELETE * FROM products")
