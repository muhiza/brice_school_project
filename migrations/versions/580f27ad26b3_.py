"""empty message

Revision ID: 580f27ad26b3
Revises: 4938899d036f
Create Date: 2020-02-08 23:52:14.028723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '580f27ad26b3'
down_revision = '4938899d036f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('archive',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('d_budget_used', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('archive')
    # ### end Alembic commands ###
