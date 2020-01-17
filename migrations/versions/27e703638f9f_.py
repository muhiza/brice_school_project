"""empty message

Revision ID: 27e703638f9f
Revises: 
Create Date: 2020-01-17 10:56:12.249602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27e703638f9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('sector', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('members', 'sector')
    # ### end Alembic commands ###
