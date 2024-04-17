"""followers

Revision ID: 6092228cc420
Revises: 5871f9691439
Create Date: 2022-12-16 07:46:47.028088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6092228cc420'
down_revision = '5871f9691439'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###