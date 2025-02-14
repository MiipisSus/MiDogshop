"""empty message

Revision ID: 8c1c45e381be
Revises: 3e41d9ab4793
Create Date: 2024-09-11 09:44:23.188168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c1c45e381be'
down_revision = '3e41d9ab4793'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_address_user_id_user'), 'user', ['user_id'], ['id'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_address_id_address', type_='foreignkey')
        batch_op.drop_column('address_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_user_address_id_address', 'address', ['address_id'], ['id'])

    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_address_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
