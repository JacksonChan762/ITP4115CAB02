"""asd

Revision ID: d9eaba284c7d
Revises: 01597ea8be0f
Create Date: 2024-04-26 17:35:02.613647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9eaba284c7d'
down_revision = '01597ea8be0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('new', schema=None) as batch_op:
        batch_op.drop_constraint('new_author_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'author', ['author_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('new', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('new_author_id_fkey', 'user', ['author_id'], ['id'])

    # ### end Alembic commands ###