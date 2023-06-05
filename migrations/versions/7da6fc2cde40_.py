"""empty message

Revision ID: 7da6fc2cde40
Revises: 9fd575282087
Create Date: 2023-06-05 23:00:20.354100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7da6fc2cde40'
down_revision = '9fd575282087'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('address_one',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('address_two',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('country',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('zip_code',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('zip_code',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
        batch_op.alter_column('country',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('address_two',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('address_one',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###
