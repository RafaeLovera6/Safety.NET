"""empty message

Revision ID: d77bd87fa6c5
Revises: 6d15abe243d3
Create Date: 2022-02-26 05:12:54.254166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd77bd87fa6c5'
down_revision = '6d15abe243d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Hash', sa.String(length=120), nullable=False),
    sa.Column('guest_email', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Hash')
    )
    op.create_table('permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token_association',
    sa.Column('token_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permission.id'], ),
    sa.ForeignKeyConstraint(['token_id'], ['token.id'], ),
    sa.PrimaryKeyConstraint('token_id', 'permission_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token_association')
    op.drop_table('permission')
    op.drop_table('token')
    # ### end Alembic commands ###
