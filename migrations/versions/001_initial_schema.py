"""empty message

Revision ID: 001_initial_schema
Revises: None
Create Date: 2016-10-23 13:35:36.865947

"""

# revision identifiers, used by Alembic.
revision = '001_initial_schema'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('price_types',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=32), nullable=True),
        sa.Column('unit', sa.String(length=8), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_types',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=32), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Text(), nullable=True),
        sa.Column('price', sa.Float(precision=2), nullable=True),
        sa.Column('unit_for_price', sa.Integer(), nullable=True),
        sa.Column('price_type_id', sa.Integer(), nullable=True),
        sa.Column('product_type_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['price_type_id'], ['price_types.id'], ),
        sa.ForeignKeyConstraint(['product_type_id'], ['product_types.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('product_types')
    op.drop_table('price_types')
    ### end Alembic commands ###
