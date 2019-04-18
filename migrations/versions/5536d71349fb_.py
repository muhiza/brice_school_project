"""empty message

Revision ID: 5536d71349fb
Revises: 8e6c77976c1a
Create Date: 2019-03-20 16:09:34.627910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5536d71349fb'
down_revision = '8e6c77976c1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abishyuwe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount_payed', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('ibiro', sa.Float(), nullable=True),
    sa.Column('done_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('abishyuwe')
    # ### end Alembic commands ###