"""empty message

Revision ID: 109e80fcd946
Revises: 8c1c45e381be
Create Date: 2024-09-11 11:20:23.600086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '109e80fcd946'
down_revision = '8c1c45e381be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_product_category_id_category'), 'category', ['category_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_product_category_id_category'), type_='foreignkey')
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###
