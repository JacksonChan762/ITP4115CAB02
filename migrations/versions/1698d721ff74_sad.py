"""sad

Revision ID: 1698d721ff74
Revises: 
Create Date: 2024-04-27 13:55:14.274323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1698d721ff74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('news_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'news', ['news_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('news_id')

    # ### end Alembic commands ###
