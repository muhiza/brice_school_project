"""empty message

Revision ID: 5df0783094d3
Revises: 
Create Date: 2019-04-25 14:38:15.534772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5df0783094d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abishyuwe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount_payed', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('member_name', sa.String(length=200), nullable=True),
    sa.Column('ibiro', sa.Float(), nullable=True),
    sa.Column('done_date', sa.Date(), nullable=True),
    sa.Column('umusaruro_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.ForeignKeyConstraint(['umusaruro_id'], ['umusarurob.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.add_column(u'umusarurob', sa.Column('UmusaruroGrade', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'umusarurob', 'UmusaruroGrade')
    op.drop_table('abishyuwe')
    # ### end Alembic commands ###