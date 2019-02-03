"""empty message

Revision ID: f1fbf075f7c4
Revises: 6f80ed35bf80
Create Date: 2019-02-03 16:33:22.690385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1fbf075f7c4'
down_revision = '6f80ed35bf80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inkunga',
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
    op.drop_table('inkunga')
    # ### end Alembic commands ###
