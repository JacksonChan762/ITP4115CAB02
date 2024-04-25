"""1234567

Revision ID: 4416c95aefc8
Revises: 758a0ce76b15
Create Date: 2024-04-25 14:57:35.470537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4416c95aefc8'
down_revision = '758a0ce76b15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('supercat_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('subcat_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('product_super_cat_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('product_sub_cat_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'supercat', ['supercat_id'], ['id'])
        batch_op.create_foreign_key(None, 'subcat', ['subcat_id'], ['id'])
        batch_op.drop_column('super_cat_id')
        batch_op.drop_column('sub_cat_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sub_cat_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('super_cat_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('product_sub_cat_id_fkey', 'subcat', ['sub_cat_id'], ['id'])
        batch_op.create_foreign_key('product_super_cat_id_fkey', 'supercat', ['super_cat_id'], ['id'])
        batch_op.drop_column('subcat_id')
        batch_op.drop_column('supercat_id')

    # ### end Alembic commands ###
