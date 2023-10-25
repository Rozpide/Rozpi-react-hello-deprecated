"""empty message

Revision ID: 602678b528bb
Revises: b6be51ca29d7
Create Date: 2023-10-25 18:35:38.283120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '602678b528bb'
down_revision = 'b6be51ca29d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('friendship', schema=None) as batch_op:
        batch_op.add_column(sa.Column('friendship_status', sa.Enum(
            'Accepted', 'Pending', 'Deleted', name='friendship_type'), nullable=False, server_default='Pending'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('friendship', schema=None) as batch_op:
        batch_op.drop_column('friendship_status')

    # ### end Alembic commands ###
