"""empty message

Revision ID: 09c562ba0162
Revises: fa6337bdbb1b
Create Date: 2020-01-27 14:59:14.550411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09c562ba0162'
down_revision = 'fa6337bdbb1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('assetsaccounting', sa.Column('Title', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assetsaccounting', 'Title')
    # ### end Alembic commands ###
