"""sad

Revision ID: ff4e3a2b7efb
Revises: 2ffd53e38fa0
Create Date: 2024-04-27 13:57:22.253769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff4e3a2b7efb'
down_revision = '2ffd53e38fa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.drop_column('product_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###