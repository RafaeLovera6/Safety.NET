"""empty message

Revision ID: 728be4457244
Revises: c5535b0aee29
Create Date: 2022-03-09 12:37:04.198127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '728be4457244'
down_revision = 'c5535b0aee29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guest', sa.Column('name', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('guest', 'name')
    # ### end Alembic commands ###
