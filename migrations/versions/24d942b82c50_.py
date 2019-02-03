"""empty message

Revision ID: 24d942b82c50
Revises: 26dc8ff193e0
Create Date: 2019-02-03 15:59:30.966323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24d942b82c50'
down_revision = '26dc8ff193e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ububiko',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ayinjiye', sa.Integer(), nullable=True),
    sa.Column('ayasohotse', sa.Integer(), nullable=True),
    sa.Column('asigaye', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ububiko')
    # ### end Alembic commands ###
