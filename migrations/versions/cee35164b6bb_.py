"""empty message

Revision ID: cee35164b6bb
Revises: 
Create Date: 2019-02-18 10:01:05.110585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cee35164b6bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rukomatanyo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tariki_byakozwe', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('piyesi', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'InguzanyoZatanzwe', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'InguzanyoZatanzwe', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'bank', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'bank', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'ibicuruzwa', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ibicuruzwa', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'ibindiRukomatanya', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ibindiRukomatanya', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'ibiramba', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ibiramba', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'ikoreshwaRyimari', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ikoreshwaRyimari', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'inguzanyozabandi', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'inguzanyozabandi', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'inkunga', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'inkunga', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'isandukunshya', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'isandukunshya', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'ububiko', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ububiko', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'umugabaneShingiro', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'umugabaneShingiro', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    op.add_column(u'zones', sa.Column('rukomatanyo_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'zones', 'rukomatanyo', ['rukomatanyo_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'zones', type_='foreignkey')
    op.drop_column(u'zones', 'rukomatanyo_id')
    op.drop_constraint(None, 'umugabaneShingiro', type_='foreignkey')
    op.drop_column(u'umugabaneShingiro', 'rukomatanyo_id')
    op.drop_constraint(None, 'ububiko', type_='foreignkey')
    op.drop_column(u'ububiko', 'rukomatanyo_id')
    op.drop_constraint(None, 'isandukunshya', type_='foreignkey')
    op.drop_column(u'isandukunshya', 'rukomatanyo_id')
    op.drop_constraint(None, 'inkunga', type_='foreignkey')
    op.drop_column(u'inkunga', 'rukomatanyo_id')
    op.drop_constraint(None, 'inguzanyozabandi', type_='foreignkey')
    op.drop_column(u'inguzanyozabandi', 'rukomatanyo_id')
    op.drop_constraint(None, 'ikoreshwaRyimari', type_='foreignkey')
    op.drop_column(u'ikoreshwaRyimari', 'rukomatanyo_id')
    op.drop_constraint(None, 'ibiramba', type_='foreignkey')
    op.drop_column(u'ibiramba', 'rukomatanyo_id')
    op.drop_constraint(None, 'ibindiRukomatanya', type_='foreignkey')
    op.drop_column(u'ibindiRukomatanya', 'rukomatanyo_id')
    op.drop_constraint(None, 'ibicuruzwa', type_='foreignkey')
    op.drop_column(u'ibicuruzwa', 'rukomatanyo_id')
    op.drop_constraint(None, 'bank', type_='foreignkey')
    op.drop_column(u'bank', 'rukomatanyo_id')
    op.drop_constraint(None, 'InguzanyoZatanzwe', type_='foreignkey')
    op.drop_column(u'InguzanyoZatanzwe', 'rukomatanyo_id')
    op.drop_table('rukomatanyo')
    # ### end Alembic commands ###
