"""empty message

Revision ID: 88700bc11fe2
Revises: 
Create Date: 2019-03-01 11:25:47.830060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88700bc11fe2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ubwisazures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('AssetDescription', sa.String(length=200), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('YearOfPurchase', sa.String(length=200), nullable=True),
    sa.Column('SalvageValue', sa.Integer(), nullable=True),
    sa.Column('UsefulLife', sa.String(length=200), nullable=True),
    sa.Column('Method', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.add_column(u'employees', sa.Column('is_accountant', sa.Boolean(), nullable=True))
    op.add_column(u'employees', sa.Column('is_manager', sa.Boolean(), nullable=True))
    op.add_column(u'employees', sa.Column('is_production_manager', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'employees', 'is_production_manager')
    op.drop_column(u'employees', 'is_manager')
    op.drop_column(u'employees', 'is_accountant')
    op.drop_table('ubwisazures')
    # ### end Alembic commands ###