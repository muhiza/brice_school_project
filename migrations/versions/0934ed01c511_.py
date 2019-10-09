"""empty message

Revision ID: 0934ed01c511
Revises: 
Create Date: 2019-10-09 17:59:23.113603

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0934ed01c511'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('CRMs_ibfk_1', 'CRMs', type_='foreignkey')
    op.drop_column('CRMs', 'cooperative_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('CRMs', sa.Column('cooperative_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('CRMs_ibfk_1', 'CRMs', 'cooperatives', ['cooperative_id'], ['id'])
    # ### end Alembic commands ###
