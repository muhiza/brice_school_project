"""empty message

Revision ID: 4938899d036f
Revises: 91e2425c37c0
Create Date: 2020-01-31 13:49:01.267825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4938899d036f'
down_revision = '91e2425c37c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=200), nullable=True),
    sa.Column('Date', sa.String(length=200), nullable=True),
    sa.Column('Category', sa.String(length=200), nullable=True),
    sa.Column('Account', sa.String(length=200), nullable=True),
    sa.Column('Amount', sa.String(length=200), nullable=True),
    sa.Column('Description', sa.String(length=200), nullable=True),
    sa.Column('cooperative_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('equitycategories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Category', sa.String(length=200), nullable=True),
    sa.Column('cooperative_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equitycategories')
    op.drop_table('equities')
    # ### end Alembic commands ###
