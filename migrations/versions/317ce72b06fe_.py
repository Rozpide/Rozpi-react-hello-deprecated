"""empty message

Revision ID: 317ce72b06fe
Revises: d0415648e8d6
Create Date: 2025-01-14 21:08:16.030315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '317ce72b06fe'
down_revision = 'd0415648e8d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('participants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('tournament_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player_id'], ['players.id'], ),
    sa.ForeignKeyConstraint(['tournament_id'], ['tournaments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('matches', schema=None) as batch_op:
        batch_op.alter_column('resume',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('matches', schema=None) as batch_op:
        batch_op.alter_column('resume',
               existing_type=sa.TEXT(),
               nullable=False)

    op.drop_table('participants')
    # ### end Alembic commands ###
