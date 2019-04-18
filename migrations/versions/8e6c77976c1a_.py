"""empty message

Revision ID: 8e6c77976c1a
Revises: 
Create Date: 2019-03-15 12:55:49.418981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e6c77976c1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('AccountName', sa.String(length=200), nullable=True),
    sa.Column('Description', sa.String(length=200), nullable=True),
    sa.Column('cooperative_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('assetsaccounting',
    sa.Column('id', sa.Integer(), nullable=False),
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
    op.create_table('budget',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Category', sa.String(length=200), nullable=True),
    sa.Column('Date', sa.String(length=200), nullable=True),
    sa.Column('Amount', sa.String(length=200), nullable=True),
    sa.Column('cooperative_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('expense',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=200), nullable=True),
    sa.Column('Date', sa.String(length=200), nullable=True),
    sa.Column('Category', sa.String(length=200), nullable=True),
    sa.Column('Account', sa.String(length=200), nullable=True),
    sa.Column('Amount', sa.String(length=200), nullable=True),
    sa.Column('Desciption', sa.String(length=200), nullable=True),
    sa.Column('cooperative_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('expensecategory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('AccountName', sa.String(length=200), nullable=True),
    sa.Column('cooperative_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('income',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=200), nullable=True),
    sa.Column('Date', sa.String(length=200), nullable=True),
    sa.Column('Category', sa.String(length=200), nullable=True),
    sa.Column('Account', sa.String(length=200), nullable=True),
    sa.Column('Amount', sa.String(length=200), nullable=True),
    sa.Column('Desciption', sa.String(length=200), nullable=True),
    sa.Column('cooperative_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['cooperative_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('incomecategory',
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
    op.drop_table('incomecategory')
    op.drop_table('income')
    op.drop_table('expensecategory')
    op.drop_table('expense')
    op.drop_table('budget')
    op.drop_table('assetsaccounting')
    op.drop_table('account')
    # ### end Alembic commands ###