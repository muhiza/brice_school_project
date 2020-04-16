"""empty message

Revision ID: f51a7b1793d7
Revises: 6054777c6778
Create Date: 2020-04-03 16:37:59.086950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f51a7b1793d7'
down_revision = '6054777c6778'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('arc_stock', sa.Column('season', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('arc_stock', 'season')
    # ### end Alembic commands ###