"""empty message

Revision ID: f97dbf53e219
Revises: 6c76b15e29b8
Create Date: 2019-02-25 10:50:26.603539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f97dbf53e219'
down_revision = '6c76b15e29b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('ubwisazures')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ubwisazures',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('AssetDescription', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('department_id', mysql.VARCHAR(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], [u'departments.email'], name=u'ubwisazures_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('actives')
    # ### end Alembic commands ###
