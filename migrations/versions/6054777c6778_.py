"""empty message

Revision ID: 6054777c6778
Revises: 29369794c1da
Create Date: 2020-04-03 16:36:20.006059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6054777c6778'
down_revision = '29369794c1da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arc_stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nimero', sa.Integer(), nullable=True),
    sa.Column('date', sa.String(length=255), nullable=True),
    sa.Column('izina_ribanza', sa.String(length=255), nullable=True),
    sa.Column('izina_rikurikira', sa.String(length=255), nullable=True),
    sa.Column('ubwoko', sa.String(length=255), nullable=True),
    sa.Column('ingano_kg', sa.String(length=255), nullable=True),
    sa.Column('igiciro_kg', sa.String(length=255), nullable=True),
    sa.Column('igiciro_cya_byose', sa.String(length=255), nullable=True),
    sa.Column('umusanzu_koperative', sa.String(length=255), nullable=True),
    sa.Column('ayishyurwa_umuhinzi', sa.String(length=255), nullable=True),
    sa.Column('telefoni', sa.String(length=255), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('arc_stock')
    # ### end Alembic commands ###