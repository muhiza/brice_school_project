"""empty message

Revision ID: b158cf0671f5
Revises: e99df59d8017
Create Date: 2020-01-10 14:23:54.451653

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b158cf0671f5'
down_revision = 'e99df59d8017'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('income', sa.Column('Description', sa.String(length=200), nullable=True))
    op.drop_column('income', 'Desciption')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('income', sa.Column('Desciption', mysql.VARCHAR(length=200), nullable=True))
    op.drop_column('income', 'Description')
    # ### end Alembic commands ###
